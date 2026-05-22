#!/usr/bin/env python3
"""
MKFS Phase 1 ballistics model.

Point-mass carrier trajectory with quadratic drag, flechette cloud dispersion,
and muzzle-velocity sensitivity analysis.

No external dependencies — stdlib only.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path

# --- Design constants (MKFS baseline) ---
V0_NOMINAL = 900.0  # m/s
ELEVATION_DEG = 30.0
CARRIER_MASS_KG = 0.188  # case + body + propellant residue (post-burn)
CARRIER_DIAM_M = 0.030
CARRIER_CD = 0.35
FLECHETTE_COUNT = 100
FLECHETTE_MASS_KG = 0.0013
# Dispersion from R_open onward (cone half-angle after mechanical release)
DISPERSION_HALF_ANGLE_DEG = 3.3
INITIAL_BURST_DIAMETER_M = 1.5
# Setback release window — fixed mechanical duration from primer initiation
T_RELEASE_S = 0.078
RHO_SEA_LEVEL = 1.225  # kg/m³
G = 9.80665

# Range targets (meters)
R_OPEN_NOMINAL_M = 61.0
R_BAND_MIN_M = 76.0
R_BAND_MAX_M = 152.0
R_MAX_M = 457.0


@dataclass
class TrajectoryPoint:
    t: float
    x: float
    y: float
    vx: float
    vy: float
    v: float


@dataclass
class RangeResult:
    range_ft: float
    range_m: float
    time_s: float
    velocity_ms: float


def ft(m: float) -> float:
    return m * 3.28084


def drag_accel(vx: float, vy: float) -> tuple[float, float]:
    v = math.hypot(vx, vy)
    if v < 1e-6:
        return 0.0, 0.0
    area = math.pi * (CARRIER_DIAM_M / 2) ** 2
    f_drag = 0.5 * RHO_SEA_LEVEL * CARRIER_CD * area * v * v
    ax = -f_drag * vx / (v * CARRIER_MASS_KG)
    ay = -f_drag * vy / (v * CARRIER_MASS_KG) - G
    return ax, ay


def simulate_trajectory(v0: float, elevation_deg: float, dt: float = 0.0005) -> list[TrajectoryPoint]:
    theta = math.radians(elevation_deg)
    vx, vy = v0 * math.cos(theta), v0 * math.sin(theta)
    x, y, t = 0.0, 0.0, 0.0
    points: list[TrajectoryPoint] = []

    while y >= 0.0 and t < 5.0:
        v = math.hypot(vx, vy)
        points.append(TrajectoryPoint(t, x, y, vx, vy, v))
        ax, ay = drag_accel(vx, vy)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        t += dt

    return points


def range_at_distance(points: list[TrajectoryPoint], target_m: float) -> RangeResult | None:
    for i in range(1, len(points)):
        p0, p1 = points[i - 1], points[i]
        if p0.x <= target_m <= p1.x:
            frac = (target_m - p0.x) / (p1.x - p0.x) if p1.x != p0.x else 0.0
            t = p0.t + frac * (p1.t - p0.t)
            v = p0.v + frac * (p1.v - p0.v)
            return RangeResult(ft(target_m), target_m, t, v)
    return None


def r_open_for_v0(v0: float, elevation_deg: float) -> float:
    """Option D: setback release at fixed mechanical time → R_open scales with V0."""
    theta = math.radians(elevation_deg)
    return v0 * math.cos(theta) * T_RELEASE_S


def pattern_diameter_at_range(range_m: float, r_open_m: float, half_angle_deg: float) -> float:
    """Cloud grows from release point; flechettes not yet dispersed before R_open."""
    if range_m <= r_open_m:
        return INITIAL_BURST_DIAMETER_M
    travel = range_m - r_open_m
    theta = math.radians(half_angle_deg)
    spread = 2.0 * travel * math.tan(theta)
    # Wake turbulence and flechette velocity spread (~10%)
    return (INITIAL_BURST_DIAMETER_M + spread) * 1.10


def hits_per_m2(count: int, diameter_m: float) -> float:
    area = math.pi * (diameter_m / 2) ** 2
    return count / area if area > 0 else 0.0


def sensitivity_analysis() -> list[dict]:
    results = []
    nominal_open = r_open_for_v0(V0_NOMINAL, ELEVATION_DEG)
    for pct in (-5, -3, 0, 3, 5):
        v0 = V0_NOMINAL * (1 + pct / 100)
        r_open_m = r_open_for_v0(v0, ELEVATION_DEG)
        r_open_ft = ft(r_open_m)
        shift_ft = r_open_ft - ft(nominal_open)
        results.append({
            "v0_pct": pct,
            "v0_ms": round(v0, 1),
            "r_open_ft": round(r_open_ft, 1),
            "r_open_shift_ft": round(shift_ft, 1),
            "pass_30ft": abs(shift_ft) <= 30,
        })
    return results


def main() -> None:
    pts = simulate_trajectory(V0_NOMINAL, ELEVATION_DEG)

    key_ranges_m = [
        (61, "R_open"),
        (76, "R_band_min"),
        (106.7, "350 ft"),
        (152, "R_band_max"),
        (457, "R_max"),
    ]

    time_table = []
    for dist_m, label in key_ranges_m:
        r = range_at_distance(pts, dist_m)
        if r:
            time_table.append({
                "label": label,
                "range_ft": round(r.range_ft, 1),
                "range_m": round(r.range_m, 1),
                "time_s": round(r.time_s, 4),
                "velocity_ms": round(r.velocity_ms, 1),
            })

    r_open_m = r_open_for_v0(V0_NOMINAL, ELEVATION_DEG)
    pattern_m = pattern_diameter_at_range(106.7, r_open_m, DISPERSION_HALF_ANGLE_DEG)
    density_single = hits_per_m2(FLECHETTE_COUNT, pattern_m)
    density_salvo_25 = hits_per_m2(FLECHETTE_COUNT * 25, pattern_m)

    band_results = []
    for dist_m in range(70, 160, 10):
        r = range_at_distance(pts, float(dist_m))
        if r:
            d = pattern_diameter_at_range(r.range_m, r_open_m, DISPERSION_HALF_ANGLE_DEG)
            band_results.append({
                "range_ft": round(r.range_ft, 0),
                "pattern_diameter_ft": round(ft(d), 1),
                "hits_per_m2_single": round(hits_per_m2(FLECHETTE_COUNT, d), 2),
                "hits_per_m2_salvo_25": round(hits_per_m2(FLECHETTE_COUNT * 25, d), 2),
            })

    output = {
        "parameters": {
            "v0_nominal_ms": V0_NOMINAL,
            "elevation_deg": ELEVATION_DEG,
            "carrier_mass_kg": CARRIER_MASS_KG,
            "carrier_cd": CARRIER_CD,
            "flechette_count": FLECHETTE_COUNT,
            "dispersion_half_angle_deg": DISPERSION_HALF_ANGLE_DEG,
        },
        "time_to_range_drag_corrected": time_table,
        "r_open_mechanical": {
            "r_open_ft": round(ft(r_open_m), 1),
            "r_open_m": round(r_open_m, 2),
            "t_release_s": T_RELEASE_S,
        },
        "pattern_at_350ft": {
            "pattern_diameter_ft": round(ft(pattern_m), 1),
            "pattern_diameter_m": round(pattern_m, 2),
            "hits_per_m2_single_round": round(density_single, 2),
            "hits_per_m2_salvo_25_tube": round(density_salvo_25, 2),
            "meets_15_25ft_target": 15 <= ft(pattern_m) <= 25,
            "meets_2_per_m2_single": density_single >= 2.0,
            "meets_2_per_m2_salvo_25": density_salvo_25 >= 2.0,
        },
        "band_pattern_envelope": band_results,
        "v0_sensitivity": sensitivity_analysis(),
    }

    out_dir = Path(__file__).parent
    json_path = out_dir / "ballistics_output.json"
    json_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    md_lines = [
        "# MKFS Ballistics Model Results",
        "",
        "**Generated by:** `ballistics_model.py`",
        "",
        "## Parameters",
        "",
        f"- V₀ = {V0_NOMINAL} m/s, elevation = {ELEVATION_DEG}°",
        f"- Carrier mass = {CARRIER_MASS_KG} kg, Cd = {CARRIER_CD}",
        f"- Flechette count = {FLECHETTE_COUNT}, dispersion half-angle = {DISPERSION_HALF_ANGLE_DEG}°",
        "",
        "## Time-to-Range (Drag-Corrected)",
        "",
        "| Label | Range (ft) | Range (m) | Time (s) | Velocity (m/s) |",
        "|-------|------------|-----------|----------|----------------|",
    ]
    for row in time_table:
        md_lines.append(
            f"| {row['label']} | {row['range_ft']} | {row['range_m']} | {row['time_s']} | {row['velocity_ms']} |"
        )

    ro = output["r_open_mechanical"]
    p = output["pattern_at_350ft"]
    md_lines.extend([
        "",
        "## Mechanical R_open (Option D)",
        "",
        f"- Release time: {ro['t_release_s']} s from primer",
        f"- R_open at nominal V₀: **{ro['r_open_ft']} ft** ({ro['r_open_m']} m)",
        "",
        "## Pattern at 350 ft",
        "",
        f"- Pattern diameter: **{p['pattern_diameter_ft']} ft** ({p['pattern_diameter_m']} m)",
        f"- Hits/m² (single round): **{p['hits_per_m2_single_round']}**",
        f"- Hits/m² (25-tube salvo): **{p['hits_per_m2_salvo_25_tube']}**",
        f"- Meets 15–25 ft target: {'Yes' if p['meets_15_25ft_target'] else 'No'}",
        f"- Meets ≥2 hits/m² (salvo): {'Yes' if p['meets_2_per_m2_salvo_25'] else 'No'}",
        "",
        "## Pattern Envelope (R_band)",
        "",
        "| Range (ft) | Pattern Dia (ft) | Hits/m² (1 rnd) | Hits/m² (25 rnd) |",
        "|------------|------------------|-----------------|------------------|",
    ])
    for row in band_results:
        md_lines.append(
            f"| {row['range_ft']} | {row['pattern_diameter_ft']} | "
            f"{row['hits_per_m2_single']} | {row['hits_per_m2_salvo_25']} |"
        )

    md_lines.extend([
        "",
        "## V₀ Sensitivity (±5%)",
        "",
        "| V₀ Δ% | V₀ (m/s) | R_open (ft) | Shift (ft) | Pass ±30 ft |",
        "|-------|----------|-------------|------------|-------------|",
    ])
    for row in output["v0_sensitivity"]:
        md_lines.append(
            f"| {row['v0_pct']:+d}% | {row['v0_ms']} | {row['r_open_ft']} | {row['r_open_shift_ft']:+} | {'Yes' if row['pass_30ft'] else 'No'} |"
        )

    md_path = out_dir / "BALLISTICS_RESULTS.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(
        f"Pattern at 350 ft: {p['pattern_diameter_ft']} ft, "
        f"salvo density {p['hits_per_m2_salvo_25_tube']} hits/m²"
    )


if __name__ == "__main__":
    main()

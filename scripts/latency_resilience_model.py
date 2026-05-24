#!/usr/bin/env python3
"""
MKFS Phase 9 latency and packet-loss resilience model.

Models position uncertainty under track delay, pattern overlap from volume
fire, and cue delivery under packet loss.

Run: python scripts/latency_resilience_model.py
Output: scripts/latency_resilience_output.json (CI: .github/workflows/ci.yml)

Maps to docs/NETWORK_ARCHITECTURE.md:
  - position_error_cv / position_error_with_accel -> section 4.3 (predictor)
  - pattern_overlap_fraction -> section 5 (quantitative grounding)
  - cue_delivery_probability -> section 10 (packet loss)

Stdlib only, CI-safe.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# Baseline from ballistics model @ 350 ft (BALLISTICS_RESULTS.md)
PATTERN_DIAMETER_M = 7.47  # ~24.5 ft
MPH_TO_MPS = 0.44704
FT_TO_M = 0.3048

# Critic baseline: 60 mph, 250 ms delay -> 22.0 ft lead error (NETWORK_ARCHITECTURE.md section 1)
BASELINE_SPEED_MPH = 60.0
BASELINE_DELAY_MS = 250.0
# Local predictor: effective delay = 25% of measured latency (concept; HIL T5-N02)
PREDICTOR_DELAY_FRACTION = 0.25


def mph_to_mps(mph: float) -> float:
    return mph * MPH_TO_MPS


def position_error_cv(speed_mps: float, delay_s: float) -> float:
    """Constant-velocity lead error: delta_x = v * tau (meters). NETWORK_ARCHITECTURE section 4.3."""
    return abs(speed_mps * delay_s)


def position_error_with_accel(
    speed_mps: float,
    delay_s: float,
    accel_mps2: float = 0.0,
    speed_sigma: float = 0.0,
) -> float:
    """
    Combined position uncertainty (meters). NETWORK_ARCHITECTURE section 4.3.

    sigma_pos = sqrt((v*tau)^2 + (0.5*a*tau^2)^2 + (sigma_v*tau)^2)
    """
    cv = speed_mps * delay_s
    accel_term = 0.5 * abs(accel_mps2) * delay_s * delay_s
    speed_term = speed_sigma * delay_s
    return math.sqrt(cv * cv + accel_term * accel_term + speed_term * speed_term)


def pattern_overlap_fraction(pattern_diameter_m: float, miss_distance_m: float) -> float:
    """
    Fraction of circular pattern covering a point target at miss_distance from aim center.

    NETWORK_ARCHITECTURE section 5. Assumes: symmetric cloud, point target, aim at
    last reported position (miss = v*tau without predictor). Chord model: overlap
    width at miss distance / pattern diameter. Returns 0.0 if miss >= radius.
    """
    if pattern_diameter_m <= 0:
        return 0.0
    radius = pattern_diameter_m / 2.0
    if miss_distance_m >= radius:
        return 0.0
    overlap_width = 2.0 * math.sqrt(radius * radius - miss_distance_m * miss_distance_m)
    return min(1.0, overlap_width / pattern_diameter_m)


def cue_delivery_probability(packet_loss_rate: float, retries: int = 0) -> float:
    """
    P(at least one cue packet arrives). NETWORK_ARCHITECTURE section 10.

    P(deliver) = 1 - p^(1 + retries) for independent trials.
    """
    p = max(0.0, min(1.0, packet_loss_rate))
    return 1.0 - math.pow(p, 1 + retries)


def delay_sweep() -> list[dict]:
    """
    Position error vs delay at 30/60/90 mph.

    pattern_overlap is WITHOUT local predictor (raw v*tau miss only).
    """
    rows = []
    for mph in (30, 60, 90):
        v = mph_to_mps(mph)
        for delay_ms in (50, 100, 150, 250, 350, 500):
            delay_s = delay_ms / 1000.0
            err_m = position_error_cv(v, delay_s)
            overlap = pattern_overlap_fraction(PATTERN_DIAMETER_M, err_m)
            rows.append({
                "speed_mph": mph,
                "delay_ms": delay_ms,
                "lead_error_m": round(err_m, 2),
                "lead_error_ft": round(err_m / FT_TO_M, 1),
                "pattern_overlap": round(overlap, 3),
            })
    return rows


def packet_loss_sweep(
    overlap_at_baseline: float,
    overlap_with_predictor: float,
) -> list[dict]:
    """Overlap after packet loss: pattern_overlap * cue_delivery_prob."""
    rows = []
    for loss_pct in (0, 5, 10, 15, 20, 30):
        p_loss = loss_pct / 100.0
        p_deliver = cue_delivery_probability(p_loss, retries=0)
        p_deliver_retry = cue_delivery_probability(p_loss, retries=2)
        rows.append({
            "packet_loss_pct": loss_pct,
            "cue_delivery_prob": round(p_deliver, 3),
            "cue_delivery_prob_2retry": round(p_deliver_retry, 3),
            "pattern_overlap_at_baseline": round(overlap_at_baseline * p_deliver, 3),
            "pattern_overlap_with_predictor": round(overlap_with_predictor * p_deliver, 3),
        })
    return rows


def baseline_reference() -> dict:
    """Critic baseline: 60 mph, 250 ms -> 22.0 ft lead error."""
    v = mph_to_mps(BASELINE_SPEED_MPH)
    delay_s = BASELINE_DELAY_MS / 1000.0
    err_m = position_error_cv(v, delay_s)
    effective_delay_s = delay_s * PREDICTOR_DELAY_FRACTION
    overlap_no_pred = pattern_overlap_fraction(PATTERN_DIAMETER_M, err_m)
    overlap_pred = pattern_overlap_fraction(
        PATTERN_DIAMETER_M, position_error_cv(v, effective_delay_s)
    )
    pred_ms = round(BASELINE_DELAY_MS * PREDICTOR_DELAY_FRACTION, 1)
    return {
        "speed_mph": BASELINE_SPEED_MPH,
        "delay_ms": BASELINE_DELAY_MS,
        "lead_error_m": round(err_m, 2),
        "lead_error_ft": round(err_m / FT_TO_M, 1),
        "pattern_diameter_ft": round(PATTERN_DIAMETER_M / FT_TO_M, 1),
        "pattern_radius_ft": round(PATTERN_DIAMETER_M / 2.0 / FT_TO_M, 1),
        "pattern_overlap_at_baseline": round(overlap_no_pred, 3),
        "predictor_effective_delay_ms": pred_ms,
        "pattern_overlap_with_predictor": round(overlap_pred, 3),
        "note": (
            f"At {BASELINE_DELAY_MS} ms / {BASELINE_SPEED_MPH} mph: "
            f"pattern_overlap_at_baseline={round(overlap_no_pred, 3)} "
            f"(lead_error_ft={round(err_m / FT_TO_M, 1)} > pattern_radius_ft=12.3). "
            f"pattern_overlap_with_predictor={round(overlap_pred, 3)} "
            f"at predictor_effective_delay_ms={pred_ms}."
        ),
    }


def main() -> None:
    baseline = baseline_reference()
    output = {
        "parameters": {
            "pattern_diameter_m": PATTERN_DIAMETER_M,
            "baseline_speed_mph": BASELINE_SPEED_MPH,
            "baseline_delay_ms": BASELINE_DELAY_MS,
            "predictor_delay_fraction": PREDICTOR_DELAY_FRACTION,
        },
        "baseline_reference": baseline,
        "delay_sweep": delay_sweep(),
        "packet_loss_sweep": packet_loss_sweep(
            baseline["pattern_overlap_at_baseline"],
            baseline["pattern_overlap_with_predictor"],
        ),
    }

    out_dir = Path(__file__).parent
    json_path = out_dir / "latency_resilience_output.json"
    json_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    ref = output["baseline_reference"]
    print("# MKFS Latency Resilience Model - Summary")
    print()
    print(f"Baseline: {ref['speed_mph']} mph + {ref['delay_ms']} ms -> {ref['lead_error_ft']} ft lead error")
    print(f"Pattern @ 350 ft: {ref['pattern_diameter_ft']} ft diameter ({ref['pattern_radius_ft']} ft radius)")
    print(f"pattern_overlap_at_baseline: {ref['pattern_overlap_at_baseline']:.3f}")
    print(
        f"pattern_overlap_with_predictor ({ref['predictor_effective_delay_ms']} ms effective): "
        f"{ref['pattern_overlap_with_predictor']:.3f}"
    )
    print()
    print("delay_sweep.pattern_overlap excludes local predictor (raw v*tau miss only).")
    print()
    print("## Delay sweep (selected; no predictor)")
    print("| mph | delay_ms | lead_ft | overlap |")
    print("|-----|----------|---------|---------|")
    for row in output["delay_sweep"]:
        if row["delay_ms"] in (100, 250, 500):
            print(
                f"| {row['speed_mph']} | {row['delay_ms']} | "
                f"{row['lead_error_ft']} | {row['pattern_overlap']:.2f} |"
            )
    print()
    print("## Packet loss @ baseline (overlap * cue_delivery_prob)")
    print("| loss_pct | P(deliver) | pattern_overlap_at_baseline | pattern_overlap_with_predictor |")
    print("|----------|------------|-----------------------------|--------------------------------|")
    for row in output["packet_loss_sweep"]:
        if row["packet_loss_pct"] in (0, 10, 20, 30):
            print(
                f"| {row['packet_loss_pct']} | {row['cue_delivery_prob']:.2f} | "
                f"{row['pattern_overlap_at_baseline']:.2f} | "
                f"{row['pattern_overlap_with_predictor']:.2f} |"
            )
    print()
    print(f"Wrote {json_path}")


if __name__ == "__main__":
    main()

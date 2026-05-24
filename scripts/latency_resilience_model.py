#!/usr/bin/env python3
"""
MKFS Phase 9 latency and packet-loss resilience model.

Models position uncertainty growth under track delay, pattern overlap
partial mitigation from volume fire, and cue delivery under packet loss.

Relates to docs/NETWORK_ARCHITECTURE.md — stdlib only, CI-safe.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# Baseline from ballistics model @ 350 ft
PATTERN_DIAMETER_M = 7.47  # ~24.5 ft
MPH_TO_MPS = 0.44704
FT_TO_M = 0.3048

# Critic baseline: 60 mph, 250 ms delay → ~22 ft lead error
BASELINE_SPEED_MPH = 60.0
BASELINE_DELAY_MS = 250.0


def mph_to_mps(mph: float) -> float:
    return mph * MPH_TO_MPS


def position_error_cv(speed_mps: float, delay_s: float) -> float:
    """Constant-velocity lead error: Δx ≈ v · τ (meters)."""
    return abs(speed_mps * delay_s)


def position_error_with_accel(
    speed_mps: float,
    delay_s: float,
    accel_mps2: float = 0.0,
    speed_sigma: float = 0.0,
) -> float:
    """
    Combined position uncertainty (meters).

    σ_pos ≈ sqrt((v·τ)² + (0.5·a·τ²)² + (σ_v·τ)²)
    """
    cv = speed_mps * delay_s
    accel_term = 0.5 * abs(accel_mps2) * delay_s * delay_s
    speed_term = speed_sigma * delay_s
    return math.sqrt(cv * cv + accel_term * accel_term + speed_term * speed_term)


def pattern_overlap_fraction(pattern_diameter_m: float, miss_distance_m: float) -> float:
    """
    Rough fraction of circular pattern still covering a point target.

    Assumes target at miss_distance from cloud center; overlap = fraction
    of pattern radius that still reaches the target (linear chord model).
    Returns 0.0–1.0; 1.0 = target inside pattern center.
    """
    if pattern_diameter_m <= 0:
        return 0.0
    radius = pattern_diameter_m / 2.0
    if miss_distance_m >= radius:
        return 0.0
    # Chord half-width at miss distance from center
    overlap_width = 2.0 * math.sqrt(radius * radius - miss_distance_m * miss_distance_m)
    return min(1.0, overlap_width / pattern_diameter_m)


def cue_delivery_probability(packet_loss_rate: float, retries: int = 0) -> float:
    """
    Probability at least one cue packet arrives.

    P(deliver) = 1 - p^(1 + retries) for independent trials.
    """
    p = max(0.0, min(1.0, packet_loss_rate))
    return 1.0 - math.pow(p, 1 + retries)


def engagement_success_estimate(miss_m: float, pattern_diameter_m: float) -> float:
    """
    Conservative engagement success proxy from pattern overlap.

    Uses pattern_overlap_fraction; expandable to Pk models later.
    """
    return pattern_overlap_fraction(pattern_diameter_m, miss_m)


def delay_sweep() -> list[dict]:
    """Position error vs delay at 30/60/90 mph."""
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
                "engagement_proxy": round(overlap, 3),
            })
    return rows


def packet_loss_sweep() -> list[dict]:
    """Cue delivery and effective engagement under loss, with/without predictor."""
    rows = []
    v = mph_to_mps(BASELINE_SPEED_MPH)
    delay_s = BASELINE_DELAY_MS / 1000.0
    miss_no_predict = position_error_cv(v, delay_s)
    miss_with_predict = position_error_cv(v, delay_s * 0.25)  # local predictor cuts effective delay

    for loss_pct in (0, 5, 10, 15, 20, 30):
        p_loss = loss_pct / 100.0
        p_deliver = cue_delivery_probability(p_loss, retries=0)
        p_deliver_retry = cue_delivery_probability(p_loss, retries=2)
        eng_no_pred = engagement_success_estimate(miss_no_predict, PATTERN_DIAMETER_M)
        eng_pred = engagement_success_estimate(miss_with_predict, PATTERN_DIAMETER_M)
        rows.append({
            "packet_loss_pct": loss_pct,
            "cue_delivery_prob": round(p_deliver, 3),
            "cue_delivery_prob_2retry": round(p_deliver_retry, 3),
            "engagement_no_predictor": round(eng_no_pred * p_deliver, 3),
            "engagement_with_predictor": round(eng_pred * p_deliver, 3),
        })
    return rows


def baseline_reference() -> dict:
    """Critic baseline: 60 mph, 250 ms → ~22 ft."""
    v = mph_to_mps(BASELINE_SPEED_MPH)
    delay_s = BASELINE_DELAY_MS / 1000.0
    err_m = position_error_cv(v, delay_s)
    return {
        "speed_mph": BASELINE_SPEED_MPH,
        "delay_ms": BASELINE_DELAY_MS,
        "lead_error_m": round(err_m, 2),
        "lead_error_ft": round(err_m / FT_TO_M, 1),
        "pattern_diameter_ft": round(PATTERN_DIAMETER_M / FT_TO_M, 1),
        "pattern_overlap_at_baseline": round(
            pattern_overlap_fraction(PATTERN_DIAMETER_M, err_m), 3
        ),
        "note": "Volume fire partially absorbs lead error; does not eliminate it.",
    }


def main() -> None:
    output = {
        "parameters": {
            "pattern_diameter_m": PATTERN_DIAMETER_M,
            "baseline_speed_mph": BASELINE_SPEED_MPH,
            "baseline_delay_ms": BASELINE_DELAY_MS,
        },
        "baseline_reference": baseline_reference(),
        "delay_sweep": delay_sweep(),
        "packet_loss_sweep": packet_loss_sweep(),
    }

    out_dir = Path(__file__).parent
    json_path = out_dir / "latency_resilience_output.json"
    json_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    ref = output["baseline_reference"]
    print("# MKFS Latency Resilience Model — Summary")
    print()
    print(f"Baseline: {ref['speed_mph']} mph + {ref['delay_ms']} ms -> "
          f"{ref['lead_error_ft']} ft lead error")
    print(f"Pattern @ 350 ft: {ref['pattern_diameter_ft']} ft diameter")
    print(f"Pattern overlap at baseline: {ref['pattern_overlap_at_baseline']:.1%}")
    print()
    print("## Delay sweep (selected)")
    print("| mph | delay_ms | lead_ft | overlap |")
    print("|-----|----------|---------|---------|")
    for row in output["delay_sweep"]:
        if row["delay_ms"] in (100, 250, 500):
            print(
                f"| {row['speed_mph']} | {row['delay_ms']} | "
                f"{row['lead_error_ft']} | {row['pattern_overlap']:.2f} |"
            )
    print()
    print(f"Wrote {json_path}")


if __name__ == "__main__":
    main()

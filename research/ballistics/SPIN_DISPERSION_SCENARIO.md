# MKFS Spin Dispersion Scenario

**Document ID:** MKFS-BAL-SPIN-001  
**Version:** 0.1 (Phase 8)  
**Related:** [RIFLING_SPIN_ANALYSIS.md](../../docs/RIFLING_SPIN_ANALYSIS.md) | [ballistics_model.py](ballistics_model.py) | [BALLISTICS_RESULTS.md](BALLISTICS_RESULTS.md)

---

## 1. Purpose

Compare **smooth bore baseline** (D-002 Option D) vs optional **light twist (1:60)** dispersion at 350 ft for the 2×1 strip (136 tubes). Baseline tubes remain smooth bore per [RIFLING_SPIN_ANALYSIS.md](../../docs/RIFLING_SPIN_ANALYSIS.md).

---

## 2. Model Variants

| Variant | V₀ (m/s) | Dispersion half-angle | Notes |
|---------|----------|----------------------|-------|
| `smooth_baseline` | 900.0 | **3.3°** | Production baseline — smooth 33 mm bore |
| `light_twist_1_60` | 891.0 (−1%) | **4.1°** | Phase 2 experiment only — estimated +0.8° from spin peel coupling |

*Model uses `FLECHETTE_COUNT = 100` as internal density term (~40 Ti BBs per puck in ICD).*

---

## 3. Comparison @ 350 ft — 2×1 Strip (136 tubes)

Run `python ballistics_model.py` to regenerate. Representative values:

| Variant | R_open (ft) | Pattern dia (ft) | Hits/m² (136-tube) |
|---------|-------------|------------------|---------------------|
| Smooth baseline | 199.5 | 24.5 | **310.1** |
| Light twist 1:60 | 197.5 | 29.5 | **214.5** |

**Interpretation:** Light twist widens the cone slightly but costs ~1% muzzle velocity from engraving. Smooth bore + Option D peel remains the recommended baseline; rifled tubes are a controlled dispersion experiment only.

---

## 4. Test Hook (T2)

If Phase 2 rifling tubes are built:

| Test | Pass |
|------|------|
| Side-by-side smooth vs 1:60 @ 350 ft | Pattern envelope documented; no regression on R_open timing |
| Witness screens | Smooth bore meets T2-002 (15–25 ft @ 350 ft) |

---

## 5. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 8 spin variant comparison table |

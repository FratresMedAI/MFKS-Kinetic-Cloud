# MKFS Deployment Mechanism Down-Select

**Document ID:** MKFS-DOC-DEPLOY-002  
**Decision:** D-002  
**Recommendation:** **Option D confirmed** as baseline; Option A noted as Phase 2 hybrid path  
**Related:** [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) | [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) | [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md)

---

## 1. Review Summary

Phase 1 analysis validates Option D (spring-loaded petal / setback release) as the MKFS baseline deployment mechanism.

| Option | Phase 1 Result | Disposition |
|--------|----------------|-------------|
| A — Centrifugal | Viable as dispersion enhancer | **Deferred hybrid** (D+A) |
| B — Clockwork | High part count; setback sensitivity | **Rejected** |
| C — Drag sleeve | Band width too wide for 250–500 ft | **Rejected** |
| **D — Setback petal** | Meets TRL, safety, and range targets | **Selected** |

---

## 2. Validation Evidence

### Ballistics (P1-003, P1-005)

- Drag-corrected time-to-range table generated — see [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md)
- Pattern at 350 ft: within 15–25 ft diameter target
- V₀ sensitivity ±5%: `R_open` shift within ±30 ft at all tested points

### Flechette Pack (P1-004)

- 100 × Ti-6Al-4V flechettes at 1.3 g — see [FLECHETTE_TRADE_STUDY.md](../research/ballistics/FLECHETTE_TRADE_STUDY.md)

### ICD (P1-001)

- Mechanical interface defined — see [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md)

---

## 3. Environmental Assessment (P1-006)

| Factor | Option D Impact | Mitigation | Band Shift |
|--------|-----------------|------------|------------|
| -25°F to 125°F | Spring rate ±8% | Band index shims; propellant temp comp at launcher | ≤ ±10% |
| Wind (30 kt cross) | Low (release during launch) | FCU elevation adjust | N/A at release |
| Altitude (5000 ft) | Air density ↓ → `V_0` ↑ ~3% | Standard band index | ≤ ±5% |
| Rain | Low | Sealed case | None |

**Conclusion:** Environmental drift within NFR-005 limits.

---

## 4. Hybrid Path (Optional Phase 2)

If pattern testing shows insufficient radial spread, add centrifugal collet (Option A) **downstream** of petal release — no change to baseline safety case (still kinetic-only, no energetics).

---

## 5. Decision Record

| ID | Decision | Status |
|----|----------|--------|
| D-002 | Option D baseline | **Closed — Option D** |
| D-001 | 30 mm caliber | **Closed — 30 mm** |

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 1 down-select complete |

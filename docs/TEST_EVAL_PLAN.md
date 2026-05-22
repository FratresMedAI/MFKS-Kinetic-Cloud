# MKFS Test and Evaluation Plan

**Document ID:** MKFS-DOC-TEST-001  
**Version:** 0.1 (Phase 4 draft)  
**Related:** [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) | [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md)

---

## 1. Test Phases

| Phase | Test Type | Location | Key Objectives |
|-------|-----------|----------|----------------|
| T1 | Component | Lab / indoor range | Petal release, primer, mechanism FR |
| T2 | Ballistics | Outdoor range 500 m | `R_open`, pattern at 350 ft, `V_0` |
| T3 | Array | Range + HIL | Salvo timing, pod swap, FCU states |
| T4 | Vehicle | Platform proving ground | Mount, power, dual-array coverage |
| T5 | System | Combined | Swarm surrogate engagement |

---

## 2. T1 — Component Tests

| Test ID | Description | Pass Criteria |
|---------|-------------|---------------|
| T1-001 | Setback petal release (high-speed video) | Release at 85% peak G ± 5% |
| T1-002 | Band index positions (3 settings) | `R_open` within band table ± 30 ft |
| T1-003 | Drop test (1.5 m, 6 orientations) | No inadvertent release |
| T1-004 | Temperature chamber (-25°F / 125°F) | Function rate ≥ 99% |

---

## 3. T2 — Ballistics Tests

| Test ID | Description | Pass Criteria |
|---------|-------------|---------------|
| T2-001 | Doppler `V_0` (n=30) | 900 m/s ± 45 m/s |
| T2-002 | Witness screens at 200, 350, 500 ft | Pattern diameter 15–25 ft at 350 ft |
| T2-003 | Pattern density (350 ft, **136-tube 2×1 strip** salvo) | ≥ 2 **Ti BBs**/m² |
| T2-004 | `V_0` sensitivity (cold/hot propellant) | `R_open` shift ≤ 30 ft |

---

## 4. T3 — Array / FCU Tests

| Test ID | Description | Pass Criteria |
|---------|-------------|---------------|
| T3-001 | Single tube fire | Clean ignition, no hangfire > 500 ms |
| T3-002 | **136-tube salvo** (2 ms spacing, LAST_DITCH_FULL) | 100% tube fire; no cross-ignition |
| T3-003 | Pod swap time | < 5 min, 2 crew |
| T3-004 | FCU state machine | All transitions per FCU spec |
| T3-005 | EMI (MIL-STD-461 CE/RE) | No false fire |

---

## 5. T4 — Vehicle Integration

| Test ID | Description | Pass Criteria |
|---------|-------------|---------------|
| T4-001 | Static mount (each adapter kit) | Bolt pattern, CG within limits |
| T4-002 | Road march (100 km) | No latch failure, no pod shift |
| T4-003 | Dual-array overlap | 360° coverage map verified |
| T4-004 | Power budget | ≤ 350 W peak on vehicle bus |

---

## 6. T5 — System Engagement *(Phase 4+)*

**Desk exercise:** [SWARM_TEST_CONCEPT.md](SWARM_TEST_CONCEPT.md) (MKFS-DOC-T5-001)

| Test ID | Description | Pass Criteria |
|---------|-------------|---------------|
| T5-001 | Multi-target drone surrogates | ≥ 80% kill in swarm scenario |
| T5-002 | End-to-end cue-to-fire latency | < 2 s (with vehicle sensors) |
| T5-003 | Salvo density @ 350 ft | ≥ 300 hits/m² (136-tube strip) |
| T5-004 | Fratricide | Zero strikes in inhibit zone — [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md) |

---

## 7. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial T&E plan outline |
| 0.2 | 2026-05-22 | T5 expanded; links to SWARM_TEST_CONCEPT, FRATRICIDE_DECONFLICTION |

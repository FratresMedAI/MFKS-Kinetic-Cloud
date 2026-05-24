# MKFS M1 Concept Specification

**Document ID:** MKFS-DOC-M1-001  
**Version:** 0.1  
**Status:** Concept | Phase 9  
**Purpose:** Single source of truth for M1 concept — configuration, performance, FCU/C2, and open items.  
**Key Decisions:** See [DECISIONS.md](DECISIONS.md) — D-003 (CAN), D-011 (PUCK-A/B), D-013 (CAN-only fire)  
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md); hardware validation P9-007  
**Related Documents:** [SYSTEM_SPEC.md](SYSTEM_SPEC.md) | [REQUIREMENTS.md](REQUIREMENTS.md) | [MKFS_CORE_ENHANCEMENTS.md](MKFS_CORE_ENHANCEMENTS.md) | [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md)

> **M1 summary SoT.** Detailed requirements remain in [REQUIREMENTS.md](REQUIREMENTS.md); full subsystem index in [SYSTEM_SPEC.md](SYSTEM_SPEC.md).

---

## 1. Purpose

**MKFS M1** is a **last-ditch terminal defense** capability — kinetic-only, non-explosive, APS-analogue protection against **close-in drone swarms** inside **~500 yd**. Volume and survival over single-target precision.

---

## 2. M1 Configuration

### Packaging

| Package | Face | Tubes (approx.) | Role |
|---------|------|-----------------|------|
| Appliqué strip | 2×1 ft | **136** | Hull / bustle / roof |
| Appliqué strip | 3×1 ft | **208** | Extended coverage |
| Pan-tilt turret | 2×2 ft / deck | **289** | Moving-head magazine × 3–4 decks |

### Projectile

| Element | M1 baseline |
|---------|-------------|
| Cartridge | `MKFS-CART-PUCK` — **31 mm × 28 mm** |
| Payload | **~40 × Ti-6Al-4V BBs** per puck (hollow-point skirt peel) |
| Deployment | Mechanical setback @ **`R_open` ≈ 200 ft** |
| Guidance | **None** in round — electronic fire at launcher only |

### Fire control

| Element | M1 baseline |
|---------|-------------|
| Bus | Vehicle **CAN** 500 kbps |
| Addressing | **Every tube individually addressable** |
| Salvo profiles | SECTOR, SWARM_WIDE, LAST_DITCH_FULL, TURRET_RIPPLE |
| Operator | **ARMED** required — no autonomous fire |

### Platforms (adapter kits)

Stryker, M2 Bradley, M113, LAV-25, MRAP — see [adapters/README.md](adapters/README.md).

---

## 3. Performance Requirements (M1)

### Design constants

| Constant | Value |
|----------|-------|
| `R_open` | ~200 ft |
| `R_band` | 250–500 ft (peak effect) |
| `R_max` | ~500 yd |
| `V_0` | 900 m/s ± 45 m/s |
| Pattern @ 350 ft | **~24.5 ft** diameter |

### Salvo density @ 350 ft ([SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md))

| Config | Tubes | Hits/m² |
|--------|-------|---------|
| 2×1 strip | 136 | **310** |
| 3×1 strip | 208 | **474** |
| Turret 1 deck | 289 | **659** |
| Turret 3-deck dump | 867 | **1,977** |

### Timing

| Package | LAST_DITCH_FULL *(2 ms inter-tube)* |
|---------|-------------------------------------|
| 2×1 strip | ~0.27 s |
| 3×1 strip | ~0.42 s |
| Turret deck | ~0.58 s |
| Turret 3-deck | ~1.7 s |

### Legacy verification targets (from [REQUIREMENTS.md](REQUIREMENTS.md))

| Parameter | Requirement |
|-----------|-------------|
| Swarm density | ≥ 2 hits/m² *(M1 exceeds by orders of magnitude at 136+ tubes)* |
| Pod swap | < 5 min *(target < 3 min — Enhancement E)* |
| Function rate | ≥ 99.5% |

---

## 4. FCU / C2 Summary (M1)

Three-tier separation ([NETWORK_ARCHITECTURE.md](NETWORK_ARCHITECTURE.md)):

| Tier | Function | Link |
|------|----------|------|
| 1 | Fire commit | CAN only — **D-013** |
| 2 | FCU edge: fusion, triage, **CV predictor**, tube select | FCU + CAN |
| 3 | Mission intent (ROE, inhibit) | C4ISR *(optional, lossy OK)* |

**Latency model baseline** ([latency_resilience_output.json](../scripts/latency_resilience_output.json)):

| Field | Value |
|-------|-------|
| `lead_error_ft` @ 250 ms / 60 mph | **22.0** |
| `pattern_overlap_at_baseline` | **0.0** |
| `predictor_effective_delay_ms` | **62.5** |
| `pattern_overlap_with_predictor` | **0.894** |

→ [FCU_EDGE_PREDICTOR_ONEPAGER.md](FCU_EDGE_PREDICTOR_ONEPAGER.md)

**Degradation ladder:** Levels 0–4 — CAN tracks + predictor through manual az/el. Operator ARMED at every level.

---

## 5. Key Functional Requirements (subset)

| ID | Requirement |
|----|-------------|
| FR-001 | Kinetic only — no explosives |
| FR-003 | Volume effect on drone swarms — last-ditch |
| FR-007 | High-volume salvo from individually addressed tubes |
| FR-009 | Electronic tube selection — core architecture |
| FR-013 | Terminal "don't die" when primary AD absent |

Full FR/NFR tables: [REQUIREMENTS.md](REQUIREMENTS.md) §4–5.

---

## 6. M1 Enhancements (in scope)

From [MKFS_CORE_ENHANCEMENTS.md](MKFS_CORE_ENHANCEMENTS.md):

- **A** — FCU at 136/208/289+ tube scale (no 25-tube cap)
- **B** — Turret staggered deck ripple (+50 ms between decks)
- **C** — Dual-strip 20 ms phase offset
- **D** — Co-mounted drone radar/EM on tile
- **E** — Faster pod swap target < 3 min
- **G** — Edge C2, local predictor, degradation ladder

**Rejected for M1:** LR puck variants, Javelin-form pods, BLOS fusion replacement.

---

## 7. Open Items

| Item | Status |
|------|--------|
| CV predictor in FCU hardware | Model only |
| Kalman/IMM predictor | Not implemented |
| Multi-vehicle HIL (P9-007) | Not built |
| Gossip radio / crypto | Architecture only |
| Field prototype | Per [PROTOTYPE_ROADMAP.md](../prototypes/PROTOTYPE_ROADMAP.md) |

---

## 8. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-24 | M1 concept SoT — consolidated from SYSTEM_SPEC, REQUIREMENTS, CORE_ENHANCEMENTS |

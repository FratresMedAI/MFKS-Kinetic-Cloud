# MKFS Current Tasks

**Last updated:** 2026-05-22  
**Project phase:** Phase 9 complete — network/C2 architecture, latency model, degraded comms scenarios

---

## Design Intent Revision (v0.2)

**[DESIGN_PHILOSOPHY.md](../docs/DESIGN_PHILOSOPHY.md)** is now the authoritative size/role doc:

- **2×1 / 3×1 ft tiles** — low profile, turret/hull/roof  
- **31 mm puck** projectiles (half-dollar class)  
- **Electronic per-tube fire** — scales to 2×100 tubes  
- **Last-ditch / don't-die** — APS analogue for swarms  

Prior "2×2 ft box / 25 tube" docs superseded where they conflict.

---

## Status Legend

| Status | Meaning |
|--------|---------|
| Done | Complete and reviewed |
| In Progress | Active work |
| Upcoming | Not yet started |

---

## Phase 0 — Foundation ✅

All tasks complete. See [REQUIREMENTS.md](../docs/REQUIREMENTS.md), [VEHICLE_INTEGRATION.md](../docs/VEHICLE_INTEGRATION.md).

---

## Phase 1 — Core Technology ✅

All tasks complete. See [CARRIER_PROJECTILE_ICD.md](../docs/CARRIER_PROJECTILE_ICD.md), [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md), [DEPLOYMENT_DOWN_SELECT.md](../docs/DEPLOYMENT_DOWN_SELECT.md).

---

## Phase 2 — Array Prototype ✅

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P2-001 | Multi-tube array module design | Done | [ARRAY_MODULE_SPEC.md](../prototypes/array/ARRAY_MODULE_SPEC.md) |
| P2-002 | FCU state machine spec | Done | [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md) |
| P2-003 | Quick-swap pod mechanism | Done | [POD_MECHANISM_SPEC.md](../prototypes/array/POD_MECHANISM_SPEC.md) |
| P2-004 | Tube tier sizing | Done | [ARRAY_MODULE_SPEC.md](../prototypes/array/ARRAY_MODULE_SPEC.md) §2 |
| P2-005 | Array prototype spec | Done | [ARRAY_MODULE_SPEC.md](../prototypes/array/ARRAY_MODULE_SPEC.md) |
| P2-006 | FCU software stub + tests | Done | [fcu.py](../src/fire_control/fcu.py), [test_fcu.py](../src/fire_control/test_fcu.py) |

---

## Phase 3 — Vehicle Integration ✅

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P3-001 | Stryker adapter kit | Done | [MKFS-ADP-STRYKER-A.md](../docs/adapters/MKFS-ADP-STRYKER-A.md) |
| P3-002 | Bradley adapter kit | Done | [MKFS-ADP-BRADLEY-A.md](../docs/adapters/MKFS-ADP-BRADLEY-A.md) |
| P3-003 | M113 adapter + structural | Done | [MKFS-ADP-M113-A.md](../docs/adapters/MKFS-ADP-M113-A.md) |
| P3-004 | LAV-25 adapter + stow | Done | [MKFS-ADP-LAV25-A.md](../docs/adapters/MKFS-ADP-LAV25-A.md) |
| P3-005 | MRAP adapter variants | Done | [MKFS-ADP-MRAP-A.md](../docs/adapters/MKFS-ADP-MRAP-A.md) |
| P3-006 | Dual-array fire plans | Done | [DUAL_ARRAY_FIRE_PLANS.md](../docs/DUAL_ARRAY_FIRE_PLANS.md) |
| P3-007 | Power/C4ISR ICD | Done | [ICD_POWER_C4ISR.md](../docs/ICD_POWER_C4ISR.md) |
| P3-008 | Sensor integration | Done | [ICD_SENSOR_INTEGRATION.md](../docs/ICD_SENSOR_INTEGRATION.md) |

---

## Phase 4 — Documentation & Next Steps

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P4-001 | Full system specification | Done | [SYSTEM_SPEC.md](../docs/SYSTEM_SPEC.md) |
| P4-002 | Prototype roadmap | Done | [PROTOTYPE_ROADMAP.md](../prototypes/PROTOTYPE_ROADMAP.md) |
| P4-003 | Risk register | Done | [RISK_REGISTER.md](../docs/RISK_REGISTER.md) |
| P4-004 | Manufacturing considerations | Done | [MANUFACTURING.md](../docs/MANUFACTURING.md) |
| P4-005 | Test and evaluation plan | Done | [TEST_EVAL_PLAN.md](../docs/TEST_EVAL_PLAN.md) |
| P4-006 | Physical prototype builds (M1–M10) | Upcoming | [PROTOTYPE_ROADMAP.md](../prototypes/PROTOTYPE_ROADMAP.md) |
| P4-007 | Range test execution (T1–T5) | Upcoming | [TEST_EVAL_PLAN.md](../docs/TEST_EVAL_PLAN.md) |

---

## Phase 5 — Idea Monkey Sprint ✅

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P5-001 | Salvo recalibration (136/208/289 tubes) | Done | [SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md) |
| P5-002 | Threat vignettes | Done | [CONOPS_VIGNETTES.md](../docs/CONOPS_VIGNETTES.md) |
| P5-003 | Magazine economics | Done | [MAGAZINE_ECONOMICS.md](../docs/MAGAZINE_ECONOMICS.md) |
| P5-004 | Fratricide & deconfliction | Done | [FRATRICIDE_DECONFLICTION.md](../docs/FRATRICIDE_DECONFLICTION.md) |
| P5-005 | Competitive positioning | Done | [COMPETITIVE_POSITIONING.md](../docs/COMPETITIVE_POSITIONING.md) |
| P5-006 | Puck cutaway storyboard | Done | [PUCK_CUTAWAY_STORYBOARD.md](../docs/visual/PUCK_CUTAWAY_STORYBOARD.md) |
| P5-007 | Reload-under-fire concept | Done | [RELOAD_UNDER_FIRE.md](../docs/visual/RELOAD_UNDER_FIRE.md) |
| P5-008 | One-pager + pitch deck | Done | [ONE_PAGER.md](../docs/outreach/ONE_PAGER.md), [PITCH_DECK.md](../docs/outreach/PITCH_DECK.md) |
| P5-009 | Swarm test concept (T5 desk) | Done | [SWARM_TEST_CONCEPT.md](../docs/SWARM_TEST_CONCEPT.md) |
| P5-010 | CONTRIBUTING + charter | Done | [CONTRIBUTING.md](../CONTRIBUTING.md), [COLLABORATION_CHARTER.md](../docs/COLLABORATION_CHARTER.md) |
| P5-011 | Questions for primes | Done | [QUESTIONS_FOR_PRIMES.md](../docs/outreach/QUESTIONS_FOR_PRIMES.md) |
| P5-012 | Maritime & fixed-site | Done | [MARITIME_FIXED_SITE.md](../docs/MARITIME_FIXED_SITE.md) |
| P5-013 | ITAR / export framing | Done | [ITAR_EXPORT_FRAMING.md](../docs/ITAR_EXPORT_FRAMING.md) |

---

## Phase 6 — Core MKFS Enhancements ✅

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P6-001 | LR munition spinoff | **Cancelled** | Not MKFS — removed |
| P6-002 | Terminal drone radar + EM sensor | Done | [ICD_DRONE_RADAR.md](../docs/ICD_DRONE_RADAR.md) |
| P6-003 | Core enhancements (FCU scale, turret ripple, dual-strip) | Done | [MKFS_CORE_ENHANCEMENTS.md](../docs/MKFS_CORE_ENHANCEMENTS.md) |
| P6-004 | FCU salvo scale update (136/289 tubes) | Done | [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md) |
| P6-005 | Rifling vs smooth-bore analysis | Done | [RIFLING_SPIN_ANALYSIS.md](../docs/RIFLING_SPIN_ANALYSIS.md) |
| P6-006 | Canonical puck forms (PUCK-A + PUCK-B) | Done | [PUCK_DESIGN_OPTIONS.md](../assets/PUCK_DESIGN_OPTIONS.md), D-011 |

---

## Phase 7 — Documentation Lock ✅

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P7-001 | Rifling/spin concept doc + deployment cross-link | Done | [RIFLING_SPIN_ANALYSIS.md](../docs/RIFLING_SPIN_ANALYSIS.md) |
| P7-002 | Puck A/B locked across ICD, storyboard, assets | Done | D-011 |

---

## Decisions — All Closed ✅

| ID | Outcome | Doc |
|----|---------|-----|
| D-001 | 30 mm | [DECISIONS.md](../docs/DECISIONS.md) |
| D-002 | Option D | [DECISIONS.md](../docs/DECISIONS.md) |
| D-003 | CAN 2.0B | [DECISIONS.md](../docs/DECISIONS.md) |
| D-004 | 25-tube standard tier *(superseded by D-012)* | [DECISIONS.md](../docs/DECISIONS.md) |
| D-012 | 136-tube 2×1 tile architecture | [DECISIONS.md](../docs/DECISIONS.md) |
| D-005 | Optional swarm sensor kit | [DECISIONS.md](../docs/DECISIONS.md) |
| D-011 | PUCK-A + PUCK-B canonical | [DECISIONS.md](../docs/DECISIONS.md) |
| D-013 | CAN-only kinetic commit path | [DECISIONS.md](../docs/DECISIONS.md) |

---

## Phase 8 — Four-Agent Sprint ✅

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P8-001 | Puck storyboard renders (6 frames + 6-up) | Done | [PUCK_CUTAWAY_STORYBOARD.md](../docs/visual/PUCK_CUTAWAY_STORYBOARD.md), [assets/](../assets/) |
| P8-002 | Spin dispersion model + scenario doc | Done | [SPIN_DISPERSION_SCENARIO.md](../research/ballistics/SPIN_DISPERSION_SCENARIO.md) |
| P8-003 | Titanium BB terminology pass | Done | [CARRIER_PROJECTILE_ICD.md](../docs/CARRIER_PROJECTILE_ICD.md), outreach |
| P8-004 | Supersede 25-tube refs (T&E, roadmap, D-004) | Done | [TEST_EVAL_PLAN.md](../docs/TEST_EVAL_PLAN.md), D-012 |
| P8-005 | FCU 136/867 tube tests + HIL stub | Done | [fcu.py](../src/fire_control/fcu.py), [HIL_SIM.md](../src/fire_control/HIL_SIM.md) |
| P8-006 | Outreach refresh + M1 build spec | Done | [ONE_PAGER.md](../docs/outreach/ONE_PAGER.md), [M1_SETBACK_PETAL_SPEC.md](../prototypes/mechanism/M1_SETBACK_PETAL_SPEC.md) |
| P8-007 | Optional reload + sensor renders | Done | [mkfs_reload_under_fire_stryker.png](../assets/mkfs_reload_under_fire_stryker.png), [mkfs_sensor_on_tile.png](../assets/mkfs_sensor_on_tile.png) |

---

## Phase 9 — Network & C2 Resilience ✅

| ID | Task | Status | Linked Doc |
|----|------|--------|------------|
| P9-001 | Network architecture doc | Done | [NETWORK_ARCHITECTURE.md](../docs/NETWORK_ARCHITECTURE.md) |
| P9-002 | Latency / packet-loss model | Done | [latency_resilience_model.py](../scripts/latency_resilience_model.py) |
| P9-003 | Degraded SWARM_TEST + FRATRICIDE scenarios | Done | T5-N01–N04, SI-009–011 |
| P9-004 | HIL delayed/lost tracks | Upcoming | [PHASE9.md](PHASE9.md) |
| P9-005 | CAN TRACK v2 addendum | Upcoming | [ICD_POWER_C4ISR.md](../docs/ICD_POWER_C4ISR.md) |
| P9-006 | Gossip ICD stub | Upcoming | [PHASE9.md](PHASE9.md) |

→ Full backlog: [PHASE9.md](PHASE9.md)

---

## Next Actions (Physical Prototype)

1. **M1** — Build setback petal mechanism prototype; run T1-001 — [M1_SETBACK_PETAL_SPEC.md](../prototypes/mechanism/M1_SETBACK_PETAL_SPEC.md)
2. **M3** — Single-tube proof; chamber pressure and primer validation
3. **M5** — Full **136-tube 2×1 pod** + pod swap demo (T3-002, T3-003)
4. **M7** — First vehicle mount (Stryker ICV)
5. **M2** — Outdoor range ballistics (T2 series)

---

## Quick Reference

| Constant | Value |
|----------|-------|
| Caliber | 30 mm |
| Payload | **~40 titanium BBs** / puck |
| `R_open` / `R_band` | 200 ft / 250–500 ft |
| Pattern (350 ft, 136-tube salvo) | ~24.5 ft; **~310 hits/m²** |
| Pattern (350 ft, 289-tube deck) | ~24.5 ft; **~659 hits/m²** |
| FCU bus | CAN 2.0B @ 500 kbps |

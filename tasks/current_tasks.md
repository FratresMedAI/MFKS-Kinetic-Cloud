# MKFS Current Tasks

**Last updated:** 2026-05-22  
**Project phase:** Phase 5 complete — idea monkey sprint; physical prototype next

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

---

## Decisions — All Closed ✅

| ID | Outcome | Doc |
|----|---------|-----|
| D-001 | 30 mm | [DECISIONS.md](../docs/DECISIONS.md) |
| D-002 | Option D | [DECISIONS.md](../docs/DECISIONS.md) |
| D-003 | CAN 2.0B | [DECISIONS.md](../docs/DECISIONS.md) |
| D-004 | 25-tube standard tier | [DECISIONS.md](../docs/DECISIONS.md) |
| D-005 | Optional swarm sensor kit | [DECISIONS.md](../docs/DECISIONS.md) |

---

## Next Actions (Physical Prototype)

1. **M1** — Build setback petal mechanism prototype; run T1-001
2. **M3** — Single-tube proof; chamber pressure and primer validation
3. **M5** — Full 25-tube module + pod swap demo (T3-002, T3-003)
4. **M7** — First vehicle mount (Stryker ICV)
5. **M2** — Outdoor range ballistics (T2 series)

---

## Quick Reference

| Constant | Value |
|----------|-------|
| Caliber | 30 mm |
| Flechette pack | 100 × Ti @ 1.3 g |
| `R_open` / `R_band` | 200 ft / 250–500 ft |
| Pattern (350 ft, 136-tube salvo) | ~24.5 ft; **~310 hits/m²** |
| Pattern (350 ft, 289-tube deck) | ~24.5 ft; **~659 hits/m²** |
| FCU bus | CAN 2.0B @ 500 kbps |

# MKFS Documentation Index

**Status:** Concept | Phase 9  
**Purpose:** Hub for all MKFS concept documentation — one sentence per doc, grouped by topic.  
**Related Documents:** [README.md](../README.md) | [M1_SPEC.md](M1_SPEC.md)

---

## Philosophy & Requirements

| Document | Purpose |
|----------|---------|
| [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) | Authoritative design intent — last-ditch terminal defense, form factors, tube scale |
| [M1_SPEC.md](M1_SPEC.md) | **M1 concept SoT** — configuration, performance, FCU/C2 summary |
| [REQUIREMENTS.md](REQUIREMENTS.md) | Full FR/NFR IDs, design constants, constraints |
| [SYSTEM_SPEC.md](SYSTEM_SPEC.md) | Consolidated subsystem spec index (Phase 0–3) |
| [MKFS_CORE_ENHANCEMENTS.md](MKFS_CORE_ENHANCEMENTS.md) | Terminal-only enhancements — tube scale, turret ripple, edge C2 |
| [DECISIONS.md](DECISIONS.md) | Architecture decision record (D-001+) |
| [RISK_REGISTER.md](RISK_REGISTER.md) | Program risks and mitigations |

---

## Architecture & C2

| Document | Purpose |
|----------|---------|
| [architecture/SYSTEM_ARCHITECTURE.md](architecture/SYSTEM_ARCHITECTURE.md) | System block diagram — FCU, arrays, sensors, CAN |
| [NETWORK_ARCHITECTURE.md](NETWORK_ARCHITECTURE.md) | Tier 1/2/3 C2, latency model, degradation ladder |
| [FCU_EDGE_PREDICTOR_ONEPAGER.md](FCU_EDGE_PREDICTOR_ONEPAGER.md) | Why local predictor + CAN fire path fix stale-track miss |
| [DUAL_ARRAY_FIRE_PLANS.md](DUAL_ARRAY_FIRE_PLANS.md) | Per-platform dual-array fire allocation |
| [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md) | Friendly/APS deconfliction rules (SI-001+) |
| [SWARM_TEST_CONCEPT.md](SWARM_TEST_CONCEPT.md) | T5 swarm surrogate test concept + network stress (T5-N01–N04) |
| [TEST_EVAL_PLAN.md](TEST_EVAL_PLAN.md) | Verification test IDs (T1–T5) |

**Models:** [latency_resilience_model.py](../scripts/latency_resilience_model.py) · [ballistics_model.py](../research/ballistics/ballistics_model.py)

---

## Integration & Sensors

| Document | Purpose |
|----------|---------|
| [ICD_SENSOR_INTEGRATION.md](ICD_SENSOR_INTEGRATION.md) | Sensor fusion priority, track handoff to FCU |
| [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md) | Power, CAN, optional C4ISR — MKFS-IF-004 |
| [ICD_DRONE_RADAR.md](ICD_DRONE_RADAR.md) | Co-mounted terminal EM/radar cueing |
| [VEHICLE_INTEGRATION.md](VEHICLE_INTEGRATION.md) | Platform integration matrix |
| [adapters/README.md](adapters/README.md) | Adapter kit drawing set index |
| [adapters/MKFS-ADP-STRYKER-A.md](adapters/MKFS-ADP-STRYKER-A.md) | Stryker adapter kit |
| [adapters/MKFS-ADP-BRADLEY-A.md](adapters/MKFS-ADP-BRADLEY-A.md) | Bradley adapter kit |
| [adapters/MKFS-ADP-M113-A.md](adapters/MKFS-ADP-M113-A.md) | M113 adapter kit |
| [adapters/MKFS-ADP-LAV25-A.md](adapters/MKFS-ADP-LAV25-A.md) | LAV-25 adapter kit |
| [adapters/MKFS-ADP-MRAP-A.md](adapters/MKFS-ADP-MRAP-A.md) | MRAP adapter kit |

**Projectile / array ICDs:** [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) · [PUCK_RELEASE.md](PUCK_RELEASE.md) · [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) · [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md) · [RIFLING_SPIN_ANALYSIS.md](RIFLING_SPIN_ANALYSIS.md)

**FCU software:** [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md) · [HIL_SIM.md](../src/fire_control/HIL_SIM.md)

---

## CONOPS & Vignettes

| Document | Purpose |
|----------|---------|
| [CONOPS_VIGNETTES.md](CONOPS_VIGNETTES.md) | Five operational last-ditch employment narratives |
| [MARITIME_FIXED_SITE.md](MARITIME_FIXED_SITE.md) | USV and fixed-site mounting concepts |
| [COMPETITIVE_POSITIONING.md](COMPETITIVE_POSITIONING.md) | vs missiles, shotguns, APS — cost and role |

---

## Economics & Manufacturing

| Document | Purpose |
|----------|---------|
| [MAGAZINE_ECONOMICS.md](MAGAZINE_ECONOMICS.md) | ROM cost per salvo, magazine depth tradeoffs |
| [MANUFACTURING.md](MANUFACTURING.md) | Production and scale considerations |
| [SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md) | Tube-count recalibration — hits/m² at 350 ft |
| [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md) | Ballistics model output summary |

---

## Visuals & Storyboards

| Document | Purpose |
|----------|---------|
| [visual/PUCK_STORYBOARD.md](visual/PUCK_STORYBOARD.md) | Five-frame puck release + image generation prompts |
| [visual/PUCK_CUTAWAY_STORYBOARD.md](visual/PUCK_CUTAWAY_STORYBOARD.md) | Six-frame cutaway with embedded renders |
| [visual/RELOAD_UNDER_FIRE.md](visual/RELOAD_UNDER_FIRE.md) | Pod swap under fire concept |

**Assets:** [assets/](../assets/) — mounting concepts, turret, puck comparison, storyboard PNGs

---

## Outreach & ITAR

| Document | Purpose |
|----------|---------|
| [outreach/ONE_PAGER.md](outreach/ONE_PAGER.md) | Prime-facing one-page summary |
| [outreach/PITCH_DECK.md](outreach/PITCH_DECK.md) | Pitch deck outline |
| [outreach/QUESTIONS_FOR_PRIMES.md](outreach/QUESTIONS_FOR_PRIMES.md) | Collaboration discovery questions |
| [ITAR_EXPORT_FRAMING.md](ITAR_EXPORT_FRAMING.md) | Export control framing for open release |
| [COLLABORATION_CHARTER.md](COLLABORATION_CHARTER.md) | Partnership and contribution terms |

---

## Tasks & Backlog

| Document | Purpose |
|----------|---------|
| [tasks/PHASE9.md](../tasks/PHASE9.md) | Phase 9 network/C2 backlog |
| [tasks/current_tasks.md](../tasks/current_tasks.md) | Active task tracker |

---

## Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-24 | Initial documentation hub |

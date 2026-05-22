# MKFS System Specification

**Document ID:** MKFS-DOC-SPEC-001  
**Version:** 0.1  
**Status:** Consolidated specification (Phase 0–3)  
**Related:** All docs in `docs/`, `research/`, `prototypes/`

---

## 1. System Description

**MKFS** is a **last-ditch terminal defense** system — kinetic, non-explosive, APS-analogue protection against close-in drone swarms. Low-profile **2×1 / 3×1 tiles** with **half-dollar pucks** mount on turret cheeks, hull sides, and roofs. **Electronic per-tube fire** scales to 200+ tubes.

**Authoritative intent:** [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md)

---

## 2. System Configuration

| Element | Baseline |
|---------|----------|
| Cartridge | `MKFS-CART-PUCK` — **31 mm × 28 mm** half-dollar class |
| Flechette pack | ~35 × Ti per puck |
| Launcher | **2×1 ft tile** (18 tubes); scales to **3×1**, multi-tile, **2×100** |
| Profile | **≤ 150 mm** — lays on armor |
| Fire control | **Individual tube addressing** — CAN bus |
| Role | **Last-ditch / don't die** when swarm is inside ~500 yd |

---

## 3. Performance Requirements

| Parameter | Requirement | Verification |
|-----------|-------------|--------------|
| `R_open` | ~200 ft (61 m) | T2-002 |
| `R_band` | 250–500 ft peak effect | T2-002, ballistics model |
| `R_max` | ~500 yd | T2-002 |
| `V_0` | 900 m/s ± 45 m/s | T2-001 |
| Pattern at 350 ft | 15–25 ft diameter | T2-002 |
| Swarm density | ≥ 2 hits/m² (25-tube salvo) | T2-003 |
| Salvo | 25 tubes in ≤ 1.2 s | T3-002 |
| Pod swap | < 5 min | T3-003 |
| Function rate | ≥ 99.5% | T1-004 |

*See [TEST_EVAL_PLAN.md](TEST_EVAL_PLAN.md) for test IDs.*

---

## 4. Subsystem Specifications

### 4.1 Projectile

| Doc | Content |
|-----|---------|
| [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) | Full ICD — MKFS-IF-001 |
| [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) | Option D mechanism |
| [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md) | Down-select record |

### 4.2 Array Module

| Doc | Content |
|-----|---------|
| [ARRAY_MODULE_SPEC.md](../prototypes/array/ARRAY_MODULE_SPEC.md) | Module tiers, tubes, initiation |
| [POD_MECHANISM_SPEC.md](../prototypes/array/POD_MECHANISM_SPEC.md) | Quick-swap pod |

### 4.3 Fire Control

| Doc | Content |
|-----|---------|
| [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md) | States, salvo profiles |
| [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md) | Power, CAN, C4ISR — MKFS-IF-004 |
| [DUAL_ARRAY_FIRE_PLANS.md](DUAL_ARRAY_FIRE_PLANS.md) | Per-platform fire allocation |

### 4.4 Vehicle Integration

| Doc | Content |
|-----|---------|
| [VEHICLE_INTEGRATION.md](VEHICLE_INTEGRATION.md) | Integration matrix |
| [adapters/README.md](adapters/README.md) | Adapter kit drawing sets |
| [ICD_SENSOR_INTEGRATION.md](ICD_SENSOR_INTEGRATION.md) | Sensor baseline + optional kit |

---

## 5. Interface Control Summary

| ID | Interface | Specification Doc |
|----|-----------|-------------------|
| MKFS-IF-001 | Projectile / cartridge | [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) |
| MKFS-IF-002 | Array module face | [ARRAY_MODULE_SPEC.md](../prototypes/array/ARRAY_MODULE_SPEC.md) |
| MKFS-IF-003 | Vehicle adapter plate | [REQUIREMENTS.md](REQUIREMENTS.md) §7, adapter kits |
| MKFS-IF-004 | Power / data (CAN) | [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md) |

---

## 6. Modularity

One projectile family + scalable array tiers + five adapter kits:

| Platform | Kit | Array Tier |
|----------|-----|------------|
| Stryker ICV/CV | `MKFS-ADP-STRYKER-A` | Standard × 2 |
| Stryker MGS | `MKFS-ADP-STRYKER-A` | Compact × 2 |
| M2 Bradley | `MKFS-ADP-BRADLEY-A` | Standard × 2 |
| M113 | `MKFS-ADP-M113-A` | Compact × 2 |
| LAV-25 | `MKFS-ADP-LAV25-A` | Compact × 2 |
| MRAP MaxxPro | `MKFS-ADP-MRAP-A/D` | Dense × 2 |
| MRAP RG-31 | `MKFS-ADP-MRAP-A/S` | Standard × 2 |

---

## 7. Design Constraints

- C-001 through C-005 per [REQUIREMENTS.md](REQUIREMENTS.md) §6
- Kinetic only — no explosives, no in-round electronics
- Terminal defense — not a medium-range AD replacement

---

## 8. Analysis and Trade Studies

| Study | Location |
|-------|----------|
| Ballistics | [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md) |
| Caliber | [CALIBER_TRADE_STUDY.md](../research/CALIBER_TRADE_STUDY.md) |
| Flechette | [FLECHETTE_TRADE_STUDY.md](../research/ballistics/FLECHETTE_TRADE_STUDY.md) |
| Decisions | [DECISIONS.md](DECISIONS.md) |
| Risks | [RISK_REGISTER.md](RISK_REGISTER.md) |

---

## 9. Prototype and Production

| Doc | Content |
|-----|---------|
| [PROTOTYPE_ROADMAP.md](../prototypes/PROTOTYPE_ROADMAP.md) | Build schedule |
| [MANUFACTURING.md](MANUFACTURING.md) | Production considerations |

---

## 10. Software

| Component | Location |
|-----------|----------|
| Ballistics model | `research/ballistics/ballistics_model.py` |
| FCU stub | `src/fire_control/fcu.py` |
| FCU tests | `src/fire_control/test_fcu.py` |

---

## 11. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial consolidated system spec |

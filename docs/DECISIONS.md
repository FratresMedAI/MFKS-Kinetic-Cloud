# MKFS Program Decisions Log

**Document ID:** MKFS-DOC-DEC-001  
**Version:** 0.1

---

| ID | Decision | Options | Outcome | Date | Reference |
|----|----------|---------|---------|------|-----------|
| D-001 | Cartridge caliber | 25 / 30 / 40 mm | **30 mm** | 2026-05-22 | [CALIBER_TRADE_STUDY.md](../research/CALIBER_TRADE_STUDY.md) |
| D-002 | Deployment mechanism | A / B / C / D / hybrid | **Option D** (setback petal) | 2026-05-22 | [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md) |
| D-003 | FCU data bus | RS-485 / CAN | **CAN 2.0B @ 500 kbps** | 2026-05-22 | [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md) |
| D-004 | Standard tier (Bradley/Stryker) | 25 / 36 tubes | **25 tubes (standard tier)** | 2026-05-22 | See rationale below |
| D-005 | Swarm sensor in baseline | Required / optional | **Optional kit**; vehicle sensors baseline | 2026-05-22 | [ICD_SENSOR_INTEGRATION.md](ICD_SENSOR_INTEGRATION.md) |
| D-006 | Module size | **2×2 ft** (610×610 mm) — sole standard | 2026-05-22 | [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) |
| D-007 | Projectile form | 165 mm cartridge / **puck** | **31 mm × 28 mm puck** | 2026-05-22 | [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) |
| D-008 | Mission framing | Generic terminal AD / **last-ditch APS analogue** | **Last-ditch don't-die layer** | 2026-05-22 | [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) |

---

## D-004 Rationale — Standard Tier (25 Tubes)

| Factor | 25-tube | 36-tube |
|--------|---------|---------|
| Dual-array mass (Stryker) | ~100 kg | ~130 kg |
| Roof CG impact | Within limit | Marginal on MGS/LAV |
| Salvo flechettes | 2,500 | 3,600 |
| Modeled density at 350 ft | 57 hits/m² | ~82 hits/m² *(est.)* |
| Power peak | 300 W | 380 W |

**Conclusion:** 25-tube standard tier meets density target (≥ 2 hits/m²) with margin; preserves CG and power budgets on constrained platforms. Dense tier (36) retained for MRAP MaxxPro where roof capacity allows.

---

## D-005 Rationale — Optional Swarm Sensor

Baseline MKFS relies on existing vehicle EO/IR or manual cue — minimizing integration cost and schedule. Optional `MKFS-SENS-SWARM-OPT` kit adds autonomous cueing for convoy/MRAP missions without organic air defense. Not required for IOC.

---

## Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | D-004, D-005 closed |

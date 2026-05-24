# MKFS Program Decisions Log

**Status:** Concept | Phase 9
**Purpose:** Architecture decision record.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-DOC-DEC-001  
**Version:** 0.1

---

| ID | Decision | Options | Outcome | Date | Reference |
|----|----------|---------|---------|------|-----------|
| D-001 | Cartridge caliber | 25 / 30 / 40 mm | **30 mm** | 2026-05-22 | [CALIBER_TRADE_STUDY.md](../research/CALIBER_TRADE_STUDY.md) |
| D-002 | Deployment mechanism | A / B / C / D / hybrid | **Option D** (setback petal) | 2026-05-22 | [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md) |
| D-003 | FCU data bus | RS-485 / CAN | **CAN 2.0B @ 500 kbps** | 2026-05-22 | [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md) |
| D-004 | Standard tier (Bradley/Stryker) | 25 / 36 tubes | **25 tubes** — **superseded by D-012** | 2026-05-22 | See rationale below |
| D-005 | Swarm sensor in baseline | Required / optional | **Optional kit**; vehicle sensors baseline | 2026-05-22 | [ICD_SENSOR_INTEGRATION.md](ICD_SENSOR_INTEGRATION.md) |
| D-006 | Module size | **2×2 ft** (610×610 mm) — sole standard | 2026-05-22 | [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) |
| D-007 | Projectile form | 165 mm cartridge / **puck** | **31 mm × 28 mm puck** | 2026-05-22 | [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) |
| D-008 | Mission framing | Generic terminal AD / **last-ditch APS analogue** | **Last-ditch don't-die layer** | 2026-05-22 | [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) |
| D-010 | Terminal drone sensor | Swarm kit only / **EM+radar on tile** | **MKFS-SENS-EM-RADAR** optional; 50–800 yd | 2026-05-22 | [ICD_DRONE_RADAR.md](ICD_DRONE_RADAR.md) |
| D-011 | Canonical puck forms | A / B / C / D / mix | **PUCK-A + PUCK-B** | 2026-05-22 | [PUCK_DESIGN_OPTIONS.md](../assets/PUCK_DESIGN_OPTIONS.md) |
| D-012 | Tile tube architecture | 25-tube module / **136-tube 2×1 strip** | **136-tube 2×1 appliqué strip** | 2026-05-22 | Supersedes D-004 for salvo scale |
| D-013 | Kinetic commit path | TCP/IP allowed / **CAN-only fire path** | **Fire path SHALL NOT traverse TCP/IP** | 2026-05-22 | [NETWORK_ARCHITECTURE.md](NETWORK_ARCHITECTURE.md) |

---

## D-011 Rationale — Canonical Puck Forms

| Form | Name | Role |
|------|------|------|
| **PUCK-A** | Standard Drum | Tube fill, tile packing, general ICD diagrams |
| **PUCK-B** | Hollow-Point Nose | Peel doctrine, cutaways, storyboards |

Options C (peel action shot) and D (setback cap reference) remain available for one-off art but are **not** canonical. All new docs and renders use **A + B**.

---

## D-004 Rationale — Standard Tier (25 Tubes) *(Superseded by D-012)*

> **Superseded:** Tile architecture now standardizes on **136-tube 2×1 strips** and **289-tube turret decks**. Legacy 25-tube module references remain in ballistics model as `legacy_25` only.

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

## D-013 Rationale — CAN-Only Kinetic Commit Path (Tier 1)

| Path | Allowed for FIRE_CMD? | Rationale |
|------|----------------------|-----------|
| Vehicle CAN (500 kbps) | **Yes** | Tier 1 commit; deterministic ≤ 5 ms |
| Vehicle Ethernet / TCP/IP | **No** | Packet loss, latency spikes, central dependency |
| C4ISR / 1553 | **Intent only** (Tier 3) | ROE, geofence — seconds-scale OK |

Model baseline ([`latency_resilience_output.json`](../scripts/latency_resilience_output.json) `baseline_reference`): 250 ms @ 60 mph → **22.0 ft** miss; `pattern_overlap_at_baseline` = **0.0**; `pattern_overlap_with_predictor` = **0.894**. Tracks and fire commands stay on the **FCU edge node** with local predictor. See [NETWORK_ARCHITECTURE.md](NETWORK_ARCHITECTURE.md).

---

## Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | D-004, D-005 closed |
| 0.2 | 2026-05-22 | D-011 — PUCK-A + PUCK-B canonical |
| 0.3 | 2026-05-22 | D-004 superseded; D-012 — 136-tube tile architecture |
| 0.4 | 2026-05-22 | D-013 — CAN-only kinetic commit path (edge-first C2) |
| 0.5 | 2026-05-22 | Hardening — D-013 quant traceability to latency model JSON |

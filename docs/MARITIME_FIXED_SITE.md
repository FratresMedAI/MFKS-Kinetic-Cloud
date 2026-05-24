# MKFS Maritime & Fixed-Site Concepts

**Status:** Concept | Phase 9
**Purpose:** USV and fixed-site mounting concepts.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-DOC-DOM-001  
**Version:** 0.1 (Phase 5)  
**Related:** [VEHICLE_INTEGRATION.md](VEHICLE_INTEGRATION.md) | [MOUNTING_CONCEPT.md](../assets/MOUNTING_CONCEPT.md) | [ARRAY_MODULE_SPEC.md](../prototypes/array/ARRAY_MODULE_SPEC.md)

---

## 1. Purpose

Extend appliqué MKFS packaging to **maritime** and **fixed-site** domains without new puck design or caliber changes. Same 2×1 / 3×1 ft strips, same FCU architecture.

---

## 2. USV / Ship Self-Defense

### Concept

Low-profile **2×1 ft strips** on conning tower or superstructure faces — as shown in [mkfs_mounting_concept_stryker_jltv_usv.png](../assets/mkfs_mounting_concept_stryker_jltv_usv.png).

| Parameter | Consideration |
|-----------|---------------|
| Mount faces | Port/starboard tower — 180° per face, dual overlap astern |
| Tube count | 2× 136 = 272 per tower level |
| Cueing | Tower EO; manual or exported track |
| Sea state | Rubber isolators in adapter; firing limited Sea State ≤ 4 *(concept)* |
| Corrosion | Salt-spray coating on tube bundle; stainless cams on pod latch |
| Power | 28 VDC ship bus or local battery pod |

### Employment

Terminal defense vs **low flyers and FPV** at 250–500 yd — same band as land. Not anti-missile. Complements Phalanx inner bubble on manned vessels.

### Reload

Shore-side or alongside replenishment — swap pods from palletized stowage. Unmanned USV may carry **1 spare pod per face** in deck locker.

---

## 3. FOB / Perimeter Fixed-Site

### Concept

Static **2×1 or 3×1 ft tile grids** on perimeter towers, gate sponsons, or CLP walls — powered from base grid, cued from existing base sensors.

| Parameter | Consideration |
|-----------|---------------|
| Layout | 4× 3×1 strips per corner tower = 832 tubes per tower |
| Cueing | Base radar *(if exportable)* + EO — FCU accepts bearing-only |
| Coverage | Overlapping sectors — 360° with 4 towers |
| Magazine | Multiple pod stacks in tower base — swap without climbing *(ground-level access)* |
| Fratricide | Strict SI-006 — base personnel corridors mapped as permanent inhibit arcs |

### Employment

Last-ditch vs **swarm saturation** of fixed site — not replacement for counter-rocket or base AD. Kinetic-only advantage: no explosive storage restrictions beyond propellant magazine.

### Power / C4

Permanent 28 VDC feed; FCU tied to base C2 via Ethernet — see [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md).

---

## 4. Shared Design Elements

Both spinoffs reuse:

- `MKFS-CART-PUCK` cartridge
- Quick-swap pod ([POD_MECHANISM_SPEC.md](../prototypes/array/POD_MECHANISM_SPEC.md))
- CAN 2.0B FCU bus
- Appliqué adapter plate (MKFS-IF-003)

**New work for prime collab:** corrosion spec, tower structural analysis, base sensor ICD.

---

## 5. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial maritime and fixed-site spinoffs |

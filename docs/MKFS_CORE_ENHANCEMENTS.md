# MKFS Core Enhancements

**Document ID:** MKFS-DOC-CORE-001  
**Version:** 0.1  
**Status:** Authoritative direction — **terminal MKFS only**  
**Related:** [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) | [SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md) | [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md)

---

## 1. North Star

MKFS is **last-ditch terminal defense** — flat tube batteries and pan-tilt turret dumps when the swarm is inside **~500 yd**. We improve **that**, not bolt pucks into Javelins or chain guns.

---

## 2. Enhancement A — FCU at Real Tube Scale

Legacy docs capped salvos at **25 tubes**. Design intent is **136 / 208 / 289+**.

| Package | Tubes | LAST_DITCH_FULL duration *(2 ms inter-tube)* |
|---------|-------|-----------------------------------------------|
| 2×1 strip | 136 | **~0.27 s** |
| 3×1 strip | 208 | **~0.42 s** |
| Turret deck | 289 | **~0.58 s** |
| Turret 3-deck | 867 | **~1.7 s** |

**Improvement:** FCU salvo engine addresses **every tube on the tile** — no artificial 25-tube cap. Profiles unchanged; scale updated.

→ See updated [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md) §5

---

## 3. Enhancement B — Turret Staggered Deck Ripple

Pan-tilt head stacks **3–4 decks** of 289 tubes. Firing all decks in one flat ripple wastes pattern overlap.

**Improvement:** `TURRET_RIPPLE` profile — deck 1 → 50 ms → deck 2 → 50 ms → deck 3. Slightly widens terminal cloud footprint without new hardware.

| Deck | Delay from primer | Effect |
|------|-------------------|--------|
| 1 | 0 ms | Lead cloud |
| 2 | +50 ms | Fills gaps |
| 3 | +100 ms | Saturation |

Still kinetic-only; still inside 200–500 yd band.

---

## 4. Enhancement C — Dual-Strip Phase Offset

Stryker/JLTV with **two 2×1 strips** can fire with **20 ms offset** between modules — forward strip first, aft strip +20 ms. Overlapping cones at 350 ft raise effective density without extra tubes.

From [SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md): single strip **310 hits/m²**; phased dual-strip overlap **~400+ hits/m²** *(concept estimate)*.

---

## 5. Enhancement D — Sensor on the Tile

Drone radar/EM co-mounted on MKFS — not a separate program. Sensor sees swarm at 600 yd; FCU fires strips at 350 yd. One kit, one bus, one kill chain.

→ [ICD_DRONE_RADAR.md](ICD_DRONE_RADAR.md)

---

## 6. Enhancement E — Faster Pod Swap

Target pod swap **< 3 min** (down from 5) with rail self-align + RFID auto-count — crew under cover while second tile holds sector.

→ [RELOAD_UNDER_FIRE.md](visual/RELOAD_UNDER_FIRE.md)

---

## 7. Enhancement F — Puck Consistency

Stay on **31 mm × 28 mm hollow-point puck** everywhere:

- Tile strip  
- Turret magazine  
- Same cartridge, same logistics, same ballistics model  

No caliber drift. No merged munitions.

---

## 8. What We Rejected

| Rejected | Why |
|----------|-----|
| MKFS-LR / 30 mm shell puck | Not our lane — terminal strips do volume better |
| AMR / Gustaf puck rounds | Different crew, different fight |
| Javelin-form LR pod | Confuses program; not MKFS |
| 1,500 yd sensor cueing LR | Sensor now cues **terminal tiles only** |

---

## 9. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Core terminal enhancements; LR spinoff rejected |

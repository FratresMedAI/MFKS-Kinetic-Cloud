# MKFS Array Module — Tile Architecture

**Document ID:** MKFS-PROTO-ARRAY-001  
**Version:** 0.5  
**Interface:** MKFS-IF-002  

---

## Vehicle Appliqué — 2×1 ft / 3×1 ft

Flat strips on armor. **Not** the pan-tilt turret (that uses **2×2 ft** — see [OBSERVATORY_TURRET.md](../../assets/OBSERVATORY_TURRET.md)).

| Tile | Face **(ft)** | Face **(mm)** | Tubes |
|------|---------------|---------------|-------|
| `MKFS-TILE-2x1` | **2 × 1** | 610 × 305 | ~136 |
| `MKFS-TILE-3x1` | **3 × 1** | 915 × 305 | ~208 |

Pitch: 35 mm · puck: 31 mm · electronic per-tube fire.

---

## Pan-Tilt Turret Only — 2×2 ft

**Moving-head CIWS** — internal magazine face:

| Module | Face | Tubes/deck | Decks |
|--------|------|------------|-------|
| `MKFS-TUR-MAG-2x2` | **2 × 2 ft** (610×610 mm) | ~289 | 3–4 stacked |

Form: [reference_moving_head_stage_light.png](../../assets/reference_moving_head_stage_light.png)

---

## Revision

| Ver | Change |
|-----|--------|
| 0.5 | Vehicle 2×1/3×1 vs turret **2×2 ft** split clarified |

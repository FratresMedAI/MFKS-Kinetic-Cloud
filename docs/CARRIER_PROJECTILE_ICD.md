# MKFS Carrier Projectile — Interface Control Document

**Status:** Concept | Phase 9
**Purpose:** Projectile/cartridge interface — MKFS-IF-001.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-ICD-001  
**Version:** 0.5  
**Interface:** MKFS-IF-001  
**Related:** [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) | [PUCK_RELEASE.md](PUCK_RELEASE.md) | [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) | [PUCK_DESIGN_OPTIONS.md](../assets/PUCK_DESIGN_OPTIONS.md)

---

## 1. Purpose

Define the **hollow-point puck** (`MKFS-CART-PUCK`) — short 31 mm carrier whose **skirt peels open** like a hollow-point bullet. **Speed + air drag + geometry** spread the **titanium BB cloud**. **No explosives. No electronic fuze.**

**Design fusion:** CIWS volume + 30 mm class + puck form + 00 buck payload + hollow-point opening → one kinetic strip.

### Canonical form factors (D-011)

| ID | Name | Use |
|----|------|-----|
| **PUCK-A** | Standard Drum | General cartridge / tube-fill diagrams; flat top, scored skirt band |
| **PUCK-B** | Hollow-Point Nose | Peel doctrine, cutaways, storyboards; domed nose + titanium BB payload visible |

See [PUCK_DESIGN_OPTIONS.md](../assets/PUCK_DESIGN_OPTIONS.md) and [mkfs_puck_design_comparison_4up.png](../assets/mkfs_puck_design_comparison_4up.png).

---

## 2. Size — What “Half Dollar” Actually Means

**Short answer:** Same **width** as a half dollar and as a 30 mm grenade (~31 mm). Much **shorter** — about **¼ the length** of a typical 30 mm grenade round, **not** half the diameter.

### Comparison Table

| | US half dollar (coin) | Typical 30 mm grenade *(30×113 mm)* | **MKFS puck** |
|--|----------------------|--------------------------------------|---------------|
| **Diameter** | 30.6 mm | 30 mm | **31 mm** |
| **Length / height** | 2.1 mm *(flat coin)* | **113 mm** | **28 mm** |
| **Mass** | ~11 g | **350–400 g** | **~63 g** |
| **Shape** | Coin | Long cartridge | **Short puck / drum** |

### Relative to a 30 mm Grenade

| Dimension | MKFS puck vs 30×113 mm grenade |
|-----------|--------------------------------|
| Diameter | **~Same** (100% — both ~30–31 mm) |
| Length | **~¼** (28 mm vs 113 mm) |
| Volume | **~¼** |
| Mass | **~⅙** (~63 g vs ~380 g) |

So when you say **“half dollar size”**:

- **Plan view (looking at the tube face):** yes — **~1.2 inch / 31 mm circle**, same as half dollar, same caliber as 30 mm ammo.  
- **Overall round bulk:** **not** half a 30 mm grenade — it’s about **one-third to one-quarter the length** and **one-quarter the total size** because grenades are **long** and this is a **puck**.

```
  Side-by-side (not to scale on length axis):

  30×113 mm grenade:  |████████████████████|  113 mm long
  MKFS puck:          |███|                  28 mm long
  Half dollar coin:   |▪|                    2 mm thick

  Diameter (all ~same):  ~31 mm
```

**Design intent:** grenade **caliber** (30 mm class) but **puck depth** so you can pack **130+ tubes** in a 2×1 ft panel — not 130 full-length grenades.

---

## 3. Cartridge Summary

| Parameter | Value |
|-----------|-------|
| Designation | `MKFS-CART-PUCK` |
| Diameter | 31.0 mm ± 0.1 mm |
| Length (OAL) | 28 mm ± 0.3 mm |
| Mass (loaded) | 55–75 g |
| Muzzle velocity (nominal) | 850–950 m/s *(short barrel / high impulse)* |
| Primer | Electric, launcher-only |
| Energetics | Propellant only — **no explosive payload** |
| Deployment | **Option HP** — hollow-point skirt peel + drag dispersal ([PUCK_RELEASE.md](PUCK_RELEASE.md)) |

---

## 4. Hollow-Point Opening *(Mechanism)*

```
  Before peel          After peel (@ R_open)
       ┌───┐                 ┌───┐
       │   │  stable flight  │ ● │  nose continues
       │   │  ───────────►   │╱ ╲│  skirt mushrooms aft
       └───┘                 │███│  Ti BBs shear out
                             └───┘
```

| Feature | Spec |
|---------|------|
| Nose | Flat hollow-point ogive — scored to peel, not penetrate |
| Skirt | 4–6 petals; setback-preloaded; releases at `R_open` |
| Dispersal | **Drag on open skirt** + forward body separation → radial buckshot cloud |
| Band index | 3-position preload — sets peel timing / `R_open` |

**Same idea as a hollow point:** shaped to open; **ballistics finish the kill.**

---

## 4. Why Puck + Many Tubes

One 165 mm “rifle” round carries many sub-projectiles but **fills a huge tube**. A **puck** carries fewer **titanium BBs** per round but:

- Fits **35 mm pitch** → **9 tubes per foot** of tile  
- **200 pucks** from a 2×100 layout >> one box of 25 big rounds  
- **Electronic select** fires exactly the sector you need  

**Last-ditch doctrine:** saturation from **count**, not single-round payload mass.

| | Old concept (superseded) | Puck concept |
|--|--------------------------|--------------|
| Form | 165 mm × 30 mm | **28 mm × 31 mm** |
| Flechettes / round | ~100 | **~40 Ti BBs** |
| Tubes on 2×1 ft tile | ~5 | **~136** |
| Ti BBs per 2×1 salvo | ~500 | **~5,400+** |

---

## 5. Puck Internals

| Subassembly | Mass (approx.) | Function |
|-------------|----------------|----------|
| Case / base | 18 g | Chamber seal, primer pocket |
| Propellant | 8 g | Launch |
| Carrier cap | 12 g | Setback petal (Option D) |
| Flechette bundle *(legacy term)* | 25 g | **Ti BB bundle — ~40 × titanium BBs** *(00 buck class spread)* |
| **Total** | **~63 g** | |

Sub-projectile: Ti-6Al-4V **BB sphere**, 00-buck class. *(Legacy ICD term “flechette” retained in ballistics model constants only.)*

---

## 6. Tube / Chamber

| Parameter | Value |
|-----------|-------|
| Tube bore | 33 mm |
| Chamber depth | 32 mm |
| Primer | Electric, 6 mm pocket |
| Band index | 3-position ring on base *(short / standard / long)* |

---

## 7. Performance Targets

| Parameter | Target |
|-----------|--------|
| `R_open` (standard band) | ~200 ft |
| Pattern per puck at 350 ft | Contributes to tile-level cloud |
| Function rate | ≥ 99.5% |
| Drop-safe | No release < 500 G |

*Tile-level ballistics: [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md) — recalibration for puck in progress.*

---

## 8. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | 165 mm rifle round (superseded) |
| 0.2 | 2026-05-22 | Half-dollar puck; MKFS-CART-PUCK |
| 0.3 | 2026-05-22 | Size comparison vs 30×113 mm grenade |
| 0.4 | 2026-05-22 | Hollow-point skirt release; CIWS+buckshot fusion |
| 0.5 | 2026-05-22 | D-011 — PUCK-A / PUCK-B canonical form factors |
| 0.6 | 2026-05-22 | Phase 8 — titanium BB terminology; Ti BB bundle §5 |

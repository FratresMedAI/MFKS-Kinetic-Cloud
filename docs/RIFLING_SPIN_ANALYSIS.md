# MKFS Rifling & Spin Analysis

**Document ID:** MKFS-DOC-RIFL-001  
**Version:** 0.1  
**Related:** [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) | [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md) | [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) | [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md) | [ballistics_model.py](../research/ballistics/ballistics_model.py)

---

## 1. Purpose

Answer whether MKFS terminal-defense tubes should be **rifled or smooth bore**, and whether **spin** can improve pattern spread, accuracy, or muzzle velocity for the **31 mm puck** strip without conflicting with **Option D setback skirt peel** (D-002) or **PUCK-B hollow-point** geometry (D-011).

**Scope:** Terminal MKFS only (~200 ft `R_open`, ~500 yd `R_max`). Not long-range precision munitions.

---

## 2. Baseline Geometry

| Parameter | Value | Source |
|-----------|-------|--------|
| Tube bore | 33 mm | [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) §6 |
| Puck diameter | 31 mm ± 0.1 mm | ICD §3 |
| Puck OAL | 28 mm | ICD §3 |
| Chamber depth | 32 mm | ICD §6 |
| Nominal `V_0` | 900 m/s | [ballistics_model.py](../research/ballistics/ballistics_model.py) |
| Deployment | Option D — setback petal @ `t_release` = 0.078 s | D-002 |

The puck is a **short disc**, not a spin-stabilized rifle bullet. Pre-peel flight lasts ~80 ms to `R_open`; post-peel the carrier body tumbles and flechettes disperse by drag.

---

## 3. Smooth Bore vs Rifling — Trade Table

| Factor | Smooth bore | Light rifling *(1:48 – 1:72)* | Full rifling *(1:12 – 1:20)* |
|--------|-------------|-------------------------------|------------------------------|
| **Tube manufacturing** | Lowest cost; straight bore; high-volume tile friendly | Single-groove or polygroove; moderate cost | Precision twist; per-tube QC; **130+ tubes/tile** cost penalty |
| **Muzzle velocity** | Baseline | −1–3% *(engraving loss)* | −3–8% *(engraving + friction)* |
| **“Speed boost”** | N/A | **No** — rifling does not add energy | **No** |
| **Pre-peel stability** | Adequate at 61 m; puck is blunt, drag-stabilized | Modest gyroscopic stability | High spin; overkill for 80 ms flight |
| **Option D peel timing** | **Independent of spin** — fixed `t_release` | Same — spin is side effect | Same, but spin couples to `V_0` via twist |
| **BB spread at peel** | Setback + petal geometry + drag only | **+ tangential ω×r** on loose BBs as skirt opens | Strong centrifugal bias; risk of **asymmetric cone** |
| **Pattern symmetry** | Best — axisymmetric release | Good if spin axis ∥ velocity | **Risk:** yaw during spin-up → elliptical pattern |
| **Wind / cross-track** | Minimal gyro drift | Low | Medium — Magnus + gyroscopic drift |
| **Option A compatibility** | Cannot use spin-release without rifling | Partial — low RPM insufficient for collet release | **Required** for centrifugal collet threshold |
| **Hollow-point skirt (PUCK-B)** | **Clean match** — peel driven by setback, not spin | Compatible if peel remains setback-triggered | Peel timing vs centrifugal release **conflicts** if both active |
| **Recommendation** | **MKFS baseline** | **Optional Phase 2 dispersion variant** | Not recommended for terminal strip |

---

## 4. Does Rifling Give a Speed or Range Boost?

**No.** Muzzle velocity is set by propellant impulse, chamber pressure, and barrel length — not twist rate.

| Mechanism | Effect on `V_0` |
|-----------|-----------------|
| Propellant / chamber | **Primary** — sets energy budget |
| Barrel length (32 mm chamber) | Fixed; short impulse barrel |
| Rifling engraving | **Negative** — work done deforming puck/case interface |
| Spin kinetic energy | **Negative** — energy diverted from forward translation |

At 900 m/s and 1:12 twist, spin ≈ 72,000 RPM. That rotational energy (~few percent of total) comes **from** muzzle velocity, not in addition to it. For terminal defense, the design target is **cloud density at 350 ft**, not extended supersonic range.

---

## 5. Spin for Pattern Spread

### 5.1 What the ballistics model already assumes

[ballistics_model.py](../research/ballistics/ballistics_model.py) models post-release spread as:

- Fixed mechanical `R_open` via Option D (`t_release` = 0.078 s)
- Cone half-angle **3.3°** after peel
- Initial burst diameter **1.5 m**
- No explicit spin term *(Phase 1 baseline)*

Salvo density at 350 ft is driven by **tube count × flechettes × cone angle**, not spin.

### 5.2 Where spin could help

At skirt peel (`R_open`), loose **titanium BBs** inside the cavity acquire:

1. **Forward velocity** — carrier `V` at release (~850 m/s at 61 m)
2. **Radial ejection** — petal geometry + setback (~5–15 m/s in DEPLOYMENT_MECHANISM §5)
3. **Tangential component** — if puck is spinning: `v_t ≈ ω · r_bb`

Example — light rifling 1:60 twist at 900 m/s:

- Spin rate ≈ 900 / (0.031 × 60) ≈ **484 rad/s** (~4,600 RPM)
- At BB radius 12 mm: `v_t` ≈ **5.8 m/s**

That tangential term is **comparable to mechanical radial ejection** and could widen the cone **without changing `R_open` timing**, provided peel remains setback-driven.

### 5.3 Where spin could hurt

| Risk | Mechanism |
|------|-----------|
| Asymmetric peel | PUCK-B skirt petals designed for **forward setback**; high spin + yaw → uneven petal opening |
| Elliptical pattern | Spin axis not aligned with velocity vector during first 20 ms |
| Coupling to Option A | Centrifugal collet release **scales with ω²** — full rifling makes spin-release viable and **competes with** setback latch design |
| Manufacturing | 136+ rifled tubes per 2×1 ft tile vs smooth extrusion |

**Conclusion:** Spin is a **dispersion seasoning**, not the primary spread mechanism. Baseline spread comes from **hollow-point skirt peel + drag differential** (Option D + HP).

---

## 6. Option D vs Option A — Hybrid or Pick One?

| | Option D — Setback petal *(D-002 baseline)* | Option A — Centrifugal / spin-release |
|--|---------------------------------------------|----------------------------------------|
| **Release trigger** | Setback force @ launch → fixed `t_release` | RPM threshold → **requires rifling** |
| **`R_open` control** | Mechanical time; scales with `V_0` only | Twist rate × `V_0` → band tied to velocity **and** spin |
| **TRL** | 5 — proven sabot/petal logic | 4–5 — mature but spin-dependent |
| **PUCK-B peel** | **Primary** — skirt mushrooms aft | Conflicts if collet opens **before** setback peel completes |

### Recommendation

| Path | Disposition |
|------|-------------|
| **Option D alone** | **MKFS baseline** — smooth bore, setback peel, drag spread |
| **Option A as primary** | **Not recommended** — replaces timed peel with spin threshold; conflicts with D-002 |
| **D + A hybrid** | **Deferred Phase 2** *(per DEPLOYMENT_DOWN_SELECT.md §4)* — centrifugal collet **after** petal opens, only if pattern tests show insufficient radial spread; requires light rifling variant |

**Do not** use full rifling (1:12) to drive Option A release while Option D handles timing — dual release paths add failure modes and void the hollow-point storyboard sequence.

---

## 7. Interaction with PUCK-A / PUCK-B (D-011)

| Form | Rifling impact |
|------|----------------|
| **PUCK-A Standard Drum** | Smooth bore optimal — cylindrical case, scored skirt band; no nose engraving preference |
| **PUCK-B Hollow-Point Nose** | Smooth bore baseline; domed nose + skirt peel **does not require** gyroscopic stability; optional light twist for BB tangential spread at peel only |

Canonical renders and ICD use **A + B**. Neither form factor assumes rifle-bullet spin stabilization.

---

## 8. MKFS Baseline Recommendation

| Item | Decision |
|------|----------|
| **Tube bore** | **Smooth bore** — 33 mm straight |
| **Deployment** | **Option D** setback skirt peel — unchanged (D-002) |
| **Spread** | Mechanical peel + drag cone (3.3° half-angle in model) |
| **Rifling** | **Not baseline** |
| **Optional variant** | **Light rifling** (1:48 – 1:72, single groove) on dispersion-test tubes only — adds ~3–6 m/s tangential BB velocity at peel without enabling Option A collet release |
| **Full rifling / Option A primary** | **Reject** for terminal strip |

---

## 9. Ballistics Implications

| Model input | Smooth baseline | Light rifling variant *(future)* |
|-------------|-----------------|----------------------------------|
| `V_0` | 900 m/s | 880–890 m/s *(estimate −1–2%)* |
| `T_RELEASE_S` | 0.078 s | **Unchanged** — Option D |
| `DISPERSION_HALF_ANGLE_DEG` | 3.3° | 3.8–4.5° *(estimate if tangential spread validated)* |
| `R_open` | ~200 ft @ 900 m/s | ~196–198 ft *(minor `V_0` loss)* |
| Pattern @ 350 ft | ~24.5 ft dia.; salvo density per [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md) | +5–15% pattern area if half-angle increase confirmed by test |

Phase 2 range work (T2 series): compare smooth vs 1:60 twist on **pattern diameter and hits/m²** at 350 ft; update `ballistics_model.py` dispersion term only after witness-screen data.

---

## 10. Summary Answer

**Do we rifle the barrels?** **Not in baseline.** MKFS terminal tubes should be **smooth bore** with **Option D mechanical skirt peel**.

**Can spin help spread patterns?** **Yes, modestly** — light rifling can add tangential velocity to titanium BBs at peel — but it is **not** required to meet current salvo density targets, and it **does not** increase muzzle velocity or range.

**Hybrid?** Keep **Option D** for `R_open`; add **optional light twist** only as a Phase 2 dispersion experiment. Do **not** adopt full rifling or Option A spin-release as baseline — it conflicts with hollow-point setback peel and D-002.

---

## 11. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial rifling vs spin analysis; baseline smooth bore + Option D |

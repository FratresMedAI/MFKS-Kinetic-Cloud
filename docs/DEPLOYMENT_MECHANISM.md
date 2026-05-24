# MKFS Mechanical Deployment Mechanism

**Status:** Concept | Phase 9
**Purpose:** Option D setback release mechanism.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-DOC-DEPLOY-001  
**Version:** 0.1 (Phase 0)  
**Related:** [REQUIREMENTS.md](REQUIREMENTS.md) | [VEHICLE_INTEGRATION.md](VEHICLE_INTEGRATION.md) | [SYSTEM_ARCHITECTURE.md](architecture/SYSTEM_ARCHITECTURE.md) | [RIFLING_SPIN_ANALYSIS.md](RIFLING_SPIN_ANALYSIS.md) | [current_tasks.md](../tasks/current_tasks.md)

---

## 1. Purpose

Explore purely mechanical range-band deployment options for the MKFS carrier projectile. The deployment mechanism must release a **titanium BB / sub-projectile cloud** at preset distances with **no explosives and no electronic fuze** in the round.

---

## 2. Design Targets

| Parameter | Symbol | Target | Notes |
|-----------|--------|--------|-------|
| Cloud open distance | `R_open` | ~200 ft (61 m) | Deployment initiates; sub-projectiles begin dispersing |
| Primary damage band | `R_band` | 250–500 ft (76–152 m) | Peak pattern density and lethality |
| Maximum range | `R_max` | ~500 yd (457 m) | Terminal defense envelope |
| Design muzzle velocity | `V_0` | 900 m/s (2,953 ft/s) | Baseline for timing calculations |
| Launch elevation | `θ` | 15°–45° (typical 30°) | Vehicle mount dependent |

### Time-to-Range (Baseline `V_0` = 900 m/s, `θ` = 30°)

Drag-corrected values from [ballistics_model.py](../research/ballistics/ballistics_model.py) (Phase 1):

| Range | Time of Flight | Velocity at Range |
|-------|----------------|-------------------|
| 200 ft (61 m) — `R_open` | 0.081 s | 850 m/s |
| 250 ft (76 m) | 0.101 s | 838 m/s |
| 350 ft (107 m) | 0.144 s | 814 m/s |
| 500 ft (152 m) | 0.210 s | 780 m/s |
| 500 yd (457 m) | 0.731 s | 585 m/s |

### Mechanical R_open (Option D)

Setback release at fixed mechanical time `t_release` = 0.078 s. Downrange `R_open` scales with `V_0`:

| V₀ | R_open |
|----|--------|
| 855 m/s (-5%) | 190 ft |
| 900 m/s (nominal) | 200 ft |
| 945 m/s (+5%) | 210 ft |

See [BALLISTICS_RESULTS.md](../research/ballistics/BALLISTICS_RESULTS.md) for full sensitivity table.

---

## 3. Deployment Options Comparison

| Option | Mechanism | Range-Band Control | Pros | Cons | TRL Est. |
|--------|-----------|-------------------|------|------|----------|
| **A — Centrifugal / spin-release** | Carrier spun by rifling; centrifugal force overcomes retention at preset RPM | Spin rate at launch sets release RPM threshold | No moving clockwork; robust; scales with velocity | Requires stable spin; wind drift during spin-up; band tied to velocity | 4–5 |
| **B — Inertial timer (mechanical clockwork)** | Spring-driven escapement counts time from launch setback | Timer wound to preset delay before load | Precise time control independent of drag | Sensitive to setback force variation; temperature affects springs; complexity | 3–4 |
| **C — Drag-retarded sleeve** | Aerodynamic sleeve creates differential drag; internal slider trips at preset airspeed/decay | Sleeve geometry sets deceleration profile | Self-calibrating to air density; no spin requirement | Less precise band; wind sensitive; sleeve adds mass and drag | 4 |
| **D — Spring-loaded petal / setback release** | Setback force compresses spring; release at velocity-dependent stroke | Spring rate + preload sets release velocity threshold | Simple; low parts count; setback is well-characterized at launch | Band tied to muzzle velocity; less tunable in field | 5 |

---

## 4. Option Detail

### 4.1 Option A — Centrifugal / Spin-Release

**Principle:** Flechette pack retained by collet or sleeve. At rotational speed ω, centrifugal force F = m·r·ω² exceeds retention spring force; collet opens and releases sub-projectiles radially.

**Range-band mapping:**

- Release RPM tied to forward velocity via barrel rifling twist rate
- At `V_0` = 900 m/s and 1:12 twist, spin ≈ 72,000 RPM
- Retention spring preload selects release threshold → maps to distance via `t = R / (V_0 · cos θ)`

**Pros:** Mature concept (similar to dispersal munitions); no internal timer; survives high-G launch.

**Cons:** Pattern asymmetry if spin axis diverges from velocity vector; difficult to adjust band without spring swap.

---

### 4.2 Option B — Inertial Timer (Mechanical Clockwork)

**Principle:** Launch setback winds or releases an escapement mechanism (similar to time fuze train, but purely mechanical — no pyrotechnic delay). After preset elapsed time, release pin frees flechette container.

**Range-band mapping:**

- Delay `t_delay` set by band index on MKFS-IF-001 (3 positions)
- Standard band: `t_delay` ≈ 0.17 s → `R` ≈ 250 ft at `V_0` = 900 m/s

**Pros:** Direct time control; band adjustable pre-load without changing carrier mass significantly.

**Cons:** Setback force varies with propellant temperature and tube condition; clockwork vulnerable to shock before launch; higher part count.

---

### 4.3 Option C — Drag-Retarded Sleeve

**Principle:** Carrier nose carries a drag sleeve. Internal inertia-driven slider moves aft as drag decelerates the carrier relative to the sleeve. At preset stroke, release mechanism opens flechette chamber.

**Range-band mapping:**

- Sleeve Cd and mass ratio set deceleration profile
- Release occurs when `V_carrier` drops below threshold → correlates to downrange distance

**Pros:** Adapts to air density; no spin dependency.

**Cons:** Wind and rain increase drag unpredictability; band width wider (lower precision); added frontal area reduces `V_0`.

---

### 4.4 Option D — Spring-Loaded Petal / Setback Release

**Principle:** Launch setback compresses a Belleville or coil spring stack. At peak setback (proportional to muzzle velocity), petals or a frangible retention ring fracture or translate, releasing flechettes forward and radially.

**Range-band mapping:**

- Spring preload and rate selected so release completes during peak acceleration phase
- Effective "band" is the distance traveled during release event (~50–100 ft for petal opening)
- Band index adjusts preload via spacer shims (MKFS-IF-001 positions)

**Pros:** Simplest mechanism; highest TRL; minimal moving parts after launch; proven in kinetic penetrator sabots.

**Cons:** Release tied to muzzle velocity — propellant variation shifts `R_open`; less independent control of open vs. peak band.

---

## 5. Ti BB Cloud Dispersion Model (Initial Assumptions)

Phase 1 will develop a full model in `research/ballistics/`. Initial assumptions:

| Parameter | Assumed Value |
|-----------|---------------|
| Sub-projectile material | Titanium alloy (Ti-6Al-4V) — **BB spheres** |
| Sub-projectiles per carrier | **~40** *(ICD)* |
| Individual BB mass | 0.5–0.9 g |
| Form | 00-buck class sphere |
| Release velocity (sub-projectile) | Carrier velocity + 5–15 m/s radial spread |
| Pattern diameter at 350 ft | 15–25 ft (4.6–7.6 m) *(target)* |
| Pattern thickness (depth) | 30–50 ft (9–15 m) |

**Lethality criterion (design target):** ≥ 1 **Ti BB** strike per 0.5 m² at 350 ft against Class 1–2 UAS *(assumed — requires test validation)*.

---

## 6. Environmental Sensitivity

| Factor | Option A | Option B | Option C | Option D |
|--------|----------|----------|----------|----------|
| Temperature | Low | High (springs) | Medium | Medium (spring rate) |
| Wind | Medium | Low | High | Low |
| Propellant temp / `V_0` drift | High | Medium | Low | High |
| Rain/humidity | Low | Low | High | Low |
| Altitude (air density) | Low | Low | High | Low |

**Mitigation strategies:**

- Band index pre-selection accounts for nominal conditions
- Propellant temperature compensation at launcher (adjust elevation, not round)
- Phase 1 ballistics model includes ±10% `V_0` sensitivity sweep

---

## 7. Carrier Projectile Interface

### What Moves

| Component | Function |
|-----------|----------|
| Retention collet / petals | Opens to release flechettes |
| Flechette pack | Disperses radially and forward |
| (Option C only) Drag sleeve | Slides relative to carrier body |

### What Stays Fixed

| Component | Function |
|-----------|----------|
| Carrier body | Provides mass, aerodynamic stability, sabot interface |
| Primer pocket | Launcher-initiated ignition only |
| Band index key | Mechanical pre-set; no post-launch adjustment |

### MKFS-IF-001 Band Index Positions

| Position | Target `R_open` | Target `R_band` peak |
|----------|-----------------|---------------------|
| Short | 150 ft (46 m) | 200–350 ft |
| Standard | 200 ft (61 m) | 250–500 ft |
| Long | 250 ft (76 m) | 350–500 ft |

---

## 8. Tube Bore — Rifling vs Smooth (See MKFS-DOC-RIFL-001)

Full analysis: [RIFLING_SPIN_ANALYSIS.md](RIFLING_SPIN_ANALYSIS.md).

| Question | Answer |
|----------|--------|
| Rifle the barrels? | **No — smooth bore baseline** (33 mm straight) |
| Does spin boost `V_0` or range? | **No** — rifling costs engraving energy; does not add propellant impulse |
| Can spin widen the BB cloud? | **Modestly** — optional light twist (1:48–1:72) adds tangential spread at peel |
| Conflict with Option D peel? | Full rifling + Option A spin-release **conflicts** with setback skirt timing |
| Hybrid path | **Option D primary**; light rifling only as Phase 2 dispersion variant (D+A downstream collet per down-select) |

Option A in §3 assumes rifling for centrifugal release. MKFS baseline keeps Option D on **smooth bore**; spin is not required for `R_open` or current salvo density targets.

---

## 9. Recommended Baseline

**Primary recommendation: Option D — Spring-loaded petal / setback release**

**Rationale:**

1. **Highest TRL** — Setback-driven release is proven in kinetic ammunition; no novel clockwork or drag-dependent logic
2. **Kinetic-only compliance** — Pure spring mechanics; no energetics; no electronics
3. **Simplicity** — Lowest part count supports high production volume and field reliability
4. **Launch survivability** — No fragile timer train; withstands multi-tube salvo shock

**Secondary / hybrid path:** Option A (centrifugal) as a variant for improved radial dispersion if Option D pattern testing shows insufficient cone angle. Centrifugal collet can augment petal release without adding energetics.

**Not recommended for baseline:**

- Option B — Clockwork complexity and setback sensitivity outweigh precision benefit
- Option C — Drag variability too high for 250–500 ft band precision against swarms

---

## 10. Phase 1 Validation Plan

| Task | Method | Success Criteria |
|------|--------|------------------|
| Setback release timing | High-speed video + strain gauges | Release within 0.5 ms of peak setback |
| Pattern diameter at 350 ft | Indoor range + witness screens | 15–25 ft pattern diameter |
| `V_0` sensitivity | ±5% velocity test series | `R_open` shift ≤ 30 ft |
| Environmental | Cold/hot chamber (-25°F / 125°F) | Band shift ≤ 10% |
| Down-select | Trade study review | Option D confirmed or hybrid documented |

---

## 11. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 0 initial deployment options and baseline recommendation |
| 0.2 | 2026-05-22 | §8 rifling vs smooth bore; cross-link RIFLING_SPIN_ANALYSIS |

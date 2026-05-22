# MKFS Caliber Trade Study

**Document ID:** MKFS-RES-CAL-001  
**Decision:** D-001  
**Recommendation:** **30 mm** — adopt as MKFS-IF-001 baseline caliber  
**Related:** [CARRIER_PROJECTILE_ICD.md](../docs/CARRIER_PROJECTILE_ICD.md) | [REQUIREMENTS.md](../docs/REQUIREMENTS.md)

---

## 1. Purpose

Select the nominal cartridge caliber for `MKFS-CART-STD` balancing flechette capacity, tube density, muzzle velocity, and fleet logistics.

---

## 2. Candidates

| Caliber | Case Volume | Est. V₀ | Flechette Mass Budget | Tubes (610 mm face) | Notes |
|---------|-------------|---------|----------------------|---------------------|-------|
| **25 mm** | Low | 950 m/s | 100 g | 36 (50 mm pitch) | High tube count; low flechette count per round |
| **30 mm** | Medium | 900 m/s | 132 g | 25 (76 mm pitch) | Balanced; existing 30 mm ammo industrial base |
| **40 mm** | High | 780 m/s | 180 g | 16 (96 mm pitch) | Heavy; fewer tubes; lower velocity hurts `R_open` mapping |

---

## 3. Evaluation Criteria

| Criterion | Weight | 25 mm | 30 mm | 40 mm |
|-----------|--------|-------|-------|-------|
| Flechette count per salvo (25-tube equiv.) | 25% | 2,160 (60×36) | **2,500 (100×25)** | 1,600 (100×16) |
| Pattern density at 350 ft | 25% | 1.8 hits/m² *(est.)* | **0.17 single / 57 salvo** *(model)* | 2.1 hits/m² *(est.)* |
| Tube density on 2×2 ft module | 20% | **36** | 25 | 16 |
| Muzzle velocity / range timing | 15% | Good | **Good** | Marginal |
| Logistics / production | 15% | Moderate | **Strong** | Moderate (40 mm LV niche) |

*30 mm scores highest on weighted trade — best salvo flechette mass and modeled pattern density.*

---

## 4. Tube Layout Impact (MKFS-IF-002)

| Caliber | Pitch | Compact | Standard | Dense |
|---------|-------|---------|----------|-------|
| 25 mm | 50 mm | 25 | 36 | 49 |
| **30 mm** | **76 mm** | **16** | **25** | **36** |
| 40 mm | 96 mm | 9 | 16 | 25 |

Standard tier at 30 mm (25 tubes) fits the ~2×2 ft module with adequate wall thickness between tubes.

---

## 5. Range Band Impact

At lower V₀ (40 mm), drag-corrected `R_open` shifts aft for same setback timing — requires heavier spring preload and reduces margin. 25 mm and 30 mm both achieve `R_open` ≈ 200 ft within ±30 ft at nominal conditions.

---

## 6. Decision

**Select 30 mm** as MKFS-IF-001 baseline caliber.

**Rationale:**
1. Highest flechette mass per standard-module salvo (2,500 flechettes vs. 2,160 for 25 mm dense)
2. Ballistics model confirms pattern targets at 350 ft with 100 flechettes/round
3. 30 mm automatic cannon industrial base (Bradley, Apache chain gun lineage) supports production
4. Standard tier (25 tubes) aligns with vehicle power/mass budgets across fleet

**Action:** Update MKFS-IF-001 caliber from "TBD" to **30 mm** in REQUIREMENTS.md.

---

## 7. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | D-001 resolved — 30 mm recommended |

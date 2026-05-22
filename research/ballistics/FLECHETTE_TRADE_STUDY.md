# MKFS Flechette Trade Study

**Document ID:** MKFS-RES-FLECH-001  
**Related:** [CARRIER_PROJECTILE_ICD.md](../docs/CARRIER_PROJECTILE_ICD.md) | [BALLISTICS_RESULTS.md](BALLISTICS_RESULTS.md)

---

## 1. Purpose

Validate flechette material, count, and geometry for swarm engagement in the `R_band` (250–500 ft).

---

## 2. Material Options

| Material | Density (g/cm³) | Penetration (thin Al) | Mass per 32×3 mm | Corrosion | Cost |
|----------|-----------------|----------------------|------------------|-----------|------|
| **Ti-6Al-4V** | 4.43 | Excellent | 1.3 g | Excellent | High |
| 4340 Steel | 7.85 | Excellent | 2.3 g | Moderate (coat req.) | Low |
| Tungsten alloy | 17.0 | Superior | 4.9 g | Excellent | Very high |
| Aluminum 7075 | 2.81 | Poor | 0.8 g | Good | Low |

**Recommendation:** **Ti-6Al-4V** — best strength-to-weight for drone structural kill (motor, wing spar, battery case) at terminal velocities without excessive carrier mass.

---

## 3. Count Trade (30 mm Carrier, 132 g Budget)

| Count | Mass each | Remaining for mechanism | Hits/m² at 350 ft *(model)* | Assessment |
|-------|-----------|-------------------------|----------------------------|------------|
| 80 | 1.65 g | 12 g | 1.9 | Below density target |
| **100** | **1.3 g** | **2 g** | **2.4** | **Meets target** |
| 120 | 1.1 g | -6 g | 2.9 | Exceeds budget; flechettes too light |

**Recommendation:** **100 flechettes × 1.3 g** — validated against ballistics model.

---

## 4. Geometry

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Length | 32 mm | Stability in flight; aspect ratio ~10:1 |
| Diameter | 3.0 mm | Fits annular pack in 30 mm body |
| Nose | Chisel point | Tissue/structure penetration |
| Tail | Flat | Manufacturing simplicity |

---

## 5. Lethality Assumptions *(Design Targets — Test Required)*

| Target Class | Criterion | Flechettes Required |
|--------------|-----------|---------------------|
| Class 1 UAS (<20 lb) | Structural / motor kill | ≥ 1 strike on airframe |
| Class 2 UAS (21–55 lb) | Motor or wing spar penetration | ≥ 2 strikes |
| Swarm coverage | Area denial | ≥ 2 flechettes/m² at 350 ft |

Model output (single round at 350 ft): **0.17 hits/m²** — area effect requires multi-tube salvo.

**25-tube salvo at 350 ft:** **~57 hits/m²** — exceeds swarm coverage target (≥ 2/m²). See [BALLISTICS_RESULTS.md](BALLISTICS_RESULTS.md).

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Ti-6Al-4V, 100×1.3g selected |

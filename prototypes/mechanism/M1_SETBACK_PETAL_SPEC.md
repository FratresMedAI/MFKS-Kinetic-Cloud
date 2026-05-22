# M1 Setback Petal Mechanism — Build Spec

**Document ID:** MKFS-PROTO-M1-001  
**Version:** 0.1 (Phase 8)  
**Milestone:** M1 — Mechanism proof  
**Related:** [TEST_EVAL_PLAN.md](../../docs/TEST_EVAL_PLAN.md) T1-001 | [PUCK_CUTAWAY_STORYBOARD.md](../../docs/visual/PUCK_CUTAWAY_STORYBOARD.md) | [RIFLING_SPIN_ANALYSIS.md](../../docs/RIFLING_SPIN_ANALYSIS.md) | [CARRIER_PROJECTILE_ICD.md](../../docs/CARRIER_PROJECTILE_ICD.md)

---

## 1. Objective

Desk-to-shop bridge for **PUCK-B hollow-point skirt + Option D setback petal** release. First hardware validates peel timing and score-line geometry — **no propellant formulation** in this spec.

---

## 2. Geometry — PUCK-B Skirt

| Feature | Spec |
|---------|------|
| Form factor | **PUCK-B** Hollow-Point Nose (D-011) |
| OAL | 28 mm ± 0.3 mm |
| Diameter | 31.0 mm ± 0.1 mm |
| Petal count | 4–6 segments |
| Score lines | Radial, 0.15–0.25 mm depth, 60–70% wall thickness |
| Band index | 3-position preload ring on base (short / standard / long) |
| Payload cavity | ~40 **titanium BBs** (Ti-6Al-4V spheres, 00-buck class) |

### Option D setback interface

```
  Nose cap (setback mass) ──► loads skirt latch
  Skirt petals ──► preloaded radial flex at score lines
  Release ──► fixed t_release ≈ 0.078 s from primer initiation (mechanical)
```

---

## 3. Materials *(Placeholder BOM)*

| Part | Material | Qty | Notes |
|------|----------|-----|-------|
| Skirt / petals | 17-4 PH SS or Ti-6Al-4V sheet | 1 | Laser-cut + score |
| Nose ogive | Al alloy or SS | 1 | Hollow-point profile |
| Setback cap | SS | 1 | Mass tuned for T1-001 G threshold |
| Case base | SS | 1 | Primer pocket mock (electric) |
| Ti BB payload | Ti-6Al-4V spheres | ~40 | Simulant mass only for drop tests |
| Latch wire | SS music wire | 4 | Replaceable per shot |

**Excluded:** Propellant, live primer energetics — separate controlled program.

---

## 4. Test Fixture

| Item | Spec |
|------|------|
| Tube bore | **33 mm smooth** (baseline per [RIFLING_SPIN_ANALYSIS.md](../../docs/RIFLING_SPIN_ANALYSIS.md)) |
| Launch sim | Gas gun or sled @ 850–950 m/s equivalent setback |
| Instrumentation | High-speed side camera (≥ 10 kfps) per storyboard §6 |

---

## 5. Pass Criteria — T1-001

From [TEST_EVAL_PLAN.md](../../docs/TEST_EVAL_PLAN.md):

| Criterion | Target |
|-----------|--------|
| Setback petal release | **85% peak G ± 5%** |
| Peel initiation | Visible skirt flex before full petal open |
| Inadvertent release | None in T1-003 drop orientations |

---

## 6. High-Speed Camera Setup

From [PUCK_CUTAWAY_STORYBOARD.md](../../docs/visual/PUCK_CUTAWAY_STORYBOARD.md) §6:

| Camera | Frame | Purpose |
|--------|-------|---------|
| High-speed side | 3–4 | Skirt peel timing |
| Front ortho | 4–5 | Pattern origin |
| Downrange wide | 6 | Cloud diameter @ 350 ft *(M2)* |

---

## 7. Deliverables

| Artifact | Location |
|----------|----------|
| Petal CAD *(future)* | `prototypes/mechanism/` |
| T1-001 video | Range data archive |
| Pass/fail report | Linked from M1 milestone |

---

## 8. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 8 M1 desk-to-shop spec |

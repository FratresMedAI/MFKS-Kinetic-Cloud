# MKFS Puck Cutaway Storyboard

**Document ID:** MKFS-VIS-STORY-001  
**Version:** 0.1 (Phase 5)  
**Related:** [PUCK_RELEASE.md](../PUCK_RELEASE.md) | [CARRIER_PROJECTILE_ICD.md](../CARRIER_PROJECTILE_ICD.md)

---

## 1. Purpose

Frame-by-frame storyboard for hollow-point puck release — for illustrators, animators, and range camera placement. **No new render in this sprint** — structured brief only.

---

## 2. Puck Key Dimensions

From [CARRIER_PROJECTILE_ICD.md](../CARRIER_PROJECTILE_ICD.md):

| Dimension | Value |
|-----------|-------|
| Diameter | 31 mm |
| Length | 28 mm |
| Mass | ~63 g |
| Flechette payload | ~40 Ti @ 1.3 g |

---

## 3. Timeline

```mermaid
flowchart LR
  F1[Frame1_Launch] --> F2[Frame2_Flight]
  F2 --> F3[Frame3_Setback]
  F3 --> F4[Frame4_SkirtPeel]
  F4 --> F5[Frame5_DragSpread]
  F5 --> F6[Frame6_Cloud]
```

---

## 4. Frame Descriptions

### Frame 1 — Launch (t = 0 ms)

**View:** Side cutaway, tube chamber  
**Action:** Electric primer fires; puck accelerates; setback loads nose/skirt interface  
**Callouts:** 31 mm diameter, 850–950 m/s muzzle velocity  
**Art note:** Show flechettes stacked inside skirt cavity, nose ogive intact  

```
  [  TUBE  ]
  |  ████  |  ← puck in tube
  |  ████  |
  [========]  primer
```

---

### Frame 2 — Supersonic flight (t = 20–80 ms)

**View:** External side, no cutaway  
**Action:** Puck stable; skirt latch holds; air flow over ogive  
**Callouts:** ~200 ft to R_open  
**Art note:** Minimal vapor trail; no HE flash  

---

### Frame 3 — Setback release (t = 78 ms / R_open)

**View:** Cutaway side + front quarter  
**Action:** Setback force exceeds latch; skirt begins radial peel  
**Callouts:** T_release = 0.078 s mechanical; R_open ≈ 200 ft  
**Art note:** Skirt petals mid-flex — strain visible at score lines  

```
       ___
      /   \   ← nose
     | * * |  ← flechettes inside
      \___/
       | |     ← skirt peeling
```

---

### Frame 4 — Skirt peel (t = 80–120 ms)

**View:** Front orthographic + side  
**Action:** Skirt petals fully open; flechettes begin radial ejection  
**Callouts:** Hollow-point geometry — opens from front  
**Art note:** 4–6 petal segments; no explosive burst  

---

### Frame 5 — Drag spread (t = 120–200 ms)

**View:** 3/4 perspective, cloud forming  
**Action:** Light flechettes decelerate faster; heavy continue forward  
**Callouts:** Drag differential spreads cloud; ~3.3° half-angle cone  
**Art note:** Streak lines for flechette paths; puck body tumbles aft  

---

### Frame 6 — Flechette cloud (t = 200 ms+, at target range)

**View:** Wide — target volume at 350 ft  
**Action:** Cloud ~24 ft diameter; saturation pattern  
**Callouts:** 100 flechettes per puck; 310+ hits/m² per 136-tube salvo  
**Art note:** Abstract density heatmap overlay optional  

---

## 5. Camera / Instrument Placement (Range)

| Camera | Frame | Purpose |
|--------|-------|---------|
| High-speed side | 3–4 | Skirt peel timing |
| Front ortho | 4–5 | Pattern origin |
| Downrange wide | 6 | Cloud diameter at 350 ft |

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial puck cutaway storyboard |

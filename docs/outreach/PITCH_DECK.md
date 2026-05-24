# MFKS / MKFS Pitch Deck

**Status:** Concept | Phase 9
**Purpose:** Pitch deck outline.
**Key Decisions:** See [../DECISIONS.md](../DECISIONS.md)
**Open Questions:** See [../RISK_REGISTER.md](../RISK_REGISTER.md)

**10 slides · markdown format**

---

## Slide 1 — Title

# MFKS / MKFS  
## Modular Flechette Kinetic System

**Last-ditch terminal defense against drone swarms**

FratresMedAI · Apache 2.0 Open Concept  
[github.com/FratresMedAI/MFKS-Kinetic-Cloud](https://github.com/FratresMedAI/MFKS-Kinetic-Cloud)

---

## Slide 2 — The Problem

- Drone swarms close to **200–500 yd**  
- EW degraded · missiles exhausted · no ship CIWS on land vehicles  
- Need: **don't die** layer — volume over precision  

*"By the time they're close, elegance doesn't matter."*

---

## Slide 3 — Swarm Math

| Threat | Challenge |
|--------|-----------|
| 8–15 drones simultaneously | Single-shot interceptors lose |
| 300–400 yd closure | Seconds to act |
| Autonomous after jamming | Soft kill insufficient |

**Answer:** Saturate the terminal volume with **titanium BB clouds**.

---

## Slide 4 — Kinetic Thesis

| Not this | This |
|----------|------|
| HE warheads | Mechanical cloud |
| Guided submunitions | Fixed tube aim + FCU sector |
| DEW power hog | 28 VDC strip |
| $500K missile | ~$100 puck ROM |

**Return to physics. Strip rate fire.**

---

## Slide 5 — Puck Forms

![PUCK-A Standard Drum + PUCK-B Hollow-Point Nose](../../assets/mkfs_puck_design_comparison_4up.png)

| Form | Role |
|------|------|
| **PUCK-A** | Tube fill, chamber diagrams |
| **PUCK-B** | Hollow-point peel, cutaways, storyboard |

→ [PUCK_DESIGN_OPTIONS.md](../../assets/PUCK_DESIGN_OPTIONS.md) · D-011

---

## Slide 6 — Puck Mechanism

**MKFS-CART-PUCK** — 31 mm × 28 mm hollow-point carrier

1. Launch @ 900 m/s  
2. Setback @ ~200 ft (`R_open`)  
3. Skirt peels — hollow-point geometry  
4. Drag spreads **~40 titanium BBs** per puck  

→ [PUCK_RELEASE.md](../PUCK_RELEASE.md) · [PUCK_CUTAWAY_STORYBOARD.md](../visual/PUCK_CUTAWAY_STORYBOARD.md)

---

## Slide 7 — Packaging

| Line | Mount | Tubes |
|------|-------|-------|
| **Appliqué** | Stryker / JLTV / hull | 136–208 per strip |
| **Turret** | Pan-tilt moving head | 289 × 3–4 decks |
| **Truck** | Standalone 6×6 | Full mobile magazine |

Flat tube batteries — not box launchers.

---

## Slide 8 — Ballistics Headline

**@ 350 ft · ~24 ft pattern**

| Config | Hits/m² |
|--------|---------|
| 2×1 strip | **310** |
| 3×1 strip | **474** |
| Turret deck | **659** |
| 3-deck dump | **1,977** |

→ [SALVO_SCENARIOS.md](../../research/ballistics/SALVO_SCENARIOS.md)

---

## Slide 9 — Safety & Fratricide

- FCU interlocks: dismount zones, elevation limits, sector masks  
- **LAST_DITCH_FULL** requires dual confirmation near friendlies  
- Coexists with Trophy/CIWS — terminal band deconfliction  

→ [FRATRICIDE_DECONFLICTION.md](../FRATRICIDE_DECONFLICTION.md)

---

## Slide 10 — Roadmap

| Milestone | Status |
|-----------|--------|
| Concept + ICD + ballistics | **Done** (open repo) |
| M1 mechanism prototype | Next — [M1_SETBACK_PETAL_SPEC.md](../../prototypes/mechanism/M1_SETBACK_PETAL_SPEC.md) |
| 136-tube range test | T5 concept ready |
| Stryker mount | Adapter spec done |

→ [PROTOTYPE_ROADMAP.md](../../prototypes/PROTOTYPE_ROADMAP.md)

---

## Slide 11 — Collaborate

**We provide:** ICD, CONOPS, ballistics model, FCU stub, renders  
**We seek:** Mechanism prototype, range data, adapter CAD, manufacturing ROM  

Apache 2.0 · Issues & PRs welcome  

→ [COLLABORATION_CHARTER.md](../COLLABORATION_CHARTER.md)  
→ [QUESTIONS_FOR_PRIMES.md](QUESTIONS_FOR_PRIMES.md)

**Let's talk.**

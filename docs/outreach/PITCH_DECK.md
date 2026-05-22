# MFKS / MKFS Pitch Deck

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

**Answer:** Saturate the terminal volume with kinetic flechettes.

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

## Slide 5 — Puck Mechanism

**MKFS-CART-PUCK** — 31 mm × 28 mm hollow-point carrier

1. Launch @ 900 m/s  
2. Setback @ ~200 ft (`R_open`)  
3. Skirt peels — hollow-point geometry  
4. Drag spreads **~100 Ti flechettes** per puck  

→ [PUCK_RELEASE.md](../PUCK_RELEASE.md)

---

## Slide 6 — Packaging

| Line | Mount | Tubes |
|------|-------|-------|
| **Appliqué** | Stryker / JLTV / hull | 136–208 per strip |
| **Turret** | Pan-tilt moving head | 289 × 3–4 decks |
| **Truck** | Standalone 6×6 | Full mobile magazine |

Flat tube batteries — not box launchers.

---

## Slide 7 — Ballistics Headline

**@ 350 ft · ~24 ft pattern**

| Config | Hits/m² |
|--------|---------|
| 2×1 strip | **310** |
| 3×1 strip | **474** |
| Turret deck | **659** |
| 3-deck dump | **1,977** |

→ [SALVO_SCENARIOS.md](../../research/ballistics/SALVO_SCENARIOS.md)

---

## Slide 8 — Safety & Fratricide

- FCU interlocks: dismount zones, elevation limits, sector masks  
- **LAST_DITCH_FULL** requires dual confirmation near friendlies  
- Coexists with Trophy/CIWS — terminal band deconfliction  

→ [FRATRICIDE_DECONFLICTION.md](../FRATRICIDE_DECONFLICTION.md)

---

## Slide 9 — Roadmap

| Milestone | Status |
|-----------|--------|
| Concept + ICD + ballistics | **Done** (open repo) |
| M1 mechanism prototype | Next |
| 136-tube range test | T5 concept ready |
| Stryker mount | Adapter spec done |

→ [PROTOTYPE_ROADMAP.md](../../prototypes/PROTOTYPE_ROADMAP.md)

---

## Slide 10 — Collaborate

**We provide:** ICD, CONOPS, ballistics model, FCU stub, renders  
**We seek:** Mechanism prototype, range data, adapter CAD, manufacturing ROM  

Apache 2.0 · Issues & PRs welcome  

→ [COLLABORATION_CHARTER.md](../COLLABORATION_CHARTER.md)  
→ [QUESTIONS_FOR_PRIMES.md](QUESTIONS_FOR_PRIMES.md)

**Let's talk.**

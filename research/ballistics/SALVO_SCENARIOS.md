# MKFS Salvo Scenarios — Tube Count Recalibration

**Document ID:** MKFS-RES-SALVO-001  
**Version:** 0.1 (Phase 5)  
**Generated from:** [`ballistics_model.py`](ballistics_model.py) · [`ballistics_output.json`](ballistics_output.json)  
**Related:** [DESIGN_PHILOSOPHY.md](../../docs/DESIGN_PHILOSOPHY.md) | [BALLISTICS_RESULTS.md](BALLISTICS_RESULTS.md)

---

## 1. Why This Doc Exists

Early ballistics used a **25-tube** legacy module. Design intent now specifies **136 / 208 / 289** tubes per face, with turret magazines stacked **3–4 decks deep**. This document compares salvo outcomes at **350 ft** (nominal band center) using the updated model.

---

## 2. Headline Comparison at 350 ft

Pattern diameter: **24.5 ft** (7.47 m) — unchanged per puck; density scales with tube count.

| Config | Tubes | Flechettes in air | Hits/m² @ 350 ft |
|--------|-------|-------------------|------------------|
| Legacy 25-tube module | 25 | 2,500 | 57 |
| **2×1 ft appliqué strip** | **136** | **13,600** | **310** |
| **3×1 ft appliqué strip** | **208** | **20,800** | **474** |
| **2×2 ft turret — 1 deck** | **289** | **28,900** | **659** |
| **2×2 ft turret — 3 decks (full dump)** | **867** | **86,700** | **1,977** |
| **2×2 ft turret — 4 decks (full dump)** | **1,156** | **115,600** | **2,636** |

---

## 3. What the Numbers Mean

**Single puck (1 tube):** 2.28 hits/m² — insufficient alone. MKFS was never a one-shot system.

**One 2×1 strip (136 tubes):** 310 hits/m² — roughly **5×** the legacy 25-tube salvo. Enough to saturate a swarm lane in the terminal band.

**One turret deck (289 tubes):** 659 hits/m² — CIWS-class volume in a single mechanical dump, no gatling, no HE.

**Full turret dump (867 tubes, 3 decks):** ~1,977 hits/m² — last-ditch **"don't die"** profile. The cloud is not a precision shot; it is **volume denial** in a ~24 ft footprint at 350 ft.

---

## 4. Pattern Envelope Across R_band

At shorter range (230 ft), pattern tightens (~9 ft dia) and density spikes. At band max (~492 ft), pattern widens (~42 ft) and density falls. See [BALLISTICS_RESULTS.md](BALLISTICS_RESULTS.md) § Multi-Salvo Envelope.

**Design implication:** FCU should bias engagement to **250–400 ft** when cue quality allows — best density without over-spreading.

---

## 5. Assumptions and Limits

- Point-mass carrier trajectory; flechettes inherit cloud cone after mechanical `R_open` (~200 ft)
- All tubes fire into overlapping cone — no per-tube aim (sector masks refine footprint in FCU)
- Model does not simulate deck stagger timing or cross-deck pattern merge
- Stdlib-only model — regenerate with `python research/ballistics/ballistics_model.py`

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial salvo recalibration for 136/208/289/867/1156 tube configs |

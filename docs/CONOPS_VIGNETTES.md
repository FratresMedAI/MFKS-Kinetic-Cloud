# MKFS CONOPS Vignettes

**Document ID:** MKFS-DOC-CONOPS-001  
**Version:** 0.1 (Phase 5)  
**Related:** [ICD_SENSOR_INTEGRATION.md](ICD_SENSOR_INTEGRATION.md) | [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md) | [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md)

---

## 1. Purpose

Five operational vignettes illustrating MKFS **last-ditch** employment — threat cue through salvo, outcome, and magazine state. Concept narratives only.

---

## Vignette 1 — Stryker Overwatch, EW Degraded

**Platform:** Stryker ICV with dual 2×1 ft strips (272 tubes)  
**Threat:** 8× FPV quadcopters, approach from 10 o'clock, range closing 450 → 350 yd  
**Conditions:** EW jamming active — drone autonomy degraded but not eliminated; no dedicated C-UAS radar

| Phase | Action |
|-------|--------|
| Detect | Gunner sees visual + RWS EO track; FCU receives bearing/elevation via vehicle Ethernet |
| Cue | Manual confirm on FCU panel — threat track valid |
| FCU | STANDBY → ARMED → ENGAGING |
| Salvo | **SWARM_WIDE** on forward strip (136 tubes) @ 10 ms inter-tube |
| Outcome | 3 drones down at ~380 yd; 2 damaged; 3 penetrate — aft strip **SECTOR_LEFT** catches remainder at ~320 yd |
| Magazine | Forward pod **empty**; aft pod **~40 tubes** remaining |
| Reload | Crew swaps forward pod under cover of aft tile — see [RELOAD_UNDER_FIRE.md](visual/RELOAD_UNDER_FIRE.md) |

---

## Vignette 2 — JLTV Convoy, Mixed Approach Angles

**Platform:** JLTV with 2× 2×1 ft strips (port/starboard roof)  
**Threat:** 6× fixed-wing loiterers + 4× FPV from rear arc, simultaneous  
**Conditions:** Convoy speed 15 kph; SI-001 override armed for slow convoy

| Phase | Action |
|-------|--------|
| Detect | Optional swarm kit *(D-005)* provides coarse track; commander confirms |
| Cue | Dual threat azimuths — FCU allocates modules |
| Salvo | Port strip **SWARM_FOCUS** (90 tubes, forward sector); starboard **SWARM_BURST** (full 136, rear arc) |
| Outcome | Rear threat neutralized; port strip suppresses forward lane — 2 leakers |
| Magazine | Port **46 tubes**; starboard **empty** |
| Reload | Starboard pod swap at next halt; convoy continues |

---

## Vignette 3 — Bradley Dismount in Progress

**Platform:** Bradley with bustle + hull strips  
**Threat:** 5× FPV from 2 o'clock, 400 yd  
**Conditions:** Squad dismounted within 50 m — **fratricide tension**

| Phase | Action |
|-------|--------|
| Detect | RWS track + commander visual |
| Cue | GPS dismount zone active — SI-002 inhibit arc covers 090°–150° |
| Salvo | **SECTOR_RIGHT** only — 68 tubes, elevation +5° trim per [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md) |
| Outcome | 4 of 5 drones defeated; 1 exits vertically — out of band |
| Magazine | Partial salvo — **68 tubes** fired, **68 remain** on active strip |
| Note | Full dump blocked by dismount interlock — deliberate design |

---

## Vignette 4 — USV Conning Tower, Maritime Low Flyer

**Platform:** Unmanned surface vessel, 2× 2×1 ft strips on tower faces (port/starboard)  
**Threat:** 3× low-altitude fixed-wing, stern approach, 350 yd  
**Conditions:** Sea state 3; no vehicle speed interlock

| Phase | Action |
|-------|--------|
| Detect | Tower EO camera + manual track *(no RWS)* |
| Cue | FCU manual azimuth entry |
| Salvo | Both strips **SWARM_WIDE** — overlapping 180° coverage |
| Outcome | All 3 targets enter flechette band; 2 confirmed kill, 1 unconfirmed |
| Magazine | Both pods **empty** |
| Reload | Shore-side pod swap — see [MARITIME_FIXED_SITE.md](MARITIME_FIXED_SITE.md) |

---

## Vignette 5 — Standalone Support Truck, Turret Full Dump

**Platform:** 6×6 support vehicle with pan-tilt turret (289 × 3 decks = 867 tubes)  
**Threat:** 15× mixed swarm, 360° encirclement, 300–400 yd  
**Conditions:** Last vehicle in column; no other C-UAS remaining

| Phase | Action |
|-------|--------|
| Detect | Turret EO + optional swarm kit |
| Cue | FCU auto-sector on highest-density track cluster |
| Salvo | **LAST_DITCH_FULL** — all 867 tubes, 0–5 ms inter-tube |
| Outcome | ~1,977 hits/m² @ 350 ft — swarm broken; 11 of 15 down, remainder abort |
| Magazine | **All decks empty** — turret shutters close |
| Reload | 15–20 min deck reload *(concept)* or withdraw |
| Decision | Commander accepts one-shot defense — second swarm requires resupply |

---

## Vignette 6 — Radar Cue, Terminal Strip Kill

**Platform:** MRAP with `MKFS-SENS-EM-RADAR` on forward 2×1 strip + dual strips (272 tubes)  
**Threat:** 8× FPV, approach from 600 yd  
**Conditions:** ESM picks up 5.8 GHz links; radar tracks at 550 yd

| Phase | Action |
|-------|--------|
| Detect | EM bearing cues radar; fused track to FCU @ 550 yd |
| Stage | Commander arms; FCU stages **SWARM_WIDE** on both strips |
| Terminal | At **380 yd** both strips fire — phased 20 ms offset — 272 tubes |
| Outcome | 7 of 8 down; 1 leaker — **SECTOR_LEFT** finishes at 290 yd |
| Magazine | Forward pod **empty**; aft **68 tubes** remain |

→ [ICD_DRONE_RADAR.md](ICD_DRONE_RADAR.md) · [MKFS_CORE_ENHANCEMENTS.md](MKFS_CORE_ENHANCEMENTS.md)

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial five CONOPS vignettes |

# MKFS Magazine Economics

**Document ID:** MKFS-DOC-ECON-001  
**Version:** 0.1 (Phase 5 — ROM estimates)  
**Related:** [SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md) | [POD_MECHANISM_SPEC.md](../prototypes/array/POD_MECHANISM_SPEC.md) | [MKFS-ADP-STRYKER-A.md](adapters/MKFS-ADP-STRYKER-A.md)

> **All cost figures are ROM placeholders** for concept planning — not quotes or program baselines.

---

## 1. Tubes and Flechettes per Package

| Package | Face size | Tubes | Flechettes per salvo | Notes |
|---------|-----------|-------|----------------------|-------|
| Appliqué strip | 2×1 ft | 136 | 13,600 | Stryker hull / bustle |
| Appliqué strip | 3×1 ft | 208 | 20,800 | Extended coverage |
| Turret deck | 2×2 ft | 289 | 28,900 | One pan-tilt head deck |
| Turret magazine | 2×2 ft × 3 | 867 | 86,700 | Full dump — LAST_DITCH_FULL |
| Turret magazine | 2×2 ft × 4 | 1,156 | 115,600 | Max depth concept |

**Per puck:** ~100 Ti flechettes @ 1.3 g (see [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md))

---

## 2. Salvo Density @ 350 ft (from model)

| Package | Hits/m² @ 350 ft |
|---------|------------------|
| 2×1 strip (136) | **310** |
| 3×1 strip (208) | **474** |
| Turret 1 deck (289) | **659** |
| Turret 3-deck dump (867) | **1,977** |

Pattern footprint: **~24.5 ft** diameter at 350 ft (single salvo cone).

---

## 3. Example Loadout — Stryker ICV (Dual 2×1 Strips)

From [MKFS-ADP-STRYKER-A.md](adapters/MKFS-ADP-STRYKER-A.md): **2 modules** (forward/aft roof).

| Metric | Value |
|--------|-------|
| Total tubes | 272 |
| Flechettes per dual-salvo | 27,200 |
| Combined hits/m² @ 350 ft *(model: 2 overlapping cones)* | **620+** *(same cone — dual face coverage)* |
| Full-dump salvos before reload | **1** per pod |
| Spare pods stowed *(concept)* | 2–4 per vehicle |

**Engagement budget:** One dual-strip LAST_DITCH_FULL = one terminal window. Second swarm requires **pod swap** (~5 min, 2 crew — [POD_MECHANISM_SPEC.md](../prototypes/array/POD_MECHANISM_SPEC.md)).

---

## 4. Reload Doctrine (Concept)

| Event | Time *(target)* | Crew |
|-------|-----------------|------|
| Pod swap (136-tube strip) | < 5 min | 2 |
| Turret deck reload *(future)* | TBD | 1–2 |
| FCU RELOAD → STANDBY | Automatic on pod RFID confirm | — |

**Under fire:** Remaining tile/turret covers sector while crew swaps empty pod — see [RELOAD_UNDER_FIRE.md](visual/RELOAD_UNDER_FIRE.md).

---

## 5. Cost ROM *(Placeholders)*

| Item | ROM unit cost | Basis |
|------|---------------|-------|
| MKFS puck cartridge | **$80–$150** | Ti flechettes + case + primer; volume-dependent |
| 2×1 loaded pod (136) | **$11K–$20K** | 136 × puck ROM + pod hardware |
| 3×1 loaded pod (208) | **$17K–$31K** | Scale linear |
| Turret 3-deck load (867) | **$70K–$130K** | Magazine + pucks |

### Compare — Notional Interceptor Economics

| Effector | ROM per engagement | Swarm handling | Notes |
|----------|-------------------|----------------|-------|
| MKFS dual-strip salvo | **$11K–$20K** *(consumes pod)* | Volume cloud | Kinetic only |
| Short-range missile | **$100K–$500K+** | 1–2 targets | Logistics heavy |
| EW/jamming suite | **$500K+** *(system)* | Soft kill; degraded vs autonomous | Power + spectrum |
| DEW shot | **$1–50** *(energy)* | 1 target; weather limited | High capital cost |

MKFS trades **per-shot cost** for **magazine mass** and **reload time** — appropriate for last-ditch, not sustained BMD.

---

## 6. Key Takeaways

1. **Economics favor volume** — puck is cheap vs missile; tile count drives magazine cost  
2. **One salvo = one pod** on strip mounts — plan stowage for 2+ reloads  
3. **Turret depth** buys multiple terminal engagements without vehicle return-to-base  
4. **Reload under fire** is the operational bottleneck, not flechette physics  

---

## 7. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial ROM magazine economics |

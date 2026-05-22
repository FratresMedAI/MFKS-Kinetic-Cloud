# MKFS Puck Release — Hollow-Point Cloud Mechanism

**Document ID:** MKFS-DOC-RELEASE-001  
**Version:** 0.1  
**Related:** [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md) | [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) | [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md)

---

## 1. Design Fusion *(What We’re Building)*

One strip that combines the **best ideas** from things that already kill things in the air — **without explosives**:

| DNA | What we take | MKFS expression |
|-----|--------------|-----------------|
| **CIWS** | Volume fire into the terminal window; don’t miss | Full strip dump — hundreds of pucks in seconds |
| **30 mm grenade** | Caliber class, terminal effect | **31 mm** puck — same width, **¼ the length** |
| **Half dollar / hockey puck** | Flat, stackable, dense tubes | Tile battery layout |
| **00 buckshot** | Pattern spread, many killers per trigger | **35+ sub-projectiles per puck** |
| **Hollow point** | Opens from the front; speed + drag do the work | **Skirt peels → cloud spreads** — no fuze |

**One sentence:** A **CIWS-rate kinetic buckshot strip** that **eviscerates a volume of sky** in the terminal band so drone swarms don’t finish the vehicle.

---

## 2. Hollow-Point Puck — How Release Works

No electronic fuze. No HE. The puck **opens like a hollow-point bullet** — shaped from the factory to **want** to peel — and **speed + air drag** finish the job.

### Sequence

```mermaid
flowchart LR
  LAUNCH[Launch_setback] --> FLIGHT[Supersonic_flight]
  FLIGHT --> PEEL[Skirt_peels_open]
  PEEL --> DRAG[Drag_accelerates_spread]
  DRAG --> CLOUD[Buckshot_flechette_cloud]
```

1. **Launch** — Electric primer; puck exits tube at **850–950 m/s**. Setback loads the nose/skirt interface.  
2. **Flight** — Puck flies stable (short ogive nose). Mechanical latch holds skirt closed until release condition.  
3. **Peel** — At **`R_open`** (~200 ft): setback-preloaded petals **or** aerodynamic pressure on scored skirt exceeds retention → **skirt mushrooms backward** (hollow-point behavior).  
4. **Spread** — Open skirt = **massive drag asymmetry** + forward body continues → sub-projectiles (flechettes / buckshot-class pellets) **shear out radially**.  
5. **Cloud** — Each puck = mini **00 buck** burst. **Full strip** = hundreds of overlapping bursts → **terminal volume saturation**.

### Why Puck Shape Enables This

| Shape | Advantage |
|-------|-----------|
| **Flat / wide nose** | Hollow-point ogive — designed to peel, not pierce armor |
| **Short body** | Stable in tube; opens quickly once skirt fails |
| **Scored skirt** | Stress concentrators — peel at predictable G / pressure |
| **No long fuze train** | Opening tied to **mechanics + physics**, not a clock |

**The mechanism and the speed and the drag spread the cloud.** Same philosophy as a hollow point: **geometry + velocity + air** — not chemistry.

---

## 3. Sub-Projectile Payload *(The “00 Buck” Layer)*

Each puck releases a **shot column** — not one killer, a **cluster**:

| Parameter | Target |
|-----------|--------|
| Sub-projectiles per puck | **35–45** |
| Individual mass | **0.5–0.9 g** *(00 buck ~3.5 g — we use more, lighter, faster flechettes)* |
| Material | Ti-6Al-4V or tungsten composite |
| Release | Radial + forward cone as skirt peels |
| Role | Structural kill on Class 1–2 UAS — motor, wing, battery |

One puck = one **buckshot pattern**. One **2×1 ft strip** (~136 pucks) = **~4,800+** sub-projectiles in the terminal window.

---

## 4. Terminal Kill Volume *(“Eviscerate the Sky”)*

### Single puck

One puck fills a **small cone** — tens of feet across at 350 ft downrange. Fine for one drone; not the swarm answer.

### Full strip salvo (`LAST_DITCH_FULL`)

All tubes in a tile (or linked tiles) — **electronic fire** — overlapping clouds merge:

| Parameter | Design target *(salvo-level)* |
|-----------|-------------------------------|
| Downrange depth | **~200–500 ft** terminal band |
| Lateral spread | **Grows with range** — merged cones from 136+ pucks |
| Vertical fill | Elevation fan from tile mount + cloud spread |
| Combined effect | **Saturation** — “nothing flies through this corridor” |

**500 ft radius** is the **aspirational terminal kill volume** for a **full battery dump** (multiple tiles, full tube count) — the **combined** overlapping buckshot clouds filling a large sector of sky ahead of the vehicle. Physics validation required; single puck does not clear a 500 ft radius alone.

```
        Vehicle
           │
    [tile strip fires]
           │
           ▼
      ╱────────╲     ← individual puck cones
     ╱  ╱╱╱╱╱╱  ╲
    ╱  ╱ MERGED ╲  ← full salvo = saturated volume
   ╱  ╱  CLOUD   ╲    ~200–500 ft deep, wide cone
  ╱──────────────╲
```

---

## 5. Mechanical Release Options *(Puck-Specific)*

Baseline: **Option HP — Hollow-Point Skirt** *(evolves Option D setback)*

| Stage | Mechanism |
|-------|-----------|
| Arming | Launch setback pre-stresses scored skirt |
| Release trigger | Setback threshold **or** dynamic pressure at `R_open` airspeed |
| Opening | Skirt petals peel aft — hollow-point mushroom |
| Dispersal | Drag + centrifugal shedding of flechette column |

**No explosives.** Retention spring preload sets band index (short / standard / long `R_open`).

Alternates in [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) remain valid; **HP skirt is baseline for puck form.**

---

## 6. Why Electronic Fire Completes the Picture

Hollow-point pucks spread **per round**. Electronic fire **orchestrates** the strip:

| Mode | Effect |
|------|--------|
| `LAST_DITCH_FULL` | Every tube — **sky evisceration** — now |
| Sector | Left/right/half strip — friendly side clear |
| Ripple | Time-staggered — extend cloud duration |
| Single tube | Test / narrow cone |

CIWS fires a **stream**. MKFS fires a **curtain** — one strip, one button, **kinetic buckshot at scale**.

---

## 7. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Hollow-point puck release; CIWS+buckshot fusion; terminal volume |

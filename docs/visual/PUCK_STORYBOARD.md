# Puck Storyboard — Hollow-Point Puck Release Sequence

**Document ID:** MKFS-VIS-STORY-002  
**Version:** 0.1  
**Status:** Concept | Phase 9  
**Purpose:** Five-frame release sequence for illustrators, animators, and image generation — terminal engagement narrative.  
**Key Decisions:** [D-011](DECISIONS.md) — PUCK-A (drum) in tube; PUCK-B (hollow-point) for peel  
**Open Questions:** Range camera timing validation — see [PUCK_CUTAWAY_STORYBOARD.md](PUCK_CUTAWAY_STORYBOARD.md) §7  
**Related Documents:** [PUCK_CUTAWAY_STORYBOARD.md](PUCK_CUTAWAY_STORYBOARD.md) | [PUCK_RELEASE.md](../PUCK_RELEASE.md) | [CARRIER_PROJECTILE_ICD.md](../CARRIER_PROJECTILE_ICD.md)

---

## Mapping to Existing 6-Frame Cutaway

| This doc | [PUCK_CUTAWAY_STORYBOARD.md](PUCK_CUTAWAY_STORYBOARD.md) | Asset |
|----------|----------------------------------------------------------|-------|
| Frame 1 | Frame 1 — Launch | [mkfs_puck_frame01_launch.png](../../assets/mkfs_puck_frame01_launch.png) |
| Frame 2 | Frame 2 — Flight | [mkfs_puck_frame02_flight.png](../../assets/mkfs_puck_frame02_flight.png) |
| Frame 3 | Frames 3–4 — Setback + Skirt peel | [mkfs_puck_frame04_skirt_peel.png](../../assets/mkfs_puck_frame04_skirt_peel.png) |
| Frame 4 | Frames 5–6 — Drag spread + Cloud | [mkfs_puck_frame06_cloud.png](../../assets/mkfs_puck_frame06_cloud.png) |
| Frame 5 | *(new art — swarm engagement)* | TBD |

Combined sheet: [mkfs_puck_storyboard_6up.png](../../assets/mkfs_puck_storyboard_6up.png)

---

## Frame 1: Puck in Tube (pre-fire)

**Caption:** PUCK-A (Standard Drum) seated in launch tube; electric primer armed; **~40 titanium BBs** stacked in skirt cavity.

**Camera:** Side cutaway, tube chamber — engineering drawing + render mix.

**Callouts:** 31 mm × 28 mm; 850–950 m/s muzzle velocity; kinetic-only — no HE.

![Frame 1 — Puck in tube](../../assets/mkfs_puck_frame01_launch.png)

---

## Frame 2: Ignition / Launch

**Caption:** Primer fires; puck accelerates; setback loads nose/skirt interface; skirt latch holds through supersonic exit.

**Camera:** External side, tube mouth — motion blur on puck tail; minimal vapor.

**Callouts:** t = 0 ms; tube grid context optional (single tube highlight).

![Frame 2 — Launch / flight](../../assets/mkfs_puck_frame02_flight.png)

---

## Frame 3: Skirt Peel + BB Dispersion (first 5–10 m)

**Caption:** At **R_open ≈ 200 ft** (~78 ms), setback exceeds latch; hollow-point skirt petals peel; **titanium BBs** begin radial ejection within **5–10 m** of muzzle.

**Camera:** Cutaway side + front quarter — petals mid-flex, BBs visible in cavity.

**Callouts:** Mechanical release only; 4–6 petal segments; **40 BBs per puck**.

![Frame 3 — Skirt peel](../../assets/mkfs_puck_frame04_skirt_peel.png)

---

## Frame 4: Full Sub-Projectile Cloud (terminal volume)

**Caption:** Drag differential spreads sub-projectiles; cloud reaches **~24.5 ft diameter** at **350 ft**; single puck insufficient — saturation requires multi-tube salvo.

**Camera:** Wide 3/4 — density cone; optional heatmap overlay.

**Callouts:** **~40 titanium BBs per puck**; full **2×2 ft turret dump (867 tubes)** → **~11,500+ sub-projectiles** in terminal volume ([SALVO_SCENARIOS.md](../../research/ballistics/SALVO_SCENARIOS.md)).

![Frame 4 — Terminal cloud](../../assets/mkfs_puck_frame06_cloud.png)

---

## Frame 5: Swarm Engagement Example

**Caption:** Vehicle-mounted MKFS engages close-in FPV swarm at **250–400 ft** — dense kinetic cloud vs multiple inbound tracks; last-ditch terminal band.

**Camera:** Overhead or 3/4 — defended asset + inbound swarm silhouettes + cloud footprint.

**Callouts:** LAST_DITCH profile; operator ARMED; co-mounted sensor cue on CAN.

*(Art TBD — use Image Prompt 6 below.)*

---

## Image Generation Prompts

Cinematic, technical, defense-concept style: dark background, high contrast, blueprint linework + photoreal render. Subtle **"MFKS Kinetic Cloud"** watermark lower-right, 15% opacity.

### Prompt 1 — Puck in tube cutaway

> Technical cutaway of MKFS half-dollar puck (31mm titanium cartridge) inside launch tube, PUCK-A drum form, stacked titanium BBs visible in hollow skirt cavity, electric primer at base, dark navy background, cyan blueprint annotation lines, photoreal metal textures, defense engineering concept art, no explosives, subtle "MFKS Kinetic Cloud" watermark.

### Prompt 2 — Skirt peel moment

> Side view MKFS hollow-point puck PUCK-B mid-skirt-peel, titanium skirt petals opening radially, titanium BBs dispersing from cavity, motion blur on petals, first 5-10 meters after muzzle, dark high-contrast defense render mixed with blueprint schematic overlay, kinetic-only no explosion flash, "MFKS Kinetic Cloud" watermark.

### Prompt 3 — Full cloud saturation

> Wide cinematic shot: dense titanium BB sub-projectile cloud filling terminal volume of sky, ~24ft pattern footprint at 350ft range, faint FPV drone swarm silhouettes entering cloud, dark stormy sky, high contrast, blueprint grid overlay, defense concept art, volume saturation not precision shot, "MFKS Kinetic Cloud" watermark.

### Prompt 4 — Pan-tilt turret firing sequence

> Stage-light style pan-tilt yoke turret on JLTV roof, observatory shutters open, 2x2ft tube grid firing sector salvo, multiple muzzle flashes sequential, dark tactical environment, blueprint + render hybrid, MKFS modular kinetic defense, "MFKS Kinetic Cloud" watermark.

### Prompt 5 — Appliqué tile strip on Stryker

> Side hull view Stryker ICV with low-profile MKFS 2x1ft appliqué tile strips mounted on roof bustle, clean armor integration no giant turret, tube grid visible from slight angle, dark olive drab vehicle, technical defense illustration, blueprint dimension callouts, "MFKS Kinetic Cloud" watermark.

### Prompt 6 — Terminal engagement

> Overhead 3/4 view armored vehicle with dense kinetic cloud engaging incoming FPV drone swarm at close range 300ft, terminal last-ditch engagement, titanium BB saturation volume, dark high-contrast cinematic defense concept, no missiles no explosions in round, "MFKS Kinetic Cloud" watermark.

---

## Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-24 | Five-frame storyboard + image prompts; links to 6-up cutaway assets |

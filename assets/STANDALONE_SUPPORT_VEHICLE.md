# MKFS Standalone Support Vehicle

**Asset:** [mkfs_standalone_support_vehicle.png](mkfs_standalone_support_vehicle.png)  
**Reference:** [reference_himars_style_launcher.png](reference_himars_style_launcher.png) *(user-provided MLRS/HIMARS-style layout)*  
**Related:** [MOUNTING_CONCEPT.md](MOUNTING_CONCEPT.md) | [DESIGN_PHILOSOPHY.md](../docs/DESIGN_PHILOSOPHY.md)

---

## Concept

A **dedicated support vehicle** — same role family as HIMARS/MLRS or short-range air defense carriers — but firing **MKFS kinetic puck batteries** instead of missiles or HE.

| HIMARS-style reference | MKFS support vehicle |
|------------------------|----------------------|
| 6×6 tactical truck | Oshkosh FMTV / similar **6×6** |
| Box of large missile tubes | **Flat dense puck tube grid** (linked 3×1 ft tiles) |
| Rocket motor exhaust | **Electric-primer puck launch** — short impulse, no rocket plume |
| Area fires / support | **Terminal swarm saturation** for convoys / fixed sites |

---

## Vehicle Configuration

| Element | Spec |
|---------|------|
| Chassis | 6×6 medium tactical *(FMTV-class, Oshkosh)* |
| Cab | 2–3 crew + FCU operator |
| Launcher | Hydraulic **tilt/elevate** bed — 0° to +70° |
| Launcher face | **4–8 linked MKFS tiles** → **800–1,600+ tubes** |
| Reload | Tile row pods from rear; crane or manual strip swap |
| Mobility | Self-deploy; supports maneuver units from standoff |

**Designator (concept):** `MKFS-SV-6x6` — Standalone Support Vehicle

---

## Mission Roles

| Role | Description |
|------|-------------|
| **Convoy umbrella** | Escorts columns — `LAST_DITCH_FULL` on swarm contact |
| **Fixed site defense** | FOB / bridge / assembly area terminal layer |
| **Forward support** | Paired with maneuver — not embedded on every IFV |
| **Naval littoral** *(future)* | Same launcher module on littoral combat craft |

Unlike **appliqué tiles** on Stryker/JLTV, this vehicle **is** the battery — maximum tube count, one job: **eviscerate the terminal volume**.

---

## Launcher Layout *(Concept)*

```
  Side view — elevated for engagement

        ○ ○ ○ ○ ○ ○ ○ ○ ○ ○   ← dense puck tube grid
       [  MKFS tile array   ]  ← 4–6× 3×1 ft tiles, one face
      ╱                       ╲
     ╱    hydraulic tilt       ╲
    ════════════════════════════  truck bed
         [ 6×6 chassis ]
```

- **Electronic fire:** full face, sector, or ripple — same FCU architecture as mounted tiles  
- **Same puck:** `MKFS-CART-PUCK` — hollow-point release, no HE  

---

## Comparison to Attached Reference

User reference shows a **tilted rectangular cell grid** on a desert tan truck firing a missile. MKFS standalone vehicle **mirrors that silhouette and support role** but:

- Cells are **small** (31 mm pucks, not missiles)  
- Grid is **much denser** (hundreds of tubes)  
- Effect is **kinetic buckshot curtain**, not explosive intercept  

---

## Disclaimer

Concept illustration only. Launcher dimensions, tube count, and chassis selection require engineering trade study.

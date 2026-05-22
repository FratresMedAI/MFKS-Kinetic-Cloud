# MKFS Mounting Concept Render

**Asset:** [mkfs_mounting_concept_stryker_jltv_usv.png](mkfs_mounting_concept_stryker_jltv_usv.png)  
**Type:** Concept illustration — not engineering drawing  
**Related:** [DESIGN_PHILOSOPHY.md](../docs/DESIGN_PHILOSOPHY.md) | [VEHICLE_INTEGRATION.md](../docs/VEHICLE_INTEGRATION.md)

---

## What the Render Shows

Low-profile **MKFS tile strips** (flat tube batteries, ~2×1 ft / 3×1 ft) mounted **flush** on:

| Platform | Mount faces |
|----------|-------------|
| **Stryker ICV** | Turret bustle, hull sides |
| **Oshkosh JLTV** | Roof edges, rear hull *(representative of new Oshkosh light tactical fleet)* |
| **USV conning tower** *(concept)* | Tower faces — unmanned surface vessel kinetic defense vs low flyers |

Tiles appear as **thin panels with dense tube grids** — same form factor as the tube-battery reference, not box launchers.

---

## Land Vehicles

### Stryker

- Tiles on **turret bustle** and **port/starboard hull** — dual coverage without roof towers  
- Kit: `MKFS-ADP-STRYKER-A` — see [adapters/MKFS-ADP-STRYKER-A.md](../adapters/MKFS-ADP-STRYKER-A.md)

### Oshkosh JLTV / Light Tactical Fleet

Army **JLTV** and related Oshkosh tactical vehicles share constraints: limited roof, need low silhouette.

| Mount | Tiles |
|-------|-------|
| Rear bustle | 1–2× **3×1 ft** |
| Roof rear corners | 2× **2×1 ft** |
| Optional hull sides | **2×1 ft** strips |

Future adapter: `MKFS-ADP-JLTV-A` *(not yet detailed — same tile interface as Stryker)*.

Other Oshkosh platforms (FMTV, eJLTV, CBTT-class trucks) use the **same tile** — adapter plate only changes.

---

## Naval — Unmanned Ship Conning Tower *(Concept)*

**In theory:** MKFS tiles **line the conning tower** (or mast structure) of **unmanned surface vessels (USVs)** for **kinetic terminal defense** against:

- Low-flying UAS  
- Suicide drones  
- Possibly incoming small arms / low-angle air threats in the terminal window  

| Consideration | Notes |
|---------------|-------|
| Environment | Salt spray, corrosion — Ti/stainless tube bores, sealed electronics |
| Motion | Sea pitch/roll — fixed elevation tiles, FCU compensates with sector fire |
| Coverage | Tiles on **four faces** of tower → 360° terminal cone |
| Power | Ship 28 VDC bus; FCU integration with USV autonomy stack |
| Role | Same **last-ditch** doctrine — kinetic buckshot curtain, no HE |

**Out of baseline scope** for Phase 0–4 land-vehicle program — documented as **future maritime variant** sharing `MKFS-CART-PUCK` and tile architecture.

Adapter concept: `MKFS-ADP-USV-TOWER` — conformal curved tiles on tower facets.

---

## Disclaimer

Render is **artistic concept only** — proportions, tile count, and mount locations require engineering validation against actual vehicle CAD and clearance envelopes.

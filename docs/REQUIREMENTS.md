# MKFS System Requirements

**Document ID:** MKFS-DOC-REQ-001  
**Version:** 0.2 (design intent revision)  
**Related:** [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) | [SYSTEM_ARCHITECTURE.md](architecture/SYSTEM_ARCHITECTURE.md) | [VEHICLE_INTEGRATION.md](VEHICLE_INTEGRATION.md) | [DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) | [current_tasks.md](../tasks/current_tasks.md)

---

## 1. Purpose

Define functional and non-functional requirements for the Modular Kinetic Flechette System (MKFS), a **last-ditch, vehicle-mounted terminal defense** capability — kinetic analogue of hard-kill APS against **close-in drone swarms**. See [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md).

---

## 2. Scope

MKFS covers:

- **Half-dollar-class puck** carriers with mechanical flechette deployment
- **Low-profile symmetrical tiles** (2×1, 3×1, N×1) — turret, hull, roof mount
- **Electronic per-tube fire** — scales to 200+ tubes per vehicle
- Vehicle adapter kits for U.S. APC/IFV/recon fleets

Out of scope for baseline design:

- Explosive warheads or electronic fuzes in the round
- Wired or wireless guidance of individual projectiles
- Beyond-line-of-sight or precision single-target engagement

---

## 3. Design Constants

| Constant | Symbol | Value | Notes |
|----------|--------|-------|-------|
| Cloud open distance | `R_open` | ~200 ft (61 m) | Mechanical deployment initiates |
| Primary damage band | `R_band` | 250–500 ft (76–152 m) | Maximum flechette cloud effectiveness |
| Max engagement range | `R_max` | ~500 yd (457 m) | Terminal defense envelope |
| Design muzzle velocity | `V_0` | 900 m/s (2,953 ft/s) | Puck nominal; tile salvo |
| Baseline tile | — | **2×2 ft** (610×610 mm) | One standard module face |

---

## 4. Functional Requirements

### Effector and Projectile

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| FR-001 | System shall use **purely kinetic** effectors with **no explosives** in the projectile, payload, or deployment mechanism | Design review confirms zero energetic materials in round; deployment is mechanical only |
| FR-002 | Carrier projectile shall deploy a flechette / sub-projectile cloud via **mechanical range-band or timer-based** release | Cloud opens at `R_open`; lethal pattern peaks within `R_band`; baseline mechanism: Option D setback release ([DEPLOYMENT_MECHANISM.md](DEPLOYMENT_MECHANISM.md) §8) |
| FR-003 | Baseline engagement shall target **drone swarms** at **area/volume** effect in **last-ditch** scenarios | Multi-tube salvo density sufficient; vehicle survival prioritized over single-target precision |
| FR-004 | Maximum effective engagement range shall not exceed **~500 yards** | Ballistics model and test data confirm pattern utility out to `R_max` |
| FR-005 | Projectile shall contain **no wired guidance** in baseline configuration | No trailing wire, no in-round RF transceiver |
| FR-013 | System shall operate as **terminal “don’t die” defense** when primary AD is absent or defeated | Documented in [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md); FCU `LAST_DITCH` preset |

### Launcher and Tiles

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| FR-006 | Launcher shall use **2 ft × 2 ft modular boxes** with dense puck tube grid | Face 610×610 mm; ~289 tubes; [ARRAY_MODULE_SPEC.md](../prototypes/array/ARRAY_MODULE_SPEC.md) |
| FR-007 | System shall support **high-volume salvo** from **individually addressed tubes** | FCU selects any tube subset; full 200-tube dump ≤ 2 s |
| FR-008 | Tiles shall support **row or tile reload** without removing mount from vehicle | Reload per tile/row spec |
| FR-009 | Fire control shall provide **electronic tube selection and salvo timing** — **this is core, not optional** | Every tube addressable; round remains passive/mechanical |

### Coverage and Integration

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| FR-010 | Vehicles shall mount **multiple tiles** on turret cheeks, hull sides, and/or roof for overlapping coverage | Layout per platform; not limited to roof boxes — [VEHICLE_INTEGRATION.md](VEHICLE_INTEGRATION.md) |
| FR-011 | System shall integrate on **Stryker, M2 Bradley, M113, LAV-25, MRAP, and recon vehicles** via thin adapter plates | Adapter kit per platform; conformal mount |
| FR-012 | Scale by **linking 2×2 ft boxes** — not new form factors | Symmetric edge interface MKFS-IF-002 |

---

## 5. Non-Functional Requirements

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| NFR-001 | **Modularity** — Same projectile family and array architecture across all platforms | Single cartridge interface (MKFS-IF-001); adapter-only vehicle differences |
| NFR-002 | **Fleet compatibility** — Minimal modification to existing U.S. APC/IFV fleets | Mounting via adapter plate; no structural hull cuts in baseline |
| NFR-003 | **Safety** — Launcher electronics isolated from round; round is inert until fired | No stored energy in unfired round beyond mechanical spring pre-load (bounded) |
| NFR-004 | **Maintainability** — Field-replaceable pods and adapter subcomponents | MTTR targets defined in Phase 4 |
| NFR-005 | **Environmental** — Operable in -25°F to 125°F (-32°C to 52°C) vehicle combat envelope | Mechanism functions across temperature band with documented drift |
| NFR-006 | **Logistics** — Common cartridge across all vehicle types | Single NSN family for projectile; adapter kits vehicle-specific |

---

## 6. Constraints

| ID | Constraint |
|----|------------|
| C-001 | **No explosives** anywhere in the round — kinetic energy and mechanical deployment only |
| C-002 | **No electronic fuze** in the projectile — deployment timing purely mechanical |
| C-003 | **No in-round power** — projectile has no battery or active electronics |
| C-004 | **Existing fleet** — Designed for in-service Stryker, Bradley, M113, LAV-25, MRAP platforms |
| C-005 | **Terminal / last-ditch** — Fires when swarm is close; survival layer like APS, not replacement for SHORAD |
| C-006 | **Low profile** — Tiles lay on armor; avoid tower mounts that defeat vehicle silhouette |

---

## 7. Modularity Interface Standards

### MKFS-IF-001: Puck / Cartridge Physical Interface

| Parameter | Specification |
|-----------|---------------|
| Cartridge family | `MKFS-CART-PUCK` |
| Diameter | **31 mm** (half-dollar class) |
| Length (OAL) | **28 mm** |
| Mass (loaded) | 55–75 g |
| Interface type | Straight wall; electric primer (launcher-initiated only) |
| Deployment selector | Mechanical band index (3 positions) |
| Tube bore | 33 mm |

### MKFS-IF-002: Module Interface — **2×2 ft Box**

| Parameter | Specification |
|-----------|---------------|
| Standard module | **`MKFS-MOD-2x2`** — **2 ft × 2 ft** (610 × 610 mm) square face |
| Tube grid | **17 × 17 ≈ 289 tubes** @ 35 mm pitch |
| Profile (appliqué) | **≤ 150 mm** |
| Depth (observatory turret) | **Multi-deck** — stacked 2×2 faces, multiple salvos |
| Edge interface | Symmetric — link additional **2×2 ft** modules |
| Tube addressing | 12-bit ID via FCU |

### MKFS-IF-003: Vehicle Adapter Plate Standard

| Parameter | Specification |
|-----------|---------------|
| Adapter plate | Thin conformal plate; follows turret/hull curvature option |
| Bolt pattern | 4× M8 min per **2×2 ft** module corner pattern |
| Height above surface | **≤ 150 mm** total tile profile |
| Load rating | 200 kg per array module including dynamic firing loads |
| Electrical pass-through | Single MIL-DTL-38999 Series III connector (FCU to module) |
| Adapter kit naming | `MKFS-ADP-{PLATFORM}-A` |

### MKFS-IF-004: Power / Data Fire-Control Connector (Launcher Side)

| Parameter | Specification |
|-----------|---------------|
| Connector | MIL-DTL-38999 Series III, 19-pin |
| Power | 28 VDC nominal (18–32 V); ≤ 150 W peak per module |
| Data | CAN 2.0B @ 500 kbps — see [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md) |
| Ground | Vehicle chassis ground via adapter plate |
| Separation | Round has **no** connection to this interface |

---

## 8. Phase Acceptance Criteria

### Phase 0 — Foundation (Complete)

- [x] System name and high-level requirements finalized
- [x] Vehicle integration matrix for all five platform families
- [x] Mechanical deployment mechanism options documented
- [x] Modularity rules and interface standards (MKFS-IF-001 through 004) established

### Phase 1 — Core Technology (In Progress)

- [ ] Carrier projectile design baseline
- [x] Range-band timing validated at `V_0` = 900 m/s
- [x] Initial ballistics and flechette pattern model for `R_band`
- [x] Deployment mechanism down-select (see [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md))

### Phase 2 — Array Prototype

- [ ] ~2×2 ft multi-tube array module detailed design
- [ ] Electronic initiation and salvo control logic specification
- [ ] Modular mounting interface (MKFS-IF-002) validated

### Phase 3 — Vehicle Integration

- [ ] Vehicle-specific adapter kit designs for all platforms
- [ ] Dual-array 360° coverage layout per vehicle
- [ ] Power, sensor, and fire-control interface requirements finalized

### Phase 4 — Documentation and Next Steps

- [ ] Full system specification (MKFS-DOC-SPEC-001)
- [ ] Prototype roadmap and risk register
- [ ] Manufacturing and test plan

---

## 9. Terminology

| Term | Definition |
|------|------------|
| **Carrier projectile** | Lightweight high-velocity round that houses and mechanically releases the flechette cloud |
| **Flechette cloud** | Dispersed pattern of titanium sub-projectiles released at preset range |
| **Array module** | Multi-tube launcher box (~2×2 ft baseline) |
| **Adapter kit** | Vehicle-specific mounting hardware (`MKFS-ADP-*`) |
| **Range band** | Preset distance window (`R_open` to `R_band`) for cloud deployment |
| **Quick-swap pod** | Reloadable tube bundle removed as a unit |

---

## 10. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 0 initial release |

# MKFS-ADP-STRYKER-A — Stryker Adapter Kit

**Status:** Concept | Phase 9
**Purpose:** Vehicle-specific adapter kit drawing set and mount layout.
**Key Decisions:** See [../DECISIONS.md](../DECISIONS.md)
**Open Questions:** See [../RISK_REGISTER.md](../RISK_REGISTER.md)

**Kit ID:** `MKFS-ADP-STRYKER-A`  
**Platforms:** Stryker ICV, CV, MGS, and related 8×8 variants  
**Document ID:** MKFS-ADP-STRYKER-001

---

## 1. Kit Contents

| Part No. | Description | Qty |
|----------|-------------|-----|
| ADP-PLT-800 | Standard adapter plate (MKFS-IF-003) | 2 |
| ADP-RSR-200 | 200 mm riser block (ICV/CV) | 2 |
| ADP-RSR-150 | 150 mm low riser (MGS) | 2 |
| ADP-FAIR-STR | Aerodynamic fairing shell | 2 |
| ADP-HRN-STR | Power/data harness, 2 m | 2 |
| ADP-BOLT-M12 | M12×1.75 mounting bolt kit | 16 |
| ADP-FCU-BKT | FCU mounting bracket (troop compartment) | 1 |

---

## 2. Mounting Locations

### ICV/CV (Standard Tier × 2)

| Module | Position | Coordinates *(from hull center)* | Riser |
|--------|----------|----------------------------------|-------|
| Forward | Fore roof, port of centerline | X: +1.8 m, Y: 0 | 200 mm |
| Aft | Aft roof, starboard of centerline | X: -1.6 m, Y: 0 | 200 mm |

Clearance: modules outside 60° RWS dead zone aft.

### MGS (Compact Tier × 2)

| Module | Position | Notes |
|--------|----------|-------|
| Port | Mid-roof, port sponson | Outside 105 mm gun arc |
| Starboard | Mid-roof, starboard sponson | 150 mm riser |

---

## 3. Structural Interface

| Parameter | Value |
|-----------|-------|
| Roof attachment | 4× M12 through-bolt to reinforced plate |
| Reinforcement | 6 mm steel spreader plate under roof skin *(if required)* |
| Load per module | 200 kg static / 300 kg dynamic (firing) |
| Shock | Rubber isolators in riser (20 durometer) |

---

## 4. Electrical Routing

- Harness exits port side of each module → roof cable tray → troop compartment FCU
- 28 VDC tap: NATO slave receptacle or direct bus (vehicle config dependent)
- Fuse: 20 A per module circuit

---

## 5. Installation Drawing Notes

```
        [FWD ARRAY]          RWS          [AFT ARRAY]
            |                 |                |
    --------+--------+--------+--------+-------
            |   riser  |  dead  |  riser   |
            |   200mm  |  zone  |  200mm   |
```

Elevation default: +15° for ICV/CV; +20° for MGS (gun clearance).

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 3 initial drawing set |

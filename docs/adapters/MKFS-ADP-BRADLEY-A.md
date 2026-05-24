# MKFS-ADP-BRADLEY-A — Bradley Adapter Kit

**Status:** Concept | Phase 9
**Purpose:** Vehicle-specific adapter kit drawing set and mount layout.
**Key Decisions:** See [../DECISIONS.md](../DECISIONS.md)
**Open Questions:** See [../RISK_REGISTER.md](../RISK_REGISTER.md)

**Kit ID:** `MKFS-ADP-BRADLEY-A`  
**Platform:** M2 Bradley IFV  
**Document ID:** MKFS-ADP-BRADLEY-001

---

## 1. Kit Contents

| Part No. | Description | Qty |
|----------|-------------|-----|
| ADP-PLT-800 | Standard adapter plate | 2 |
| ADP-RSR-250 | 250 mm riser (TOW/cupola clearance) | 2 |
| ADP-RING-EXT | Turret ring clearance extension | 2 |
| ADP-FAIR-BRD | Bradley fairing | 2 |
| ADP-HRN-BRD | Harness with 1553 tap option | 2 |
| ADP-SHOCK | Track shock mount kit | 2 |
| ADP-FCU-BKT | FCU bracket (turret bustle) | 1 |

---

## 2. Mounting Locations

| Module | Position | Coverage Arc |
|--------|----------|--------------|
| Forward | Roof forward of TOW, outside turret ring | 330°–150° |
| Aft | Engine deck aft of turret ring | 150°–330° |

Both modules: **Standard tier (25-tube)** per D-004.

---

## 3. Clearance Envelope

| Obstruction | Clearance Required | Module Solution |
|-------------|-------------------|-----------------|
| TOW launcher | 400 mm vertical | 250 mm riser + fairing notch |
| Commander cupola | 360° rotation | Mount outside 1.5 m ring |
| 25 mm gun | ±30° elevation | Module max +60° independent |

---

## 4. Structural

| Parameter | Value |
|-----------|-------|
| Roof load | 110 kg combined (both modules + pods) |
| CG shift | ≤ 45 mm lateral, ≤ 35 mm vertical |
| Track shock mounts | 4× isolator per module (cross-country) |

---

## 5. C4ISR

- FCU interfaces with Bradley FBCB2 via Ethernet gateway (optional kit ADP-C4-BRD)
- Threat cue from CIV / RWS when available

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 3 initial drawing set |

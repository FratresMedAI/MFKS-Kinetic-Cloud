# MKFS Sensor Integration Requirements

**Document ID:** MKFS-ICD-SENS-001  
**Version:** 0.1 (Phase 3)  
**Decision D-005:** **Vehicle sensors baseline; optional swarm sensor kit**  
**Related:** [SYSTEM_ARCHITECTURE.md](architecture/SYSTEM_ARCHITECTURE.md) | [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md)

---

## 1. Sensor Architecture

```mermaid
flowchart LR
  RWS[VehicleRWS_EOIR]
  RAD[VehicleRadar_Opt]
  SWARM[MKFS_SwarmKit_Opt]
  FCU[FCU]
  RWS --> FCU
  RAD --> FCU
  SWARM --> FCU
```

---

## 2. Baseline — Vehicle Sensors

| Source | Data | Interface | Latency Target |
|--------|------|-----------|----------------|
| RWS EO/IR | Bearing, elevation, video track | Ethernet or RS-170 | < 500 ms |
| Vehicle GPS/INS | Platform position, heading | CAN or 1553 | < 100 ms |
| Commander manual | Azimuth/elevation entry | FCU panel | Immediate |

**Baseline configuration:** No dedicated MKFS sensor required. FCU accepts manual cue or RWS track if vehicle provides export.

---

## 3. Optional — MKFS Swarm Sensor Kit (`MKFS-SENS-SWARM-OPT`)

| Parameter | Specification |
|-----------|---------------|
| Type | Compact X-band FMCW radar *(conceptual)* |
| Coverage | 360°, 30° elevation, 50–800 yd |
| Track capacity | 32 simultaneous |
| Mass | ≤ 15 kg |
| Power | 75 W avg, 120 W peak |
| Mount | Adapter mast (MRAP kit included; others optional) |
| Interface | CAN 0x300 TRACK messages |

**Decision D-005:** Optional kit — not required for baseline vehicle integration. Recommended for convoy/MRAP missions without organic air defense cueing.

---

## 4. Track Fusion (FCU Software)

| Priority | Source | Use |
|----------|--------|-----|
| 1 | Swarm sensor (if fitted) | Primary auto-track |
| 2 | Vehicle radar track | Secondary auto-track |
| 3 | RWS manual track | Tertiary |
| 4 | Manual FCU entry | Fallback |

Stale track (> 500 ms) → hold fire, alert operator.

---

## 5. Integration by Platform

| Platform | Baseline Cue | Optional Kit Mount |
|----------|--------------|-------------------|
| Stryker | RWS (CROWS) | Adapter mast on forward plate |
| Bradley | CIV / RWS | Turret bustle mast |
| M113 | Manual / external | Not recommended (power/space) |
| LAV-25 | RWS | Low-profile mast |
| MRAP | CROWS + optional kit | ADP-MAST-OPT included in MRAP kit |

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Baseline vs optional kit defined; D-005 closed |

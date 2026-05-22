# MKFS Power and C4ISR Interface Control Document

**Document ID:** MKFS-ICD-004  
**Interface:** MKFS-IF-004  
**Version:** 0.1 (Phase 3)  
**Decision D-003:** **CAN 2.0B @ 500 kbps** — adopted  
**Related:** [REQUIREMENTS.md](REQUIREMENTS.md) | [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md)

---

## 1. Scope

Defines electrical power and data interfaces between:
- Vehicle platform ↔ FCU
- FCU ↔ Array module(s)
- FCU ↔ Optional C4ISR / sensor systems

**Not in scope:** Projectile/cartridge (no electrical interface).

---

## 2. Power Interface

### 2.1 Vehicle Power Input

| Parameter | Specification |
|-----------|---------------|
| Nominal voltage | 28 VDC (MIL-STD-1275) |
| Operating range | 18–32 VDC |
| Surge / spike | MIL-STD-1275E Type III |
| Input fuse | 30 A time-delay (vehicle side) |
| Ground | Chassis ground via adapter plate |

### 2.2 Power Budget

| State | FCU | Module A | Module B | Total |
|-------|-----|----------|----------|-------|
| Standby | 25 W | 15 W | 15 W | 55 W |
| Armed | 80 W | 40 W | 40 W | 160 W |
| Salvo peak | 80 W | 150 W | 150 W | **380 W** |

Peak duration: ≤ 2 s per salvo. Vehicle shall provide ≥ 400 W allocated capacity.

### 2.3 Module Power Connector

| Parameter | Value |
|-----------|-------|
| Connector | MIL-DTL-38999 Series III, size 17, 19-pin |
| Pin A1–A4 | +28 VDC (4× power) |
| Pin A5–A8 | Return (4× ground) |
| Pin B1–B8 | CAN_H, CAN_L (redundant pair) |
| Pin C1–C4 | Discrete (arm, status, fault) |

---

## 3. Data Interface — CAN Bus

### 3.1 Physical Layer

| Parameter | Value |
|-----------|-------|
| Protocol | CAN 2.0B |
| Bit rate | 500 kbps |
| Termination | 120 Ω at FCU and last module |
| Max modules | 2 arrays + 1 FCU + 1 sensor node |

### 3.2 Message Definitions

| ID | Dir | Name | Payload |
|----|-----|------|---------|
| 0x100 | FCU→MOD | FIRE_CMD | tube_mask[4], inter_ms[2], profile[1] |
| 0x101 | FCU→MOD | AIM_CMD | elev[2], azim[2] |
| 0x102 | FCU→MOD | ARM_CMD | arm_state[1], inhibit_mask[4] |
| 0x200 | MOD→FCU | MOD_STATUS | ready[1], fault[1], pod_count[1], temp[1] |
| 0x201 | MOD→FCU | SALVO_RPT | tubes_fired[4], timestamp[4] |
| 0x300 | SENS→FCU | TRACK | az[2], el[2], range[2], id[2] |
| 0x400 | FCU→C4ISR | ENGAGE_RPT | status[1], module[1], time[4] |

### 3.3 Timing

| Parameter | Value |
|-----------|-------|
| FIRE_CMD to primer | ≤ 5 ms |
| Status refresh | 100 ms |
| Track message max age | 500 ms (stale → hold fire) |

---

## 4. C4ISR Integration (Optional)

| Interface | Protocol | Data |
|-----------|----------|------|
| Vehicle Ethernet | TCP/IP | Threat tracks, position |
| MIL-STD-1553 | Bus bridge | Legacy IFV (Bradley) |
| Disconnected mode | — | Manual FCU azimuth entry |

FCU shall operate fully with no C4ISR connection (local sensor or manual cue).

---

## 5. EMI / EMC

| Standard | Applicability |
|----------|---------------|
| MIL-STD-461G CE102/CS101 | Conducted emissions/susceptibility |
| MIL-STD-461G RE102/RS103 | Radiated |
| MIL-STD-464C | P-static, bonding |

Harness: double-shielded, ≤ 3 m from ignition wiring.

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | CAN adopted; message map defined |

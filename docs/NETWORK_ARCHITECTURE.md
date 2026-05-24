# MKFS Network & C2 Architecture

**Document ID:** MKFS-DOC-NET-001  
**Version:** 0.2 (Phase 9 hardening)  
**Related:** [ICD_POWER_C4ISR.md](ICD_POWER_C4ISR.md) | [ICD_SENSOR_INTEGRATION.md](ICD_SENSOR_INTEGRATION.md) | [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md) | [SWARM_TEST_CONCEPT.md](SWARM_TEST_CONCEPT.md) | [latency_resilience_model.py](../scripts/latency_resilience_model.py) | [DECISIONS.md](DECISIONS.md) D-013

---

## 1. Problem Statement

Distributed terminal defense fails when **multidirectional swarms overload centralized fusion**, and when **TCP/IP links** add packet loss, retransmit storms, head-of-line blocking, and variable latency. At **60 mph**, **250 ms** of stale track data produces **22.0 ft** of uncompensated target motion ([`latency_resilience_output.json`](../scripts/latency_resilience_output.json) `baseline_reference.lead_error_ft`) — sufficient to miss a small UAS before sensor error is counted.

Multi-wave, jam-resistant drone operations (e.g. March 2026 Barksdale AFB) show that **comms resilience precedes terminal effector value**. MKFS is **terminal kinetic** on the defended asset (200–500 yd). It does not replace BLOS cueing or base-wide fusion. This document defines how MKFS **limits dependence on low-latency central links** on the **Tier 1 CAN commit path**.

### TCP/IP limitations

| Failure mode | Effect on terminal engagement |
|--------------|------------------------------|
| Packet loss | Missed or stale tracks; FCU fires on old aim point |
| Retransmit storms | Latency spikes; head-of-line blocking |
| Central fusion saturation | Track updates drop when count exceeds node capacity |
| Single point of failure | One C2 node loss degrades entire sector |

Baseline ICD ([`ICD_POWER_C4ISR.md`](ICD_POWER_C4ISR.md)) documents optional TCP/IP C4ISR and **500 ms stale-track hold-fire**. Phase 9 adds architecture and modeling for overload, loss, and prediction — not fielded hardware.

---

## 2. Design Principle — Tier 1 Commit on CAN Only

**[D-013](DECISIONS.md):** Track-to-primer **SHALL NOT traverse TCP/IP**. C4ISR delivers **mission intent only**; it does not gate `FIRE_CMD`.

```mermaid
flowchart TB
  subgraph tier3 [Tier3_C4ISR_intent]
    C4ISR[C4ISR_TCP_IP_or_1553]
    Intent[MissionIntent_ROE_InhibitZones]
  end
  subgraph tier2 [Tier2_FCU_edge_node]
    FCU[VehicleFCU]
    LocalFusion[LocalTrackFusion_Predictor]
    CAN[CAN_500kbps]
  end
  subgraph tier1 [Tier1_CAN_commit]
    FirePath[FIRE_CMD_le_5ms]
    Modules[ArrayModules_Turret]
  end
  subgraph optional [Optional_adjacent_nodes]
    Gossip[GossipTrackShare]
  end
  C4ISR -->|"intent only"| Intent
  Intent --> FCU
  LocalFusion --> FCU
  CAN --> LocalFusion
  FCU --> FirePath
  FirePath --> Modules
  Gossip <-->|"best effort"| FCU
```

**Tier 1 — CAN commit path (existing ICD):**

1. Co-mounted sensor → CAN `0x300 TRACK`
2. FCU edge node: local fusion + **local predictor** → aim point
3. FCU → CAN `0x100 FIRE_CMD` → primer (≤ 5 ms)

**Tier 2 — FCU edge node:** fusion, triage, prediction, tube selection (milliseconds).

**Tier 3 — C4ISR intent:** sector masks, ROE, authorized profiles, geofence (seconds–minutes; lossy OK).

---

## 3. Hierarchical Intent-Based C2

| Layer | Latency | Content | Link |
|-------|---------|---------|------|
| Tier 3 — mission | Minutes | Area priorities, weapons-free rules | C4ISR |
| Tier 3 — tactical intent | Seconds | Terminal arc, authorized profiles | C4ISR or FCU panel |
| Tier 2 — execution | Milliseconds | Tubes, elevation, **predicted intercept volume** | FCU (CAN) |

Commander or C4ISR sets intent and inhibit zones. FCU executes each track update **without brigade round-trip**. Operator **ARMED** remains required ([`FRATRICIDE_DECONFLICTION.md`](FRATRICIDE_DECONFLICTION.md)).

---

## 4. Edge-Heavy Track Management (Tier 2)

Per [`ICD_SENSOR_INTEGRATION.md`](ICD_SENSOR_INTEGRATION.md) §4:

### 4.1 Fusion priority

| Priority | Source | Use |
|----------|--------|-----|
| 1 | Co-mounted EM/radar (CAN) | Primary auto-track |
| 2 | Vehicle radar | Secondary |
| 3 | RWS manual track | Tertiary |
| 4 | Manual FCU entry | Fallback |

Prefer **CAN-local** sources over TCP/IP when both exist.

### 4.2 Track triage (overload)

When tracks exceed sensor capacity (32 per [`ICD_DRONE_RADAR.md`](ICD_DRONE_RADAR.md)):

1. Closure rate toward defended asset
2. Range (250–500 yd band weighted higher)
3. EM confidence

Engage top-N; coast lower-priority tracks. FCU logs overload; does not fault.

### 4.3 Local predictor

```
Δx ≈ v · τ
σ_pos ≈ sqrt((v·τ)² + (0.5·a_max·τ²)² + (σ_v·τ)²)
```

Aim **predicted intercept volume**, not last report. CV model is minimum spec; Kalman/IMM is implementation target.

---

## 5. Latency Mitigation — Quantitative Grounding

**Key numbers** — source: [`latency_resilience_output.json`](../scripts/latency_resilience_output.json) `baseline_reference`:

| Field | Value |
|-------|-------|
| `lead_error_ft` | **22.0** (60 mph, 250 ms) |
| `pattern_diameter_ft` / `pattern_radius_ft` | **24.5** / **12.3** |
| `pattern_overlap_at_baseline` | **0.0** |
| `predictor_effective_delay_ms` | **62.5** |
| `pattern_overlap_with_predictor` | **0.894** |

At the critic baseline, **22 ft miss exceeds 12.3 ft pattern radius** — `pattern_overlap_at_baseline` is zero. Volume fire does not compensate for stale tracks without **local predictor** on the FCU edge node. With predictor (`pattern_overlap_with_predictor` = 0.894), engagement proxy remains viable.

Regenerate tables: `python scripts/latency_resilience_model.py`

### Delay sweep (selected)

| Speed (mph) | Delay (ms) | Lead error (ft) | `pattern_overlap` |
|-------------|------------|-----------------|-------------------|
| 60 | 100 | 8.8 | 0.70 |
| 60 | 250 | 22.0 | 0.00 |
| 60 | 500 | 44.0 | 0.00 |

---

## 6. Resilient Communication Patterns

### 6.1 Tier 1 — vehicle CAN (D-003)

500 kbps; FIRE_CMD, TRACK, ARM_CMD. Deterministic; not IP.

### 6.2 Optional adjacent-node gossip

Compressed track state (id, az, el, range, range_rate, timestamp, confidence). No central master. Merge under conservative fratricide rules (§7). ICD stub: P9-006.

### 6.3 CAN priority classes

| Class | Preempt | Examples |
|-------|---------|----------|
| P0 — kinetic | Yes | FIRE_CMD, ARM_CMD |
| P1 — track | Yes over P2 | TRACK, AIM_CMD |
| P2 — status | No | MOD_STATUS, SALVO_RPT |
| P3 — telemetry | No | ENGAGE_RPT |

### 6.4 Degradation ladder

| Level | Condition | FCU behavior |
|-------|-----------|--------------|
| **0 — Normal** | Local sensor + C4ISR intent | Full profiles per ROE |
| **1 — C4ISR loss** | TCP/IP down | Local sensor + last-known intent TTL (30 s) |
| **2 — Sensor overload** | Tracks > capacity | Triage top-N; local predictor on |
| **3 — Local sensor loss** | No auto-track | Sector scan behaviors; operator ARMED required |
| **4 — Manual only** | All auto tracks lost | FCU panel az/el entry |

No level autonomously initiates fire under current policy.

---

## 7. Fratricide Under Partial Connectivity

See [`FRATRICIDE_DECONFLICTION.md`](FRATRICIDE_DECONFLICTION.md) §7.

| Source | Latency | Degraded behavior |
|--------|---------|-------------------|
| Vehicle GPS/INS | < 100 ms | Local truth for SI-002 |
| C4ISR friendly position | Seconds | Last-known TTL; expand inhibit if stale |
| Gossip friendly hull ID | Best effort | Conservative union |

**Rules:** Friendly position unknown → **SECTOR_** only (no LAST_DITCH_FULL). Conflicting inhibit → hold fire (SI-011). C4ISR lost → SI-009 (30 s TTL, then SECTOR-only).

---

## 8. Operational Context

Jam-resistant, long-link swarms stress systems that (1) fuse all tracks centrally, (2) require TCP/IP for engagement, (3) assume timely RWS/Ethernet under EW. MKFS remains operable when Ethernet/C4ISR degrades: co-mounted CAN sensor, local predictor, manual cue.

---

## 9. Separation of Concerns

| Function | Max latency | Link | Central required? |
|----------|-------------|------|-------------------|
| Primer fire command | ≤ 5 ms | CAN (Tier 1) | No |
| Track update → aim | ≤ 100 ms | CAN / vehicle LAN (Tier 2) | No |
| Track prediction | 250–500 ms compensated | FCU compute (Tier 2) | No |
| ROE / ARMED | Seconds | FCU panel | No |
| Mission intent / geofence | Seconds–minutes | C4ISR (Tier 3) | Optional |
| Fleet picture | Seconds | TCP/IP / gossip | Optional |

---

## 10. Packet Loss — Cue Delivery

From `packet_loss_sweep` at baseline (60 mph, 250 ms):

| Packet loss | P(deliver) | `engagement_no_predictor` | `engagement_with_predictor` |
|-------------|------------|---------------------------|-----------------------------|
| 0% | 1.00 | 0.00 | 0.89 |
| 10% | 0.90 | 0.00 | 0.80 |
| 20% | 0.80 | 0.00 | 0.71 |
| 30% | 0.70 | 0.00 | 0.63 |

Local CAN tracks keep the Tier 1 commit path off IP. Retries increase delivery but add latency.

---

## 11. Gap Assessment

### Established in Phase 9

- Tier 1/2/3 separation and D-013 CAN-only fire path
- Quantified baseline: 22 ft miss, 0.0 overlap without predictor, 0.894 with predictor
- Degradation Levels 0–4, triage spec, network-stress tests T5-N01–N04
- Fratricide rules SI-009–011 under partial connectivity

### Remains unvalidated

| Item | Status |
|------|--------|
| Radio hardware for gossip | Architectural only |
| Crypto / authentication on gossip | Not specified |
| Multi-node track correlation | Not specified |
| Multi-vehicle HIL (P9-007) | Not built |
| Kalman/IMM predictor in FCU | CV model only in repo |
| Autonomous fire policy | Operator ARMED required |
| Base-wide fusion replacement | Out of MKFS scope |

---

## 12. Next Steps

[`tasks/PHASE9.md`](../tasks/PHASE9.md)

---

## 13. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Phase 9 — network/C2 resilience architecture |
| 0.2 | 2026-05-22 | Hardening — quant anchor, Tier 1/2/3 terminology, JSON field traceability |

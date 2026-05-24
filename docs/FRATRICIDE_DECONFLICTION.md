# MKFS Fratricide & Deconfliction

**Status:** Concept | Phase 9
**Purpose:** Friendly/APS deconfliction rules under partial connectivity.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-DOC-SAFE-001  
**Version:** 0.3 (Phase 9 hardening)  
**Mitigates:** R-004, R-013 in [RISK_REGISTER.md](RISK_REGISTER.md)  
**Related:** [DUAL_ARRAY_FIRE_PLANS.md](DUAL_ARRAY_FIRE_PLANS.md) | [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md) | [CONOPS_VIGNETTES.md](CONOPS_VIGNETTES.md) | [NETWORK_ARCHITECTURE.md](NETWORK_ARCHITECTURE.md)

---

## 1. Problem Statement

MKFS fires **thousands of titanium BBs** into a terminal volume. Friendly troops, adjacent vehicles, aircraft, and existing APS/CIWS systems must be **protected from inadvertent engagement** and collateral hazard.

---

## 2. FCU Interlocks

From [FCU_STATE_MACHINE.md](../src/fire_control/FCU_STATE_MACHINE.md):

| ID | Condition | Action |
|----|-----------|--------|
| SI-002 | Friendly zone inhibit (GPS + turret aspect) | Block tubes in inhibit arc |
| SI-003 | Module elevation < −5° or > +60° | Block fire |
| SI-001 | Vehicle speed > 5 kph | Block ARMED unless override |

**Additional MKFS interlocks (concept):**

| ID | Condition | Action |
|----|-----------|--------|
| SI-006 | Dismount zone active within 75 m | Limit to **SECTOR_** profiles only |
| SI-007 | Friendly aircraft ADIZ overlap | Full inhibit until clear |
| SI-008 | Trophy/APS active engagement | 500 ms hold — avoid dual intercept |
| SI-009 | C4ISR link lost | Apply last-known inhibit zones (TTL **30 s**); then **SECTOR_** profiles only |
| SI-010 | Friendly position gossip stale (> **15 s**) | Expand inhibit arc by **+5°** safety margin |
| SI-011 | Conflicting inhibit from two nodes | **Hold fire** until resolved; trust local GPS for SI-002 when valid |

---

## 3. Dismounted Troop Standoff Arcs

```mermaid
flowchart TB
  subgraph vehicle [Vehicle]
    MKFS[MKFS_Tile]
  end
  subgraph arcs [StandoffArcs]
    FULL[FullDumpBlocked_75m]
    SECTOR[SectorFireAllowed_75to150m]
    CLEAR[NoRestrict_beyond150m]
  end
  MKFS --> FULL
  MKFS --> SECTOR
  MKFS --> CLEAR
```

| Troop distance | Permitted profile | Elevation trim |
|----------------|-------------------|----------------|
| < 75 m | **HOLD** — no fire | — |
| 75–150 m | **SECTOR_** masks only | +3° to +8° minimum |
| > 150 m | All profiles per ROE | FCU computed |

See Vignette 3 in [CONOPS_VIGNETTES.md](CONOPS_VIGNETTES.md).

---

## 4. Dual-Array Overlap

Per [DUAL_ARRAY_FIRE_PLANS.md](DUAL_ARRAY_FIRE_PLANS.md), forward and aft modules overlap at vehicle quarters. FCU edge node **deduplicates tube masks** in overlap zones when both modules engage the same azimuth.

---

## 5. Coexistence with Other Systems

| System | Deconfliction |
|--------|---------------|
| **Trophy / APS** | MKFS fires **outside** APS engagement envelope (> 50 m) or on SI-008 hold |
| **CIWS / Phalanx** | MKFS is terminal backup — CIWS owns inner bubble; MKFS owns 200–500 yd band |
| **Friendly rotary-wing** | SI-007 + altitude filter — no fire above 200 ft AGL in friendly corridor |
| **Dismounted infantry** | SI-006 sector masks — never LAST_DITCH_FULL with troops near |

---

## 6. Training & ROE Checklist

Before arming MKFS (FCU edge node):

- [ ] Dismount status confirmed on FCU
- [ ] Friendly air corridor checked
- [ ] APS/CIWS status acknowledged
- [ ] Inhibit arcs set for troop position
- [ ] Salvo profile selected *(default: SWARM_WIDE, not FULL)*
- [ ] Commander authorizes ARMED
- [ ] C4ISR link state acknowledged (SI-009 fallback understood)
- [ ] Gossip neighbor count / staleness checked (SI-010/011)
- [ ] Last-known inhibit TTL visible on FCU
- [ ] If SI-009, SI-010, or SI-011 active → LAST_DITCH_FULL **blocked**

**LAST_DITCH_FULL** requires **dual confirmation** (commander + gunner) when any friendly within 150 m.

---

## 7. Degraded Connectivity

When links are lossy or denied — [NETWORK_ARCHITECTURE.md](NETWORK_ARCHITECTURE.md) §6.4 degradation Levels 0–4.

| Condition | Fratricide response |
|-----------|---------------------|
| C4ISR down (Level 1) | SI-009: last-known inhibit TTL 30 s → SECTOR-only |
| Gossip stale | SI-010: widen inhibit arc +5° |
| Conflicting friendly reports | SI-011: hold fire |
| Local GPS valid, C4ISR invalid | Trust local GPS for SI-002 |
| All position sources lost (Level 4) | **HOLD** — manual confirm only |

---

## 8. Range / Test Safety

T5 test per [SWARM_TEST_CONCEPT.md](SWARM_TEST_CONCEPT.md): 200 m lateral standoff, 600 m downrange clear. Instrumented inhibit zones validate SI-002 before live swarm surrogates.

---

## 9. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial fratricide and deconfliction concept |
| 0.2 | 2026-05-22 | Phase 9 — SI-009–011 degraded connectivity |
| 0.3 | 2026-05-22 | Hardening — integrated checklist, Degradation Level alignment |

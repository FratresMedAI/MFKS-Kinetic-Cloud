# Phase 9 — Network & C2 Resilience Backlog

**Status:** P0 items complete (docs + model); P1+ pending  
**Parent:** [NETWORK_ARCHITECTURE.md](../docs/NETWORK_ARCHITECTURE.md)  
**Last updated:** 2026-05-22

---

## P0 — Complete (Phase 9 sprint)

| ID | Task | Deliverable | Status |
|----|------|-------------|--------|
| P9-001 | Write NETWORK_ARCHITECTURE.md | [NETWORK_ARCHITECTURE.md](../docs/NETWORK_ARCHITECTURE.md) | Done |
| P9-002 | Latency / packet-loss model | [latency_resilience_model.py](../scripts/latency_resilience_model.py) | Done |
| P9-003 | Degraded scenarios in SWARM_TEST + FRATRICIDE | T5-N01–N04, SI-009–011 | Done |

---

## P1 — Next (software / ICD)

| ID | Task | Deliverable | Notes |
|----|------|-------------|-------|
| P9-004 | Extend FCU HIL with delayed/lost tracks | `hil_sim.py` + tests | Inject 250 ms delay; verify predictor hook |
| P9-005 | CAN TRACK v2 message addendum | ICD §3.2 extension | velocity + timestamp fields on `0x300` |
| P9-006 | Gossip ICD stub | `docs/ICD_NODE_GOSSIP.md` | Adjacent-node compressed track share |

---

## P2 — Simulation & CONOPS

| ID | Task | Deliverable | Notes |
|----|------|-------------|-------|
| P9-007 | Multi-node time-synced sim | `src/fire_control/multi_node_sim.py` | 3 FCU stubs; gossip + fratricide |
| P9-008 | CONOPS vignette: full C4ISR denial | [CONOPS_VIGNETTES.md](../docs/CONOPS_VIGNETTES.md) Vignette 7 | EW + Ethernet down; CAN-only |

---

## P3 — Research

| ID | Task | Deliverable | Notes |
|----|------|-------------|-------|
| P9-009 | Radio link trade study | Research note | UHF mesh vs wired convoy tether |
| P9-010 | Kalman / IMM predictor upgrade | Model + HIL | Replace CV minimum in latency model |
| P9-011 | Crypto / auth for gossip | Security note | Anti-spoof for friendly position |

---

## Success metrics (from critique)

| Metric | Target | Current |
|--------|--------|---------|
| 60 mph + 250 ms lead error documented | ~22 ft | **Done** (model + doc) |
| Fire path independent of TCP/IP | D-013 | **Done** |
| Degraded comms test cases defined | T5-N01–N04 | **Done** |
| Predictor restores overlap @ baseline | ≥ 70% | **Concept** (~70% in model); HIL not built |
| Multi-node sim | 3 nodes | **Not started** (P9-007) |

---

## Honest remaining gaps

See [NETWORK_ARCHITECTURE.md](../docs/NETWORK_ARCHITECTURE.md) §11 — radio hardware, crypto, formal track correlation, certifiable autonomous fire policy, central fusion replacement.

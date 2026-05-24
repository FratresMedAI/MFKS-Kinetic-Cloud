# MKFS Risk Register

**Status:** Concept | Phase 9
**Purpose:** Program risks and mitigations.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-DOC-RISK-001  
**Version:** 0.3 (Phase 9 hardening)  
**Related:** [REQUIREMENTS.md](REQUIREMENTS.md) | [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md) | [NETWORK_ARCHITECTURE.md](NETWORK_ARCHITECTURE.md)

---

## Top 10 Risks

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|------------|--------|------------|-------|
| R-001 | `R_open` drift exceeds ±30 ft due to propellant/`V_0` variation | Medium | High | Band index shims; FCU elevation comp; lot testing | Eng |
| R-002 | Pattern density insufficient vs. fast swarm | Medium | High | Salvo profiles; dense tier on MRAP; Option A hybrid | Eng |
| R-003 | Roof structural limit on M113 / LAV-25 | Medium | Medium | Compact tier only; reinforcement plate; Phase 3 analysis | Integration |
| R-004 | Friendly fire / fratricide from flechette cloud | Low | Critical | Arming interlocks; elevation limits; training — see [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md) | Safety |
| R-005 | Pod swap too slow under combat reload | Medium | Medium | P2 prototype time study; tool-free latches | Prototype |
| R-006 | Ti flechette cost / supply chain | Medium | Medium | Dual-source; steel fallback variant | Logistics |
| R-007 | CAN bus EMI on vehicle platform | Low | Medium | Shielded harness; MIL-38999 connector; HIL test | Software |
| R-008 | Mechanism failure rate > 0.5% | Low | High | Accelerated life test; redundant petal design | QA |
| R-009 | Sensor cueing latency vs. small UAS | Medium | High | Co-mounted CAN sensor; local predictor; manual override | Integration |
| R-010 | Regulatory / classification of kinetic counter-UAS | Low | High | Early legal review; kinetic-only advantage — see [ITAR_EXPORT_FRAMING.md](ITAR_EXPORT_FRAMING.md) | Program |

## Network & C2 Risks *(Phase 9)*

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|------------|--------|------------|-------|
| R-011 | Central fusion / C4ISR overload under multi-wave swarm | Medium | High | Tier 2 edge triage; CAN-local tracks; D-013 CAN-only fire path | Software |
| R-012 | C4ISR latency / packet loss → stale aim (`pattern_overlap_at_baseline` = 0 at 250 ms) | Medium | High | Local predictor on FCU edge node; 500 ms hold-fire; [latency_resilience_output.json](../scripts/latency_resilience_output.json) | Software |
| R-013 | Gossip fratricide uncertainty (spoofed/stale friendly position) | Low | Critical | SI-010 (+5° margin); SI-011 hold fire on conflict | Safety |

---

## Risk Matrix

```
Impact
  Critical | R-004 R-013   | R-001 R-002 R-008 R-010
  High     |               | R-009 R-011 R-012
  Medium   |               | R-003 R-005 R-006 R-007
  Low      |               |
           +--------------+--------------+
              Low           Medium         Likelihood
```

---

## Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial top 10 risks |
| 0.2 | 2026-05-22 | Phase 9 — R-011–R-013 network/C2 risks |
| 0.3 | 2026-05-22 | Hardening — mitigation wording tied to D-013, JSON fields, SI-010/011 |

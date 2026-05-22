# MKFS Risk Register

**Document ID:** MKFS-DOC-RISK-001  
**Version:** 0.1 (Phase 4 draft)  
**Related:** [REQUIREMENTS.md](REQUIREMENTS.md) | [DEPLOYMENT_DOWN_SELECT.md](DEPLOYMENT_DOWN_SELECT.md)

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
| R-009 | Sensor cueing latency vs. small UAS | Medium | High | Optional swarm radar kit; manual override salvo | Integration |
| R-010 | Regulatory / classification of kinetic counter-UAS | Low | High | Early legal review; kinetic-only advantage — see [ITAR_EXPORT_FRAMING.md](ITAR_EXPORT_FRAMING.md) | Program |

---

## Risk Matrix

```
Impact
  Critical | R-004        | R-001 R-002 R-008 R-010
  High     |              | R-009
  Medium   |              | R-003 R-005 R-006 R-007
  Low      |              |
           +--------------+--------------+
              Low           Medium         Likelihood
```

---

## Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial top 10 risks |

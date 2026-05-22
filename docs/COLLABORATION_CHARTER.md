# MKFS Collaboration Charter

**Document ID:** MKFS-DOC-COLLAB-001  
**Version:** 0.1 (Phase 5)  
**License:** [Apache 2.0](../LICENSE)  
**Related:** [CONTRIBUTING.md](../CONTRIBUTING.md) | [ITAR_EXPORT_FRAMING.md](ITAR_EXPORT_FRAMING.md) | [QUESTIONS_FOR_PRIMES.md](outreach/QUESTIONS_FOR_PRIMES.md)

---

## 1. Purpose

Define what **FratresMedAI** offers in this open repository and what we seek from **defense primes, integrators, and research partners** — without pretending to be a prime contractor.

---

## 2. What FratresMedAI Provides (Open)

| Asset | Location | Value to partner |
|-------|----------|------------------|
| Design philosophy & CONOPS | `docs/` | Shared problem framing |
| Puck ICD & release mechanism | `docs/CARRIER_PROJECTILE_ICD.md`, `PUCK_RELEASE.md` | Starting technical baseline |
| Ballistics model | `research/ballistics/` | Salvo density analysis |
| FCU state machine + stub | `src/fire_control/` | Software integration starting point |
| Adapter kit concepts | `docs/adapters/` | Vehicle integration sketches |
| Concept renders | `assets/` | Program communication |
| Test & risk docs | `docs/TEST_EVAL_PLAN.md`, `RISK_REGISTER.md` | Planning scaffolding |

All under **Apache 2.0** — fork, extend, integrate.

---

## 3. What We Seek from Partners

| Contribution | Priority | Notes |
|--------------|----------|-------|
| **Mechanism prototype** (hollow-point skirt release) | High | M1 milestone — setback petal proof |
| **Range test data** | High | T2/T5 validation — export-controlled handling |
| **Vehicle adapter CAD** | Medium | Stryker/Bradley structural sign-off |
| **Manufacturing ROM** | Medium | Replace placeholder economics |
| **Safety / fratricide review** | Medium | Expand [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md) |
| **Propellant / chamber design** | High | Not in open repo — program-controlled |
| **Production tooling** | Low (later) | M10 pilot lot |

---

## 4. Collaboration Models

| Model | Description |
|-------|-------------|
| **GitHub PR** | Doc/code contributions per [CONTRIBUTING.md](../CONTRIBUTING.md) |
| **CRADA / R&D agreement** | Shared mechanism or range test — counsel required |
| **Subcontract** | Prime builds hardware to open ICD; FratresMedAI retains concept IP per Apache contributions |
| **License discussion** | Dual-license or program-specific terms for controlled artifacts |

---

## 5. Boundaries

**FratresMedAI is not:**
- A manufacturer of record
- An export license holder *(today)*
- A certifying authority for fielding

**Partners retain:**
- Build, test, field, and export compliance for hardware they produce

See [ITAR_EXPORT_FRAMING.md](ITAR_EXPORT_FRAMING.md) for control discussion.

---

## 6. Success Criteria for Collaboration

1. M1 mechanism proof completed with documented test data  
2. 136-tube module fires on range with ≥ 300 hits/m² @ 350 ft  
3. First vehicle mount (Stryker) with FCU HIL pass  
4. Prime publishes adapter CAD under agreed license  

---

## 7. Contact

- **Repository:** [github.com/FratresMedAI/MFKS-Kinetic-Cloud](https://github.com/FratresMedAI/MFKS-Kinetic-Cloud)  
- **Issues / PRs:** Preferred for technical discussion  
- **Direct outreach:** Via GitHub profile for program conversations  

---

## 8. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial collaboration charter |

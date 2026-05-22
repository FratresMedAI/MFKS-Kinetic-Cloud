# MKFS ITAR & Export-Control Framing

**Document ID:** MKFS-DOC-LEGAL-001  
**Version:** 0.1 (Phase 5 — collaborator briefing, **not legal advice**)  
**Mitigates:** R-010 in [RISK_REGISTER.md](RISK_REGISTER.md)  
**Related:** [LICENSE](../LICENSE) | [COLLABORATION_CHARTER.md](COLLABORATION_CHARTER.md)

---

> **Disclaimer:** This document is a **collaborator briefing** for open-concept discussion. It is **not legal advice**. Engage qualified export counsel before any controlled transfer, foreign collaboration, or program submission.

---

## 1. Why This Matters

MKFS is a **kinetic counter-UAS / terminal defense** concept. Collaborators (defense primes, integrators, foreign partners) need clarity on **what this repo contains** vs what would require **program-controlled handling**.

---

## 2. What This Open Repo Contains

| Category | Status in repo | Typical control posture |
|----------|----------------|-------------------------|
| Concept documentation | Public (Apache 2.0) | Uncontrolled concept |
| Ballistics model (stdlib Python) | Public | Uncontrolled analysis |
| FCU state machine stub | Public | Uncontrolled software concept |
| Concept renders | Public | Uncontrolled illustrations |
| Puck ICD (geometry, no propellant spec) | Public | Concept — verify before build |

**Kinetic-only design boundary:**
- No explosives in round
- No guidance / seeker / autonomous targeting in projectile
- No propellant formulation or live fire data in repo

---

## 3. What Would Stay Program-Controlled in a Prime Partnership

| Artifact | Reason |
|----------|--------|
| Propellant / chamber pressure data | Energetic materials |
| Live fire test results | Performance of defense article |
| Production CAD / tooling | Manufacturing know-how |
| Vehicle-specific integration packages | Platform + defense combination |
| Export-licensed foreign variants | ITAR/EAR per destination |

FratresMedAI intends to keep **concept and ICD open**; primes retain **build, test, and field** under their compliance programs.

---

## 4. Apache 2.0 Posture

Repository licensed under **Apache License 2.0** — see [LICENSE](../LICENSE).

**Why Apache for U.S. industry collab:**
- Explicit **patent grant** — reduces friction for prime legal review
- Permissive use, modification, and commercial integration
- Standard license familiar to Northrop, L3Harris, RTX, etc.

Contributors grant patent rights per Apache §3. Prime contributions should follow [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## 5. Kinetic-Only Advantage for Classification Discussions

| Factor | MKFS posture |
|--------|--------------|
| Explosive warhead | **None** |
| Guidance | **None** in round |
| Autonomous weapon | **No** — FCU fires fixed tubes on cue |
| Dual-use | Potential — commercial perimeter variant |

Kinetic-only does **not** automatically mean uncontrolled — **caliber, performance, and end use** still matter for ITAR/EAR. This repo stays at **concept TRL** to minimize inadvertent control issues.

---

## 6. Questions for Your Counsel

Before collaborating or exporting:

1. Does our puck ICD + concept doc constitute **technical data** under ITAR Category VIII or XI?
2. Does foreign national access to a forked repo require **license**?
3. What performance thresholds trigger **defense article** classification for flechette cartridges?
4. Can we publish live fire density results without control?
5. Does Apache 2.0 distribution to **listed countries** require additional review?
6. How do we structure a **CRADA** or prime subcontract to keep concept open and hardware controlled?

---

## 7. FratresMedAI Intent

- Keep **idea-layer** open for industry collab  
- Route **build-layer** through prime compliance  
- No live munitions data in public repo without counsel sign-off  

Contact: [github.com/FratresMedAI](https://github.com/FratresMedAI)

---

## 8. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial ITAR/export collaborator briefing |

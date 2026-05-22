# Contributing to MFKS / MKFS Kinetic Cloud

Thank you for your interest in contributing. This project is licensed under **Apache License 2.0** — see [LICENSE](LICENSE).

---

## What We're Looking For

- Documentation improvements (CONOPS, ICDs, adapter kits)
- Ballistics model enhancements (stdlib Python only)
- FCU state machine and test coverage
- Adapter CAD concepts and integration notes
- Range test data *(subject to export review — see [ITAR_EXPORT_FRAMING.md](docs/ITAR_EXPORT_FRAMING.md))*

---

## How to Contribute

1. **Fork** the repo on GitHub
2. **Branch** from `main` — use descriptive names (`docs/fratricide-update`, `ballistics/salvo-model`)
3. **Make changes** — follow existing doc conventions below
4. **Test** if touching code:
   ```bash
   python -m pytest src/fire_control/test_fcu.py -v
   python research/ballistics/ballistics_model.py
   ```
5. **Open a Pull Request** with a clear description of what and why

---

## Documentation Conventions

| Element | Convention |
|---------|------------|
| Doc ID | `MKFS-DOC-XXX-001` in header |
| Version | Increment on substantive change |
| Related docs | Link at top of each file |
| Status | Mark concept vs fielded clearly |
| ROM / estimates | Label as placeholders |

Place new docs in:
- `docs/` — system documentation
- `docs/adapters/` — vehicle kits
- `docs/outreach/` — pitch and prime materials
- `docs/visual/` — storyboards and render briefs
- `research/` — trade studies and models

---

## Code Conventions

- **Python:** stdlib only in `research/ballistics/` — no pip dependencies unless CI updated
- **Tests:** `pytest` in `src/fire_control/`
- **FCU:** Match states in [FCU_STATE_MACHINE.md](src/fire_control/FCU_STATE_MACHINE.md)

---

## Apache 2.0

By contributing, you agree your contributions are licensed under Apache 2.0. You grant patent rights per the license terms.

Do **not** commit:
- Classified or export-controlled technical data
- Propellant formulations or live fire results without counsel approval
- Credentials, `.env`, or secrets

---

## Collaboration

For prime partnerships and larger engagements, see [COLLABORATION_CHARTER.md](docs/COLLABORATION_CHARTER.md).

Questions: open a GitHub issue or contact [FratresMedAI](https://github.com/FratresMedAI).

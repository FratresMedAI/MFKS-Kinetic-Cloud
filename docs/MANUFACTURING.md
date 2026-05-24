# MKFS Manufacturing Considerations

**Status:** Concept | Phase 9
**Purpose:** Production and scale considerations.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-DOC-MFG-001  
**Version:** 0.1 (Phase 4)  
**Related:** [SYSTEM_SPEC.md](SYSTEM_SPEC.md) | [CARRIER_PROJECTILE_ICD.md](CARRIER_PROJECTILE_ICD.md)

---

## 1. Production Volume Scenarios

| Scenario | Cartridges/yr | Array Modules/yr | Adapter Kits/yr |
|----------|---------------|------------------|-----------------|
| Pilot | 5,000 | 50 | 100 |
| Low rate | 50,000 | 200 | 400 |
| Full rate | 250,000 | 800 | 1,600 |

---

## 2. Cartridge Manufacturing

### 2.1 Process Flow

```
Case manufacture → Primer install → Propellant load →
Carrier body assembly → Flechette pack load →
Band index set → QC → Seal → Pack
```

### 2.2 Key Processes

| Process | Method | QC Point |
|---------|--------|----------|
| Case | Draw + machine | Dimensional, pressure test |
| Flechette | CNC turn (Ti) | Mass, length sample |
| Petal ring | Injection mold (polymer) | Shear force sample |
| Spring stack | Belleville stack + shim | Preload measurement |
| Assembly | Automated or semi-auto | Function sample 1:100 |

### 2.3 Supply Chain

| Component | Source Strategy | Risk |
|-----------|-----------------|------|
| Ti-6Al-4V bar | Dual source (US) | Medium — see R-006 |
| Cases | Existing 30 mm supply base | Low |
| Propellant | Low-pressure charge (electric primer) | Not high-pressure smokeless long-range |
| Petal polymer | Commercial FR-grade | Low |

---

## 3. Array Module Manufacturing

| Component | Process | Notes |
|-----------|---------|-------|
| Tube bundle | Seamless steel tube, ream | Chamber tolerance ±0.02 mm |
| Module frame | Weldment + machine | MKFS-IF-002 face flatness 0.5 mm |
| Cam mechanism | CNC + heat treat | 500-cycle life test sample |
| FCU electronics | COTS + conformal coat | MIL-STD-810 |

Pod assembly parallel to module; pods shipped loaded or empty per customer.

---

## 4. Adapter Kits

- Fabrication: laser-cut plate, machined risers
- Platform-specific fairings: composite or sheet metal
- Kits ship as bolt-on packages with install manual
- No hull modification tooling required

---

## 5. Quality Assurance

| Level | Activity |
|-------|----------|
| Lot acceptance | `V_0` sample (n=5), function sample (n=10) |
| Periodic | Full T2 ballistics (quarterly) |
| Module | Salvo test every 50th unit |
| Traceability | RFID pod tag + cartridge lot stamp |

---

## 6. Cost Drivers *(ROM)*

| Item | Unit Cost Driver |
|------|------------------|
| Cartridge | Ti flechettes (~40%), assembly labor |
| Module | Tube count, electronics |
| Adapter kit | Low volume per platform — fairing tooling |

---

## 7. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial manufacturing outline |

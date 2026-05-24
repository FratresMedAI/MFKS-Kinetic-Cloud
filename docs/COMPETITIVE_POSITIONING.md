# MKFS Competitive Positioning

**Status:** Concept | Phase 9
**Purpose:** Competitive comparison vs missiles, APS, shotguns.
**Key Decisions:** See [DECISIONS.md](DECISIONS.md)
**Open Questions:** See [RISK_REGISTER.md](RISK_REGISTER.md)

**Document ID:** MKFS-DOC-COMP-001  
**Version:** 0.1 (Phase 5)  
**Related:** [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) | [SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md) | [MAGAZINE_ECONOMICS.md](MAGAZINE_ECONOMICS.md)

---

## 1. Purpose

Honest comparison of MKFS against alternative terminal-defense approaches — where kinetic cloud wins, where it loses.

---

## 2. Comparison Matrix

| Approach | Range | Swarm handling | Power / logistics | Weather | Cost curve | Fratricide risk | Maturity |
|----------|-------|----------------|-------------------|---------|------------|-----------------|----------|
| **MKFS kinetic cloud** | 200–500 yd | **High volume** — 310–1,977 hits/m² | Magazine mass; 28 VDC | All-weather kinetic | **Low per shot** (~$100 puck ROM) | **High** — needs interlocks | Concept TRL 2–3 |
| Directed energy (DEW) | 100–1000+ m | Single beam — sequential | **High power** (kW–MW) | Rain/dust degraded | High capital, low per shot | Lower collateral | Emerging TRL 6+ |
| EW / jamming | BLOS if linked | Soft kill — autonomy dependent | Moderate power | Spectrum contested | System cost | Low kinetic | Fielded |
| Explosive intercept (Trophy) | 50–200 m | 1–2 targets per shot | Reload + blast hazard | All-weather | **High per shot** | Blast + debris | Fielded TRL 9 |
| Shotgun / C-UAS drones | 100–300 m | 1 target per engagement | Drone logistics | Moderate | Moderate | Moderate | Commercial |
| CIWS (Phalanx) | 500–1500 m | Gatling volume | Ship power | All-weather | High capital | Penetrator risk | Fielded TRL 9 |

---

## 3. Where MKFS Wins

**Terminal swarm volume.** At 350 ft, a single 2×1 strip delivers **310 hits/m²** — see [SALVO_SCENARIOS.md](../research/ballistics/SALVO_SCENARIOS.md). A 289-tube turret deck delivers **659 hits/m²**. No other portable vehicle system matches **titanium BB count** in one trigger pull.

**No HE in the round.** Simpler storage, fewer explosive safety restrictions, no detonation chain in the magazine.

**Mechanical simplicity.** Hollow-point skirt release — no fuze, no seeker, no guidance law. Electronics at launcher only.

**Cost per engagement.** Dual-strip salvo ROM **$11K–$20K** vs **$100K+** per missile — see [MAGAZINE_ECONOMICS.md](MAGAZINE_ECONOMICS.md).

**All-weather kinetic.** Unlike DEW, rain and dust do not defocus **Ti BBs**.

---

## 4. Where MKFS Loses

**Beyond-line-of-sight.** MKFS is terminal only (~500 yd max). Not a replacement for radar, EW, or medium-range AD.

**Single-target precision.** Cannot pick one drone in a crowded sky with surgical precision — it saturates a volume.

**Reload time.** Pod swap ~5 min; turret deck reload longer. DEW and EW do not consume physical rounds the same way.

**Fratricide.** Thousands of **titanium BBs** require strict interlocks — see [FRATRICIDE_DECONFLICTION.md](FRATRICIDE_DECONFLICTION.md). Trophy/DEW have different collateral profiles.

**Peacetime optics.** Kinetic counter-UAS near populated areas faces regulatory scrutiny regardless of HE content.

**Maturity.** Concept phase — no fielded MKFS equivalent yet. CIWS and Trophy are proven.

---

## 5. Role in Layered Defense

```mermaid
flowchart LR
  BLOS[BLOS_Radar_EW] --> MID[MediumRange_Missile]
  MID --> TERMINAL[MKFS_TerminalCloud]
  TERMINAL --> INNER[CIWS_APS_Inner]
```

MKFS sits **between** failed mid-range intercept and inner APS — the **"don't die"** layer when the swarm is already close.

---

## 6. Revision History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-22 | Initial competitive positioning |
| 0.2 | 2026-05-22 | Phase 8 — titanium BB density language |

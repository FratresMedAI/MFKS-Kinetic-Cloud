# MFKS — Modular Flechette Kinetic System (MKFS)

**Last-ditch kinetic saturation when drone swarms are already inside ~500 yd and everything else failed.**

**Repository:** [github.com/FratresMedAI/MFKS-Kinetic-Cloud](https://github.com/FratresMedAI/MFKS-Kinetic-Cloud)

→ Full documentation: [docs/00_INDEX.md](docs/00_INDEX.md)

---

## The Problem

- **Close-in drone swarms** leak inside **~500 yd** when EW degrades, missiles run dry, and CIWS is not on the vehicle.
- **One-shot interceptors** cannot saturate a multidirectional swarm at terminal range — cost and magazine depth lose to volume.
- **Centralized track fusion over TCP/IP** adds latency and loss; at **60 mph** and **250 ms** stale tracks, uncompensated aim misses by **`lead_error_ft` = 22.0** — outside the **`pattern_radius_ft` = 12.3** cloud ([`latency_resilience_output.json`](scripts/latency_resilience_output.json)).
- The fight at this range is **volume and survival**, not elegance.

---

## The MFKS Answer

Modular **kinetic-only** appliqué — same role as hard-kill APS or CIWS, no explosives in the round.

| Package | Form | Tubes (approx.) |
|---------|------|-----------------|
| **Appliqué strips** | Flat on Stryker/JLTV/ship skin | **136** (2×1 ft) / **208** (3×1 ft) |
| **Pan-tilt turret** | Moving head + yoke (stage-light style) | **289** per deck × 3–4 deep |

- **Half-dollar puck cartridges** (31 mm × 28 mm) — hollow-point skirt peels under speed; **~40 titanium BBs** per puck.
- **Electronic per-tube fire** — sector, ripple, or full dump; not dumb fuse lines.
- **Volume saturation @ 350 ft:** one **2×1 strip** (136 tubes) → **310 hits/m²** in a **~24.5 ft** pattern ([SALVO_SCENARIOS.md](research/ballistics/SALVO_SCENARIOS.md)).

→ [DESIGN_PHILOSOPHY.md](docs/DESIGN_PHILOSOPHY.md) · [M1_SPEC.md](docs/M1_SPEC.md)

---

## Why It Actually Works in the Real World

Stale tracks kill terminal kinetic if you aim at the last report. MKFS puts **prediction and fire commit on the vehicle**, not the brigade net.

**Two mechanisms:**

1. **Local FCU predictor (Tier 2)** — constant-velocity lead on the edge node. Effective delay = measured latency × **0.25** → **`predictor_effective_delay_ms` = 62.5** at 250 ms baseline. Restores **`pattern_overlap_with_predictor` = 0.894** vs **`pattern_overlap_at_baseline` = 0.0** without it.
2. **CAN-isolated fire path (Tier 1, [D-013](docs/DECISIONS.md))** — track → FCU → `FIRE_CMD` on vehicle CAN (≤ 5 ms). **Track-to-primer SHALL NOT traverse TCP/IP.** C4ISR delivers mission intent only.

```
Without predictor:  250 ms @ 60 mph → lead_error_ft 22.0 → pattern_overlap 0.0
With FCU predictor: 62.5 ms effective → pattern_overlap_with_predictor 0.894
```

→ [FCU_EDGE_PREDICTOR_ONEPAGER.md](docs/FCU_EDGE_PREDICTOR_ONEPAGER.md) · [NETWORK_ARCHITECTURE.md](docs/NETWORK_ARCHITECTURE.md)

---

## Two Form Factors

### Appliqué strips (2×1 / 3×1 ft)

![Appliqué mounts — Stryker, JLTV, USV](assets/mkfs_mounting_concept_stryker_jltv_usv.png)

Flat tiles on hull, bustle, roof. **136–208 tubes** per face. Primary Stryker/JLTV integration path.

### Pan-tilt turret (2×2 ft magazine in head)

![Moving-head pan-tilt turret — 2×2 ft magazine inside head](assets/mkfs_moving_head_turret_2x2.png)

**289 tubes** per deck, stacked 3–4 deep. Observatory shutters open; full dump in **~0.6–1.7 s**.

→ Puck release sequence: [PUCK_STORYBOARD.md](docs/visual/PUCK_STORYBOARD.md)

---

## Integration & Cueing

MKFS is **sensor- and AI-layer friendly, not dependent** on them.

| Priority | Source | Link |
|----------|--------|------|
| 1 | Co-mounted EM/radar | CAN `0x300 TRACK` |
| 2 | Vehicle radar / RWS | Vehicle LAN or manual |
| 3 | C4ISR / external AI | TCP/IP — **intent only** (ROE, inhibit zones) |
| 4 | FCU panel | Manual az/el fallback |

Co-mounted CAN tracks keep Tier 1 alive when Ethernet or C4ISR drops. Operator **ARMED** required — no autonomous fire.

→ [ICD_SENSOR_INTEGRATION.md](docs/ICD_SENSOR_INTEGRATION.md) · [CONOPS_VIGNETTES.md](docs/CONOPS_VIGNETTES.md)

---

## License

Licensed under **[Apache License 2.0](LICENSE)** — industry-friendly open terms with an explicit patent grant.

Contributions welcome (issues, pull requests, or direct outreach). Defense primes, integrators, and research partners can fork and extend under the license terms.

→ [LICENSE](LICENSE) · [NOTICE](NOTICE) · [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Current Status

**Concept documentation • Phase 9 network/C2 complete • Not an engineering spec or procurement offer**

# MFKS — Modular Flechette Kinetic System

**Terminal kinetic layer for swarms that have already closed inside ~500 yards** — the outer **threat envelope** when the last-ditch layer becomes relevant. **Not** a long-range engagement system.

**Effective engagement:** **150–350 yards**. Useful pattern density out to **~400–450 yards** in optimal turret/elevated setups.

**M1 baseline:** Low-pressure electric-primer charges, **distributed/sequenced tube fire** (sector, ripple, full dump) — not high-pressure smokeless powder or single long-range shots. When outer layers fail and the vehicle cannot afford to die, MFKS saturates the terminal volume with ~11,500+ sub-projectiles from a single 2×2 ft box.

**Exploring (not M1):** Range-extension options — small cost-effective boosters on pucks or mortar-style low-pressure launch — to improve effectiveness toward the full ~500 yd threat envelope while keeping recoil manageable.

## Why it actually works when tracks are stale

At 60 mph, a 250 ms track delay creates a **22 ft lead error**.  
MFKS pattern radius is only **~12.3 ft** → baseline overlap = **0.0**.

The FCU edge node runs a local constant-velocity predictor (effective delay 62.5 ms) and fires over **CAN only** (D-013).  
Result: `pattern_overlap_with_predictor = 0.894`.

→ [FCU_EDGE_PREDICTOR_ONEPAGER.md](docs/FCU_EDGE_PREDICTOR_ONEPAGER.md)

## Two packaging lines

| Package              | Form                        | Module size     | Tubes (approx) |
|----------------------|-----------------------------|-----------------|----------------|
| **Appliqué strips**  | Flat on hull/roof           | 2×1 ft / 3×1 ft | 136 / 208      |
| **Pan-tilt turret**  | Moving head + yoke          | 2×2 ft magazine | 289 per deck   |

Every tube is individually addressable. Salvo profiles: `SECTOR`, `SWARM_WIDE`, `LAST_DITCH_FULL`.

**Concept renders:** [assets/](assets/)

## Integration

- Takes cues from co-mounted radar/EM or external AI/sensor layers ([ICD_SENSOR_INTEGRATION.md](docs/ICD_SENSOR_INTEGRATION.md), [ICD_DRONE_RADAR.md](docs/ICD_DRONE_RADAR.md))
- Fire decision stays local and deterministic on CAN
- Operator remains **ARMED** at every degradation level

## Current status

**Concept documentation only.** Not an engineering specification or procurement offer.

**Phase 9** in progress: hardware-scale FCU + live predictor validation targets.

**License:** Apache 2.0 with explicit patent grant. Defense primes and integrators welcome to fork and extend.

→ Full documentation hub: [docs/00_INDEX.md](docs/00_INDEX.md)

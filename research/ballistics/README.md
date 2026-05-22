# research/ballistics/

MKFS Phase 1 ballistics and flechette dispersion analysis.

## Files

| File | Description |
|------|-------------|
| [ballistics_model.py](ballistics_model.py) | Trajectory, pattern, and V₀ sensitivity model (stdlib only) |
| [BALLISTICS_RESULTS.md](BALLISTICS_RESULTS.md) | Generated results — run model to refresh |
| [ballistics_output.json](ballistics_output.json) | Machine-readable output |
| [FLECHETTE_TRADE_STUDY.md](FLECHETTE_TRADE_STUDY.md) | Material and count trade study |

## Usage

```bash
python ballistics_model.py
```

Regenerates `BALLISTICS_RESULTS.md` and `ballistics_output.json`.

## Key Results (Nominal)

- Drag-corrected time-to-range for `R_open` through `R_max`
- Pattern diameter at 350 ft: ~24 ft (15–25 ft target)
- 25-tube salvo density at 350 ft: ≥ 2 hits/m² (swarm coverage target)
- V₀ ±5%: `R_open` shift ±10 ft (within ±30 ft limit)

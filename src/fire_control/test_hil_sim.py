"""Tests for MKFS HIL simulator stub."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from hil_sim import HILSimulator


def test_hil_vignette_strip_salvo():
    sim = HILSimulator()
    result = sim.run_vignette(136)
    assert result["final_state"] == "ARMED"
    assert result["queue_len"] == 136
    assert result["last_delay_ms"] == 270


def test_hil_stale_track_blocks_engage():
    sim = HILSimulator()
    sim.power_on_and_arm()
    sim.apply_track(True, stale_ms=600)
    assert sim.fcu.state.name == "ARMED"
    assert sim.engage_strip() == []

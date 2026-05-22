"""Tests for MKFS FCU state machine."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from fcu import FCU, FCUState


def _engage(fcu: FCU) -> FCU:
    fcu.power_on()
    fcu.safety_clear = True
    fcu.operator_arm = True
    fcu.try_arm()
    fcu.threat_cue(True)
    return fcu


def test_power_cycle():
    fcu = FCU()
    assert fcu.state == FCUState.OFF
    fcu.power_on()
    assert fcu.state == FCUState.STANDBY
    fcu.power_off()
    assert fcu.state == FCUState.OFF


def test_arm_and_engage():
    fcu = _engage(FCU())
    assert fcu.state == FCUState.ENGAGING


def test_fire_queue_136():
    fcu = _engage(FCU())
    queue = fcu.build_fire_queue(136, inter_tube_ms=2)
    assert len(queue) == 136
    assert queue[0] == (0, 0)
    assert queue[135] == (135, 270)
    assert fcu.salvo_duration_ms(136, "LAST_DITCH_FULL") == 270


def test_fire_queue_legacy_25():
    fcu = _engage(FCU())
    queue = fcu.build_fire_queue(25, inter_tube_ms=20)
    assert len(queue) == 25
    assert queue[24] == (24, 480)


def test_turret_ripple_867():
    fcu = _engage(FCU())
    decks = [list(range(i * 289, (i + 1) * 289)) for i in range(3)]
    queue = fcu.build_turret_ripple(decks, inter_tube_ms=2, inter_deck_ms=50)
    assert len(queue) == 867
    assert queue[0] == (0, 0)
    assert queue[288][1] == 576
    assert queue[289][1] == 626
    assert queue[-1][1] == 1828


def test_dual_strip_phase():
    fcu = _engage(FCU())
    strip_a = list(range(136))
    strip_b = list(range(136, 272))
    queue = fcu.build_dual_strip_phase(strip_a, strip_b, inter_tube_ms=10, module_offset_ms=20)
    assert len(queue) == 272
    assert queue[135][1] == 1350
    assert queue[136][1] == 1370


def test_salvo_complete():
    fcu = _engage(FCU())
    fcu.salvo_complete()
    assert fcu.state == FCUState.ARMED


def test_pod_empty_reload():
    fcu = _engage(FCU())
    fcu.pod_empty = True
    fcu.salvo_complete()
    assert fcu.state == FCUState.RELOAD
    fcu.pod_replaced()
    assert fcu.state == FCUState.STANDBY


def test_fault():
    fcu = FCU()
    fcu.power_on()
    fcu.module_fault = True
    fcu.tick_faults()
    assert fcu.state == FCUState.FAULT

"""Tests for MKFS FCU state machine."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from fcu import FCU, FCUState


def test_power_cycle():
    fcu = FCU()
    assert fcu.state == FCUState.OFF
    fcu.power_on()
    assert fcu.state == FCUState.STANDBY
    fcu.power_off()
    assert fcu.state == FCUState.OFF


def test_arm_and_engage():
    fcu = FCU()
    fcu.power_on()
    fcu.safety_clear = True
    fcu.operator_arm = True
    fcu.try_arm()
    assert fcu.state == FCUState.ARMED
    fcu.threat_cue(True)
    assert fcu.state == FCUState.ENGAGING


def test_fire_queue():
    fcu = FCU()
    fcu.power_on()
    fcu.safety_clear = True
    fcu.operator_arm = True
    fcu.try_arm()
    fcu.threat_cue(True)
    queue = fcu.build_fire_queue(25, inter_tube_ms=20)
    assert len(queue) == 25
    assert queue[0] == (0, 0)
    assert queue[24] == (24, 480)


def test_salvo_complete():
    fcu = FCU()
    fcu.power_on()
    fcu.safety_clear = True
    fcu.operator_arm = True
    fcu.try_arm()
    fcu.threat_cue(True)
    fcu.salvo_complete()
    assert fcu.state == FCUState.ARMED


def test_pod_empty_reload():
    fcu = FCU()
    fcu.power_on()
    fcu.safety_clear = True
    fcu.operator_arm = True
    fcu.try_arm()
    fcu.threat_cue(True)
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

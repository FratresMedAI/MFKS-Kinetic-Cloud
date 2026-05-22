"""MKFS Fire Control Unit — state machine stub (Phase 2)."""

from __future__ import annotations

from enum import Enum, auto


class FCUState(Enum):
    OFF = auto()
    STANDBY = auto()
    ARMED = auto()
    ENGAGING = auto()
    RELOAD = auto()
    FAULT = auto()


class FCU:
    """Minimal FCU state machine per FCU_STATE_MACHINE.md."""

    def __init__(self) -> None:
        self.state = FCUState.OFF
        self.safety_clear = False
        self.operator_arm = False
        self.threat_valid = False
        self.module_fault = False
        self.fire_fail = False
        self.pod_empty = False
        self.fault_cleared = False

    def power_on(self) -> FCUState:
        if self.state == FCUState.OFF:
            self.state = FCUState.STANDBY
        return self.state

    def power_off(self) -> FCUState:
        self.state = FCUState.OFF
        return self.state

    def operator_safe(self) -> FCUState:
        if self.state == FCUState.ARMED:
            self.state = FCUState.STANDBY
        return self.state

    def try_arm(self) -> FCUState:
        if self.state == FCUState.STANDBY and self.operator_arm and self.safety_clear:
            self.state = FCUState.ARMED
        return self.state

    def threat_cue(self, valid: bool) -> FCUState:
        self.threat_valid = valid
        if self.state == FCUState.ARMED and valid:
            self.state = FCUState.ENGAGING
        return self.state

    def salvo_complete(self) -> FCUState:
        if self.state == FCUState.ENGAGING:
            self.state = FCUState.ARMED if not self.pod_empty else FCUState.RELOAD
        return self.state

    def pod_replaced(self) -> FCUState:
        if self.state == FCUState.RELOAD:
            self.pod_empty = False
            self.state = FCUState.STANDBY
        return self.state

    def tick_faults(self) -> FCUState:
        if self.module_fault or self.fire_fail:
            self.state = FCUState.FAULT
        elif self.state == FCUState.FAULT and self.fault_cleared:
            self.state = FCUState.STANDBY
            self.fault_cleared = False
        return self.state

    def build_fire_queue(self, tube_count: int, inter_tube_ms: int = 20) -> list[tuple[int, int]]:
        """Return (tube_id, delay_ms) pairs for a full salvo."""
        if self.state != FCUState.ENGAGING:
            return []
        return [(i, i * inter_tube_ms) for i in range(tube_count)]

    def build_salvo(self, tube_ids: list[int], profile: str = "SWARM_WIDE") -> list[tuple[int, int]]:
        """Build fire queue for addressed tubes. profile sets inter-tube delay."""
        if self.state != FCUState.ENGAGING:
            return []
        delays = {
            "LAST_DITCH_FULL": 2,
            "TURRET_RIPPLE": 50,
            "DUAL_STRIP_PHASE": 20,
            "SWARM_BURST": 5,
            "SWARM_WIDE": 10,
            "SWARM_FOCUS": 10,
            "SECTOR_LEFT": 10,
            "SECTOR_RIGHT": 10,
        }
        ms = delays.get(profile, 10)
        return [(tid, i * ms) for i, tid in enumerate(tube_ids)]


if __name__ == "__main__":
    fcu = FCU()
    fcu.power_on()
    fcu.safety_clear = True
    fcu.operator_arm = True
    fcu.try_arm()
    fcu.threat_cue(True)
    queue = fcu.build_fire_queue(136, inter_tube_ms=2)
    fcu.salvo_complete()
    print(f"State after salvo: {fcu.state.name}")
    print(f"Fire queue (first 5): {queue[:5]}")

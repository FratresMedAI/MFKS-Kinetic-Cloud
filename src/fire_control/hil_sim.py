"""MKFS FCU hardware-in-loop simulator stub (Phase 8)."""

from __future__ import annotations

from fcu import FCU, FCUState


class HILSimulator:
    """Minimal track-in → fire-queue-out simulator for one engagement vignette."""

    def __init__(self) -> None:
        self.fcu = FCU()
        self.track_stale_ms = 0

    def power_on_and_arm(self) -> FCUState:
        self.fcu.power_on()
        self.fcu.safety_clear = True
        self.fcu.operator_arm = True
        self.fcu.try_arm()
        return self.fcu.state

    def apply_track(self, valid: bool, stale_ms: int = 0) -> FCUState:
        self.track_stale_ms = stale_ms
        if stale_ms > 500:
            return self.fcu.state
        return self.fcu.threat_cue(valid)

    def engage_strip(self, tube_count: int = 136) -> list[tuple[int, int]]:
        if self.fcu.state != FCUState.ENGAGING:
            return []
        return self.fcu.build_fire_queue(tube_count, inter_tube_ms=2)

    def run_vignette(self, tube_count: int = 136) -> dict:
        self.power_on_and_arm()
        self.apply_track(True)
        queue = self.engage_strip(tube_count)
        self.fcu.salvo_complete()
        return {
            "final_state": self.fcu.state.name,
            "queue_len": len(queue),
            "first_tube": queue[0] if queue else None,
            "last_delay_ms": queue[-1][1] if queue else None,
        }

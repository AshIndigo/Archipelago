from typing import Optional

from pymem import Pymem


class GameManager:

    process: Optional[Pymem]
    is_process_running: bool

    def __init__(self):
        self.process = None
        self.game_state_manager = None
        self.goal_completed = None
        self.completed_locations_queue = None
        self.received_items_queue = None
        self.received_items = None

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem("dmc3.exe")
            self.is_process_running = True
        except Exception:
            return False

        return True

    def is_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            return False

        return True

    def update(self):
        pass
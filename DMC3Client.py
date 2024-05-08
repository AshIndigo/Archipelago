import asyncio
import multiprocessing
from typing import List, Optional, Dict

import CommonClient
import NetUtils
import Utils
from CommonClient import CommonContext, server_loop, ClientCommandProcessor, get_base_parser
from worlds.dmc3 import DMC3Location, DMC3Item, dmc3_items
from worlds.dmc3.GameManager import GameManager

SYSTEM_MESSAGE_ID = 0

script_version: int = 2

debugEnabled = False
locations_checked = []
items_sent = []
itemIndex = 1


class DMC3CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

    def _cmd_dmc(self) -> None:
        """Attach to an open DMC3 process."""
        result: bool = self.ctx.game_controller.open_process_handle()

        if result:
            self.ctx.process_attached_at_least_once = True
            self.output("Successfully attached to DMC3 process.")
        else:
            self.output("Failed to attach to DMC3 process.")


class DMC3Context(CommonContext):
    command_processor = DMC3CommandProcessor
    controller_task = None
    game = "Devil May Cry 3"
    game_controller: GameManager
    controller_task: Optional[asyncio.Task]
    process_attached_at_least_once: bool
    can_display_process_message: bool

    def __init__(self, server_address, password):
        super(DMC3Context, self).__init__(server_address, password)
        self.location_table = {}
        self.version_warning = False
        self.slot_data = dict()
        self.sent_hints = []
        self.auth = "AshIndigo"  # todo
        self.items_handling = 0b101
        self.process_attached_at_least_once = False
        self.can_display_process_message = True

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(DMC3Context, self).server_auth(password_requested)
        await self.send_connect()

    async def controller(self):
        while not self.exit_event.is_set():
            await asyncio.sleep(0.1)

            # Enqueue Received Item Delta
            network_item: NetUtils.NetworkItem
            for network_item in self.items_received:
                item: DMC3Item = dict((v, k) for k, v in {name: id for id, name in enumerate(dmc3_items, 451000)})[
                    network_item.item]

                if item not in self.game_controller.received_items:
                    if item not in self.game_controller.received_items_queue:
                        self.game_controller.received_items_queue.append(item)

            # Game Controller Update
            if self.game_controller.is_running():
                self.game_controller.update()
                self.can_display_process_message = True
            else:
                process_message: str

                if self.process_attached_at_least_once:
                    process_message = (
                        "Lost connection to DMC3 process. Please restart the game and use the /dmc "
                        "command to reattach."
                    )
                else:
                    process_message = (
                        "Please use the /dmc command to attach to a running DMC3 process."
                    )

                if self.can_display_process_message:
                    CommonClient.logger.info(process_message)
                    self.can_display_process_message = False

            # Send Checked Locations
            checked_location_ids: List[int] = list()

            while len(self.game_controller.completed_locations_queue) > 0:
                location: DMC3Location = self.game_controller.completed_locations_queue.popleft()
                location_id: int = self.location_name_to_id[location.value]

                checked_location_ids.append(location_id)

            await self.send_msgs([
                {
                    "cmd": "LocationChecks",
                    "locations": checked_location_ids
                }
            ])

            # Check for Goal Completion
            if self.game_controller.goal_completed:
                await self.send_msgs([
                    {
                        "cmd": "StatusUpdate",
                        "status": CommonClient.ClientStatus.CLIENT_GOAL
                    }
                ])

    def run_gui(self):
        from kvui import GameManager

        class DMC3Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Devil May Cry 3 Client"

        self.ui = DMC3Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_package(self, cmd: str, args: dict):
        if cmd == 'Connected':
            self.slot_data = args.get("slot_data", {})
            print(self.slot_data)


def launch():
    Utils.init_logging("DMC3Client")

    async def main():
        parser = get_base_parser()
        args = parser.parse_args()

        ctx = DMC3Context(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="DMC3GameController")

        if CommonClient.gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        ctx.server_address = None
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(main())
    colorama.deinit()

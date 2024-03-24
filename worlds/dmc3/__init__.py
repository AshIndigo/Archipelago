from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import launch_subprocess, components, Component, Type
from worlds.dmc3.Options import dmc3_options


def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="DMC3Client")


components.append(Component("Devil May Cry 3 Client", "DMC3Client", func=launch_client, component_type=Type.CLIENT))


class DevilMayCry3Web(WebWorld):
    bug_report_page = "https://github.com/AshIndigo/Devil-May-Cry-3-Archipelago/issues"
    theme = "stone"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Devil May Cry 3 randomizer on your computer.",
        "English",
        "en_setup.md",
        "setup/en",
        ["AshIndigo"]
    )

    tutorials = [setup_en]
    options_presets = {
        "Default": {
            "enable_dlc": True
        }
    }


class DevilMayCry3World(World):
    """
        TODO Write Cool stuff here
        """

    game: str = "Devil May Cry 3"
    option_definitions = dmc3_options
    topology_present: bool = True
    web = DevilMayCry3Web()
    data_version = 8
    base_id = 100000
    required_client_version = (0, 4, 2)

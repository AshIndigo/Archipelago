from typing import Dict, Any

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import item_descriptions, DMC1Item, dmc1_items, ItemData, junk_pool, item_name_groups
from .Locations import location_descriptions, DMC1Location, \
    dmc1_locations, location_name_groups
from .Options import DMC1Options
from .Regions import dmc1_regions, setup_linear_goal
from .Rules import *
from .Skills import *
from ..LauncherComponents import Component, components, launch as launch_component, Type

DEBUG = False


def launch_client(*args: str):
    from .DMC1Client import launch
    launch_component(launch, name="DMC1Client", args=args)


components.append(Component("Devil May Cry 1 Client", "DMC1Client", func=launch_client,
                            component_type=Type.CLIENT, game_name="Devil May Cry 1"))


# icon_paths['dante'] = local_path('data', 'dante.png')

class DevilMayCry1Web(WebWorld):
    rich_text_options_doc = True
    location_descriptions = location_descriptions
    item_descriptions = item_descriptions
    bug_report_page = "https://github.com/AshIndigo/Devil-May-Cry-1-Archipelago/issues"
    theme = "stone"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Devil May Cry 1 randomizer on your computer.",
        "English",
        "en_setup.md",
        "setup/en",
        ["AshIndigo"]
    )

    tutorials = [setup_en]
    options_presets = Options.dmc1_presets


class DevilMayCry1World(World):
    """
        Devil May Cry 1 is the first Devil May Cry game
        """

    game = "Devil May Cry 1"
    options: DMC1Options
    options_dataclass = DMC1Options
    topology_present: bool = True
    web = DevilMayCry1Web()
    base_id = 1
    dmc1_mission_order = [i for i in range(1, 24)]

    item_name_to_id = {name: data.code for name, data in (dmc1_items | weapon_skills).items() if
                       data.code is not None}

    location_name_to_id = {name: id for id, name in
                           enumerate(dmc1_locations, base_id)}
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    set_rules = Rules.set_dmc1_rules
    create_regions = Regions.create_regions

    def __init__(self, world, player: int):
        super(DevilMayCry1World, self).__init__(world, player)

    def create_item(self, item: str) -> DMC1Item:
        item = DMC1Item(item, (dmc1_items | weapon_skills)[item].classification,
                        self.item_name_to_id[item],
                        self.player)
        return item

    def generate_early(self) -> None:
        gun = "Handgun"
        match self.options.start_gun.value:
            case 0:
                gun = "Handgun"
            case 1:
                gun = "Shotgun"
            case 2:
                gun = "Needlegun"
            case 3:
                gun = "Grenade Launcher"
            case 4:
                gun = "Nightmare Beta"
        melee = "Force Edge"
        match self.options.start_melee.value:
            case 0:
                melee = "Force Edge"
            case 1:
                melee = "Alastor"
            case 2:
                melee = "Ifrit"
            case 3:
                melee = "Sparda"
        self.multiworld.push_precollected(self.create_item(gun))
        self.multiworld.push_precollected(self.create_item(melee))
        if self.options.goal == self.options.goal.option_random_order:
            match self.options.mission_shuffle.value:
                case self.options.mission_shuffle.option_rng:
                    self.random.shuffle(self.dmc3_mission_order)
                case self.options.mission_shuffle.option_grouped:
                    self.grouped_mission_order()
                case self.options.mission_shuffle.option_weighted:
                    self.weighted_mission_order()

            print(f"Mission Order: {self.dmc3_mission_order}")

    def create_items(self) -> None:
        # Setup exclude list so dupes aren't in pool
        exclude = [item for item in self.multiworld.precollected_items[self.player]]
        # Proper Purple+Blue orb counts are added below
        exclude.append(self.create_item("Purple Orb"))
        exclude.append(self.create_item("Blue Orb"))
        exclude.append(self.create_item("Blue Orb Fragment"))
        # Consumables are filler, don't add them to the pool
        for item in junk_pool.keys():
            exclude.append(self.create_item(item))

        # Initial item pool before excludes are taken out
        initial_item_pool = []
        for item in map(self.create_item, dmc1_items):
            initial_item_pool.append(item)
        # Skill handling
        if self.options.randomize_skills:
            # Adds all skills to the pool
            for skill in map(self.create_item, weapon_skills):
                initial_item_pool.append(skill)
            # Progressive skills need a second copy to reach max level
            for skill in map(self.create_item, self.item_name_groups["upgradable_skills"]):
                initial_item_pool.append(skill)

        final_item_pool = []
        # Add enough blue and purple to ensure max magic+hp can be obtained
        final_item_pool.extend([self.create_item("Blue Orb") for _ in range(20)])  # Max HP is 20k, start with 6k
        # Max Magic is 10k
        final_item_pool.extend([self.create_item("Purple Orb") for _ in range(7)])  # Add 7 orbs no matter what

        # Remaining 3 if Purple mode is on, otherwise DT Item will be used to reach 10k magic
        if self.options.purple_orb_mode:
            final_item_pool.extend([self.create_item("Purple Orb") for _ in range(3)])

        # If we have 10 purple orbs in world and don't need the DT item to unlock DT, remove it from the world
        # If purple mode is off, then we need the DT item, and if DT mode is on, we need the DT item
        if self.options.purple_orb_mode and not self.options.devil_trigger_mode:
            exclude.append(self.create_item("Devil Trigger"))

        # Remove any items that are in the excluded pool
        for item in initial_item_pool:
            if item in exclude:
                exclude.remove(item)  # this is destructive. create unique list above
            else:
                final_item_pool.append(item)

        if DEBUG:
            print("Item pool len: {}".format(len(final_item_pool)))
            print("Location count: {}".format(len(dmc1_locations)))
        while len(final_item_pool) < len(self.multiworld.get_unfilled_locations(self.player)):
            final_item_pool.append(self.create_item(self.get_filler_item_name()))
        self.multiworld.itempool += final_item_pool

    def get_filler_item_name(self) -> str:
        return self.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]

    def fill_slot_data(self) -> Dict[str, Any]:
        data = {
            'starter_items': [item.name for item in self.multiworld.precollected_items[self.player]],
            'generated_version': self.world_version
        }
        if self.options.goal == self.options.goal.option_random_order:
            data.update({'mission_order': self.dmc3_mission_order})
        data.update(self.options.as_dict("start_melee", "start_gun",
                                         "randomize_skills", "purple_orb_mode",
                                         "devil_trigger_mode", "goal",
                                         "death_link", toggles_as_bools=True))
        return data
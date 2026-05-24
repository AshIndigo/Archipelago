from typing import TypedDict

from BaseClasses import Region, ItemClassification
from .Items import DMC1Item
from .Locations import DMC1Location, dmc1_locations, default_shop_locations


class Mission(TypedDict):
    secret: list


dmc1_regions: dict[int, Mission] = {
    # First number is mission number, 2nd is secret mission indexes. 0 if the mission doesn't have one
    1: Mission(secret=[0]),
    2: Mission(secret=[0]),
    3: Mission(secret=[1]),
    4: Mission(secret=[2, 3, 4]),  # Why? (Also SM4 is the sucky one shot one)
    5: Mission(secret=[0]),
    6: Mission(secret=[5]),
    7: Mission(secret=[0]),
    8: Mission(secret=[0]),
    9: Mission(secret=[0]),
    10: Mission(secret=[0]),
    11: Mission(secret=[6]),
    12: Mission(secret=[0]),
    13: Mission(secret=[0]),
    14: Mission(secret=[7]),  # Technically its part of the intermission, but we'll count it as M14
    15: Mission(secret=[8]),
    16: Mission(secret=[9, 10]),
    17: Mission(secret=[11]),
    18: Mission(secret=[0]),
    19: Mission(secret=[0]),
    20: Mission(secret=[0]),
    21: Mission(secret=[12]),
    22: Mission(secret=[0]),
    23: Mission(secret=[0]),
}


# For a linear mission order (1-20 or whatever random order AP comes up with)
def setup_linear_goal(mission: int, mission_name: str, current_region: Region, world, menu_region):
    if mission == world.dmc1_mission_order[0]:
        menu_region.connect(current_region)
    else:
        idx = world.dmc1_mission_order.index(mission)
        if idx > 0:
            prev_mission = world.dmc1_mission_order[idx - 1]
            world.get_region(f"Mission #{prev_mission}").add_exits([mission_name])

    if world.dmc1_mission_order[22] == mission:
        victory_loc = DMC1Location(world.player, "Final Mission", None,
                                   current_region)
        victory_loc.place_locked_item(
            DMC1Item("Complete", ItemClassification.progression, None, world.player))
        current_region.locations.append(victory_loc)


def setup_all_goal(mission: int, mission_name: str, current_region: Region, world, menu_region):
    menu_region.connect(current_region)
    if mission == 1:
        victory_loc = DMC1Location(world.player, "Final Mission", None,
                                   current_region)
        victory_loc.place_locked_item(
            DMC1Item("Complete", ItemClassification.progression, None, world.player))
        menu_region.locations.append(victory_loc)


def create_regions(self) -> None:
    # Menu
    menu_region = Region("Menu", self.player, self.multiworld)
    if self.options.shop_orb_checks:
        menu_region.add_locations({
            m_loc: self.location_name_to_id[m_loc]
            for m_loc in [loc for loc in default_shop_locations]
        }, DMC1Location)
    self.multiworld.regions.append(menu_region)
    # Setup missions+secret missions
    for mission_idx in range(23):
        mission = self.dmc1_mission_order[mission_idx]
        data = dmc1_regions[mission]
        mission_name = f"Mission #{mission}"

        # Generic mission stuff
        current_region = Region(mission_name, self.player, self.multiworld)
        current_region.add_locations({
            m_loc: self.location_name_to_id[m_loc]
            for m_loc in [loc for loc in dmc1_locations if dmc1_locations[loc].mission_number == mission]
        }, DMC1Location)

        if mission_idx == 0:
            current_region.add_locations({
                m_loc: self.location_name_to_id[m_loc]
                for m_loc in [loc for loc in dmc1_locations if dmc1_locations[loc].mission_number == 0]
            }, DMC1Location)

        # current_region.add_event(f"Finish Mission #{mission}", None, lambda state, mi=mission: state.can_reach_location(f"Mission #{mi} Complete", self.player), DMC1Location, DMC1Item)

        current_region.add_exits(["Menu"])
        self.multiworld.regions.append(current_region)

        # Goal specific stuff
        match self.options.goal.value:
            case self.options.goal.option_standard:
                setup_linear_goal(mission, mission_name, current_region, self, menu_region)
            case self.options.goal.option_all:
                setup_all_goal(mission, mission_name, current_region, self, menu_region)
            case self.options.goal.option_random_order:
                setup_linear_goal(mission, mission_name, current_region, self, menu_region)

        # Secret mission handling
        if data["secret"] != [0]:
            for secret in data["secret"]:

                secret_mission_name = f"Secret Mission #{secret}"
                secret_region = Region(secret_mission_name, self.player, self.multiworld)
                if secret != 12:
                    secret_region.locations.append(DMC1Location(self.player, secret_mission_name,
                                                                self.location_name_to_id.get(
                                                                    secret_mission_name, None), current_region))
                else:
                    secret_mission_name_blue = "Secret Mission #12 - Blue Orb"
                    secret_mission_name_bangle = "Secret Mission #12 - Bangle of Time"
                    bangle_loc = DMC1Location(self.player, secret_mission_name_bangle,
                                              self.location_name_to_id.get(
                                                  secret_mission_name_bangle, None), current_region)
                    blue_loc = DMC1Location(self.player, secret_mission_name_blue,
                                            self.location_name_to_id.get(
                                                secret_mission_name_blue, None), current_region)
                    secret_region.locations.append(bangle_loc)
                    secret_region.locations.append(blue_loc)
                current_region.connect(secret_region)
                self.multiworld.regions.append(secret_region)
                secret_region.add_exits(["Menu", mission_name])

from worlds.generic.Rules import add_rule


# Generic Location rules, independent of goal
def add_generic_rules(world):
    pass


# What location needs to be reached/items are needed to finish a mission
def add_mission_complete_rules(world):
    pass


def set_dmc1_rules(dmc1_world) -> None:
    add_generic_rules(dmc1_world)
    add_mission_complete_rules(dmc1_world)

    dmc1_world.multiworld.completion_condition[dmc1_world.player] = lambda state: state.has("Complete",
                                                                                            dmc1_world.player)

    add_rule(dmc1_world.multiworld.get_location("Final Mission", dmc1_world.player), lambda state:
    state.can_reach_location(f"Mission #{dmc1_world.dmc1_mission_order[-1]} Complete", dmc1_world.player)),

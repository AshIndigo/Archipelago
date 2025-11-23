from worlds.generic.Rules import add_rule

# For linear mission orders
def add_mission_order_rules(world):
    for idx in range(22):
        mission_idx = world.dmc1_mission_order[idx]
        add_rule(
            world.multiworld.get_entrance(f"Mission #{mission_idx} -> Mission #{world.dmc1_mission_order[idx+1]}", world.player),
            lambda state, i=mission_idx: state.can_reach_location(f"Mission #{i} Complete", world.player))

# Generic Location rules, independent of goal
def add_generic_rules(world):
    # I think the rusty key is needed for frag 5
    add_rule(world.multiworld.get_location("Mission #1 - Blue Orb Fragment #5", world.player),
             lambda state: state.has("Rusty Key (Mission #1)", world.player))
    # Rusty Key #2 is needed to get to the Staff of Judgement
    add_rule(world.multiworld.get_location("Mission #2 - Staff of Judgement", world.player),
             lambda state: state.has("Rusty Key (Mission #2)", world.player))
    # Death Sentence is used to unlock the bust holding the Melancholy Soul
    add_rule(world.multiworld.get_location("Mission #4 - Melancholy Soul", world.player),
             lambda state: state.has("Death Sentence", world.player))
    # Last Rusty Key is used to unlock the door to the Guiding Light
    add_rule(world.multiworld.get_location("Mission #6 - Guiding Light", world.player),
             lambda state: state.has("Rusty Key (Mission #6)", world.player))
    # Might need the trident to get to the grenade launcher in m8, dont think so though?
    add_rule(world.multiworld.get_location("Mission #11 - Chalice", world.player),
             lambda state: state.has("Sign of Chastity", world.player))
    # Might need the emblem shield for some items M14
    # .
    add_rule(world.multiworld.get_location("Mission #15 - Wheel of Destiny", world.player),
             lambda state: state.has("Pair of Lances", world.player))
    # .
    add_rule(world.multiworld.get_location("Mission #15 - Pair of Lances", world.player),
             lambda state: state.has("Luminite", world.player))
    # M16 Wheel of Destiny
    # Elixir needs Egg
    add_rule(world.multiworld.get_location("Mission #18 - Elixir", world.player),
             lambda state: state.has("Philosopher's Egg", world.player))
    add_rule(world.multiworld.get_location("Mission #19 - Philosopher's Stone", world.player),
             lambda state: state.has("Elixir", world.player))

# What location needs to be reached/items are needed to finish a mission
def add_mission_complete_rules(world):
    # Rusty Key #1 is needed
    add_rule(world.multiworld.get_location("Mission #1 Complete", world.player),
             lambda state: state.has("Rusty Key (Mission #1)", world.player))
    # The Staff of Judgement is used to open the door that Alastor is obtained from
    add_rule(world.multiworld.get_location("Mission #2 Complete", world.player),
             lambda state: state.has("Staff of Judgement", world.player))
    # Death Sentence is used to unlock the bust holding the Melancholy Soul which triggers the Nelo Angelo fight
    add_rule(world.multiworld.get_location("Mission #4 Complete", world.player),
             lambda state: state.has("Death Sentence", world.player))
    # Melancholy Soul is used to unlock a door at the end of the mission
    add_rule(world.multiworld.get_location("Mission #5 Complete", world.player),
             lambda state: state.has("Melancholy Soul", world.player))
    # Last Rusty Key is used to unlock the door to finish the mission
    add_rule(world.multiworld.get_location("Mission #6 Complete", world.player),
             lambda state: state.has("Rusty Key (Mission #6)", world.player))
    # Guiding Light is needed to be put in a slot
    add_rule(world.multiworld.get_location("Mission #7 Complete", world.player),
             lambda state: state.has("Guiding Light", world.player))
    # Trident is used to get back into the castle
    add_rule(world.multiworld.get_location("Mission #8 Complete", world.player),
             lambda state: state.has("Trident", world.player))
    # No item needed for M9?
    # .
    add_rule(world.multiworld.get_location("Mission #11 Complete", world.player),
             lambda state: state.has("Chalice", world.player))
    # Might make needlegun required to complete M12...
    # .
    add_rule(world.multiworld.get_location("Mission #14 Complete", world.player),
             lambda state: state.has("Emblem Shield", world.player))
    # Wheel of Destiny is needed for the start of M16, need to write a better rule for this
    add_rule(world.multiworld.get_location("Mission #16 Complete", world.player),
             lambda state: state.has("Wheel of Destiny", world.player))
    #.
    add_rule(world.multiworld.get_location("Mission #17 Complete", world.player),
             lambda state: state.has("Quicksilver", world.player))
    # Don't need the elixir? Might need the egg
    add_rule(world.multiworld.get_location("Mission #18 Complete", world.player),
             lambda state: state.has("Philosopher's Egg", world.player))
    # .
    add_rule(world.multiworld.get_location("Mission #19 Complete", world.player),
             lambda state: state.has("Philosopher's Stone", world.player))


def set_dmc1_rules(dmc1_world) -> None:
    if dmc1_world.options.goal.value != 1:
        add_mission_order_rules(dmc1_world)
    add_generic_rules(dmc1_world)
    add_mission_complete_rules(dmc1_world)

    dmc1_world.multiworld.completion_condition[dmc1_world.player] = lambda state: state.has("Complete",
                                                                                            dmc1_world.player)

    add_rule(dmc1_world.multiworld.get_location("Final Mission", dmc1_world.player), lambda state:
    state.can_reach_location(f"Mission #{dmc1_world.dmc1_mission_order[-1]} Complete", dmc1_world.player)),

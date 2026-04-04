from BaseClasses import ItemClassification
from .Items import item_name_groups, ItemData

# We are going to treat everything >=0x40 as skills
weapon_skills_dante: dict[str, ItemData] = {
    # Rebellion
    "Rebellion - Progressive Stinger": ItemData(  # Stinger Level 1
        0x40, ItemClassification.useful),
    # "Rebellion - Stinger Level 2": ItemData(
    #     0x41, ItemClassification.useful),
    "Rebellion - Drive": ItemData(
        0x42, ItemClassification.useful),
    "Rebellion - Air Hike": ItemData(
        0x43, ItemClassification.progression),

    # Cerberus (Why does Cerberus only have two purchasable skills?)
    "Cerberus - Revolver Level 2": ItemData(
        0x44, ItemClassification.useful),
    "Cerberus - Windmill": ItemData(
        0x45, ItemClassification.useful),

    # Agni and Rudra
    "Agni and Rudra - Progressive Jet Stream": ItemData(  # Jet Stream Level 2
        0x46, ItemClassification.useful),
    # "Agni and Rudra - Jet Stream Level 3": ItemData(
    #     0x47, ItemClassification.useful),
    "Agni and Rudra - Whirlwind": ItemData(
        0x48, ItemClassification.useful),
    "Agni and Rudra - Air Hike": ItemData(
        0x49, ItemClassification.progression),

    # Nevan
    "Nevan - Progressive Reverb Shock": ItemData(
        0x4A, ItemClassification.useful),
    # "Nevan - Reverb Shock Level 2": ItemData(
    #     0x4B, ItemClassification.useful),
    "Nevan - Bat Rift Level 2": ItemData(
        0x4C, ItemClassification.useful),
    "Nevan - Air Raid": ItemData(  # Needed for SM6
        0x4D, ItemClassification.progression),
    "Nevan - Volume Up": ItemData(
        0x4E, ItemClassification.useful
    ),

    # Beowulf
    "Beowulf - Straight Level 2": ItemData(
        0x4F, ItemClassification.useful),
    # Progression
    "Beowulf - Progressive Uppercut": ItemData(  # Beowulf - Beast Uppercut
        0x50, ItemClassification.useful),
    # "Beowulf - Rising Dragon": ItemData(
    #     0x51, ItemClassification.useful),
    "Beowulf - Air Hike": ItemData(
        0x52, ItemClassification.progression),
}

gun_levels_dante = {
    "Ebony & Ivory Progressive Upgrade": ItemData(0x53, ItemClassification.useful),
    "Shotgun Progressive Upgrade": ItemData(0x54, ItemClassification.useful),
    "Artemis Progressive Upgrade": ItemData(0x55, ItemClassification.useful),
    "Spiral Progressive Upgrade": ItemData(0x56, ItemClassification.useful),
    "Kalina Ann Progressive Upgrade": ItemData(0x57, ItemClassification.useful),
}

styles_dante = {
    "Progressive Trickster": ItemData(0x60, ItemClassification.progression),
    "Progressive Swordmaster": ItemData(0x61, ItemClassification.useful),
    "Progressive Gunslinger": ItemData(0x62, ItemClassification.useful),
    "Progressive Royalguard": ItemData(0x63, ItemClassification.useful),
}

gun_levels_vergil = {
    "Summoned Swords Progressive Upgrade": ItemData(0x73, ItemClassification.useful),
    "Spiral Swords": ItemData(0x75, ItemClassification.useful)
}

styles_vergil = {"Progressive Darkslayer": ItemData(0x75, ItemClassification.progression)}

weapon_skills_vergil = {
    # Yamato
    "Yamato - Progressive Rapid Slash": ItemData(0x76, ItemClassification.useful),
    "Yamato - Progressive Judgement Cut": ItemData(0x78, ItemClassification.useful),
    # Beowulf
    "Beowulf - Starfall Level 2": ItemData(0x7A, ItemClassification.useful),
    "Beowulf - Rising Sun": ItemData(0x7B, ItemClassification.useful),
    "Beowulf - Lunar Phase Level 2": ItemData(0x7C, ItemClassification.useful),
    # Force Edge
    "Force Edge - Helm Breaker Level 2": ItemData(0x7D, ItemClassification.useful),
    "Force Edge - Progressive Stinger": ItemData(0x7E, ItemClassification.useful),
    "Force Edge - Round Trip": ItemData(0x80, ItemClassification.useful),
}

combined_upgrades = weapon_skills_dante | gun_levels_dante | weapon_skills_vergil | gun_levels_vergil

from dataclasses import dataclass

from BaseClasses import ItemClassification, Item

item_descriptions = {
    "Rusty Key": "A key that opens a door",
    "Vital Star": "A consumable item that heals Dante",
}


@dataclass
class ItemData:
    code: int
    classification: ItemClassification


item_name_groups = {
    "melees": ["Force Edge", "Alastor", "Ifrit", "Sparda"],
    "guns": ["Ebony & Ivory", "Shotgun", "Needlegun", "Grenade Launcher", "Nightmare Beta"],
    "upgradable_skills": ["Alastor - Progressive Stinger", "Alastor - Progressive Vortex",
                          "Ifrit - Progressive Kick 13", "Ifrit - Progressive Meteor"]
}

dmc1_items: dict[str, ItemData] = {
    # Guns
    "Handgun": ItemData(0, ItemClassification.useful),
    "Shotgun": ItemData(1, ItemClassification.useful),
    "Needlegun": ItemData(2, ItemClassification.progression),
    "Grenade Launcher": ItemData(3, ItemClassification.useful),
    "Nightmare Beta": ItemData(4, ItemClassification.useful),
    # Orbs
    "Blue Orb": ItemData(5, ItemClassification.useful),  # 20
    "Purple Orb": ItemData(6, ItemClassification.useful),  # 7
    # Melee
    "Force Edge": ItemData(7, ItemClassification.useful),
    "Alastor": ItemData(8, ItemClassification.useful),
    "Ifrit": ItemData(9, ItemClassification.useful),
    "Sparda": ItemData(10, ItemClassification.useful),
    # Consumables
    "Vital Star": ItemData(11, ItemClassification.filler),
    "Untouchable": ItemData(12, ItemClassification.filler),
    "Devil Star": ItemData(13, ItemClassification.filler),
    "Yellow Orb": ItemData(14, ItemClassification.useful),
    "Holy Water": ItemData(15, ItemClassification.filler),
    # Key items
    "Staff of Judgement": ItemData(17, ItemClassification.progression),
    "Pride of Lion": ItemData(18, ItemClassification.progression),
    "Death Sentence": ItemData(19, ItemClassification.progression),
    "Melancholy Soul": ItemData(20, ItemClassification.progression),
    "Guiding Light": ItemData(21, ItemClassification.progression),
    "Trident": ItemData(22, ItemClassification.progression),
    "Sign of Chastity": ItemData(23, ItemClassification.progression),
    "Chalice": ItemData(24, ItemClassification.progression),
    "Staff of Hermes": ItemData(25, ItemClassification.progression),
    "Emblem Shield": ItemData(26, ItemClassification.progression),
    "Pair of Lances": ItemData(27, ItemClassification.progression),
    "Luminite": ItemData(28, ItemClassification.progression),
    "Wheel of Destiny": ItemData(29, ItemClassification.progression),
    "Quicksilver": ItemData(30, ItemClassification.progression),
    "Philosopher's Egg": ItemData(31, ItemClassification.progression),
    # Egg is turned into Elixir in M18
    "Elixir": ItemData(32, ItemClassification.progression),
    "Philosopher's Stone": ItemData(33, ItemClassification.progression),
    # Unused
    "Blue Orb Fragment": ItemData(34, ItemClassification.filler),

    "Bangle of Time": ItemData(35, ItemClassification.useful),
    # There are 3 rusty keys, don't know if it's same ID or not
    "Rusty Key (Mission #1)": ItemData(16, ItemClassification.progression),
    "Rusty Key (Mission #2)": ItemData(36, ItemClassification.progression),
    "Rusty Key (Mission #6)": ItemData(37, ItemClassification.progression),
    # DT Item, if I can control when DT is available
    # Maybe use this for Sparda DT?
    "Devil Trigger": ItemData(38, ItemClassification.progression),
}

key_items: list[str] = [
    k for k, v in dmc1_items.items() if v.code in range(17, 34) or "Rusty Key" in k
]

junk_pool: dict[str, int] = {
    "Vital Star": 6,
    "Untouchable": 2,
    "Devil Star": 4,
    "Yellow Orb": 5,
    "Holy Water": 2
}


class DMC1Item(Item):
    game = "Devil May Cry 1"

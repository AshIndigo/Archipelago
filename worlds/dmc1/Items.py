from dataclasses import dataclass

from BaseClasses import ItemClassification, Item

item_descriptions = {
    "Rusty Key (Mission #1)": "A key that opens a door in Mission #1",
    "Vital Star": "A consumable item that heals Dante",
}


@dataclass
class ItemData:
    code: int
    classification: ItemClassification


item_name_groups = {
    "melees": ["Force Edge", "Alastor", "Ifrit", "Sparda"],
    "guns": ["Handgun", "Shotgun", "Needlegun", "Grenade Launcher", "Nightmare Beta"],
    "upgradable_skills": ["Alastor - Progressive Stinger", "Alastor - Progressive Vortex",
                          "Ifrit - Progressive Kick 13", "Ifrit - Progressive Meteor"],
    "dt_capable": ["Alastor", "Ifrit"] # Technically Sparda too, but that's only in a specific case
}

dmc1_items: dict[str, ItemData] = {
    # Guns
    "Handgun": ItemData(1, ItemClassification.useful),
    "Shotgun": ItemData(2, ItemClassification.useful),
    "Needlegun": ItemData(3, ItemClassification.progression),
    "Grenade Launcher": ItemData(4, ItemClassification.useful),
    "Nightmare Beta": ItemData(5, ItemClassification.useful),
    # Orbs
    "Blue Orb": ItemData(6, ItemClassification.useful),  # 20
    "Purple Orb": ItemData(7, ItemClassification.progression),  # 7
    # Melee
    "Force Edge": ItemData(8, ItemClassification.useful),
    "Alastor": ItemData(9, ItemClassification.progression),
    "Ifrit": ItemData(10, ItemClassification.progression),
    "Sparda": ItemData(11, ItemClassification.useful),
    # Consumables
    "Vital Star": ItemData(12, ItemClassification.filler),
    "Untouchable": ItemData(13, ItemClassification.filler),
    "Devil Star": ItemData(14, ItemClassification.filler),
    "Yellow Orb": ItemData(15, ItemClassification.useful),
    "Holy Water": ItemData(16, ItemClassification.filler),

    "Bangle of Time": ItemData(17, ItemClassification.useful),

    # Key items
    "Staff of Judgement": ItemData(18, ItemClassification.progression),
    "Pride of Lion": ItemData(19, ItemClassification.progression),
    "Death Sentence": ItemData(20, ItemClassification.progression),
    "Melancholy Soul": ItemData(21, ItemClassification.progression),
    "Guiding Light": ItemData(22, ItemClassification.progression),
    "Trident": ItemData(23, ItemClassification.progression),
    "Sign of Chastity": ItemData(24, ItemClassification.progression),
    "Chalice": ItemData(25, ItemClassification.progression),
    "Staff of Hermes": ItemData(26, ItemClassification.progression),
    "Emblem Shield": ItemData(27, ItemClassification.progression),
    "Pair of Lances": ItemData(28, ItemClassification.progression),
    "Luminite": ItemData(29, ItemClassification.progression),
    "Wheel of Destiny": ItemData(30, ItemClassification.progression),
    "Quicksilver": ItemData(31, ItemClassification.progression),
    "Philosopher's Egg": ItemData(32, ItemClassification.progression),
    # Egg is turned into Elixir in M18
    "Elixir": ItemData(33, ItemClassification.progression),
    "Philosopher's Stone": ItemData(34, ItemClassification.progression),
    # Unused
    "Blue Orb Fragment": ItemData(35, ItemClassification.filler),

    # There are 3 rusty keys, don't know if it's same ID or not
    "Rusty Key (Mission #1)": ItemData(36, ItemClassification.progression),
    "Rusty Key (Mission #2)": ItemData(37, ItemClassification.progression),
    "Rusty Key (Mission #6)": ItemData(38, ItemClassification.progression),
    # DT Item, if I can control when DT is available
    # Maybe use this for Sparda DT?
    "Devil Trigger": ItemData(39, ItemClassification.progression),


    # Red Orb Filler
    "Red Orbs - 100": ItemData(41, ItemClassification.filler),
    "Red Orbs - 150": ItemData(42, ItemClassification.filler),
    "Red Orbs - 200": ItemData(43, ItemClassification.filler),
}

key_items: list[str] = [
    k for k, v in dmc1_items.items() if v.code in range(18, 34) or "Rusty Key" in k
]

junk_pool: dict[str, int] = {
    "Vital Star": 6,
    "Untouchable": 2,
    "Devil Star": 4,
    "Yellow Orb": 5,
    "Holy Water": 3,
    "Red Orbs - 100": 5,
    "Red Orbs - 150": 4,
    "Red Orbs - 200": 3,
}


class DMC1Item(Item):
    game = "Devil May Cry 1"

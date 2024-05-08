from enum import Enum
from typing import NamedTuple

from BaseClasses import Item, ItemClassification

item_descriptions = {
    "Astronomical Board": "The key item that is needed in Mission #5, normally obtained at the end of Mission #4",
    "N/A": "Not yet written"
}


class ItemData(NamedTuple):
    name: str
    code: int
    classification: ItemClassification
    description: str


dmc3_items: dict[str, ItemData] = {
    # Orbs
    "blue_orb": ItemData("blue_orb", 0x07, ItemClassification.useful, item_descriptions["N/A"]),
    "purple_orb": ItemData("purple_orb", 0x08, ItemClassification.useful, item_descriptions["N/A"]),
    "blue_fragment": ItemData("blue_fragment", 0x09, ItemClassification.useful, item_descriptions["N/A"]),

    # Consumables
    "vital_star_l": ItemData("vital_star_l", 0x10, ItemClassification.filler, item_descriptions["N/A"]),
    "vital_star_s": ItemData("vital_star_s", 0x11, ItemClassification.filler, item_descriptions["N/A"]),
    "devil_star": ItemData("devil_star", 0x12, ItemClassification.filler, item_descriptions["N/A"]),
    "holy_water": ItemData("holy_water", 0x13, ItemClassification.filler, item_descriptions["N/A"]),

    # Melee
    "rebellion": ItemData("rebellion", 0x16, ItemClassification.useful, item_descriptions["N/A"]),
    "cerberus": ItemData("cerberus", 0x17, ItemClassification.useful, item_descriptions["N/A"]),
    "agni": ("agni", 0x18, ItemClassification.useful, item_descriptions["N/A"]),
    # Tie Awakened Rebellion to DT unlock?
    "awakened_rebellion": ItemData("awakened_rebellion", 0x19, ItemClassification.useful, item_descriptions["N/A"]),
    "nevan": ItemData("nevan", 0x1A, ItemClassification.useful, item_descriptions["N/A"]),
    "beowulf": ItemData("beowulf", 0x1B, ItemClassification.useful, item_descriptions["N/A"]),

    # Guns
    "ebony_and_ivory": ItemData("ebony_and_ivory", 0x1C, ItemClassification.useful, item_descriptions["N/A"]),
    "shotgun": ItemData("shotgun", 0x1D, ItemClassification.useful, item_descriptions["N/A"]),
    "artemis": ItemData("artemis", 0x1E, ItemClassification.useful, item_descriptions["N/A"]),
    "spiral": ItemData("spiral", 0x1F, ItemClassification.useful, item_descriptions["N/A"]),
    "kalina_ann": ItemData("kalina_ann", 0x21, ItemClassification.useful, item_descriptions["N/A"]),

    # Key items
    "astroboard": ItemData("astroboard", 0x24, ItemClassification.progression, item_descriptions["Astronomical Board"]),
    "vajura": ItemData("vajura", 0x25, ItemClassification.progression, item_descriptions["N/A"]),
    # "high_roller": ItemData("high_roller", 0x26, ItemClassification.progression, item_descriptions["N/A"]),
    "soul_of_steel": ItemData("soul_of_steel", 0x27, ItemClassification.progression, item_descriptions["N/A"]),
    "essence_fighting": ItemData("essence_fighting", 0x28, ItemClassification.progression, item_descriptions["N/A"]),
    "essence_technique": ItemData("essence_technique", 0x29, ItemClassification.progression, item_descriptions["N/A"]),
    "essence_intelligence": ItemData("essence_intelligence", 0x2A, ItemClassification.progression,
                                     item_descriptions["N/A"]),
    # These 5 may be wrong
    "orihalcon_fragment": ItemData("orihalcon_fragment", 0x2B, ItemClassification.progression,
                                   item_descriptions["N/A"]),
    "sirens_shriek": ItemData("sirens_shriek", 0x2C, ItemClassification.progression, item_descriptions["N/A"]),
    "crystal_skull": ItemData("crystal_skull", 0x2E, ItemClassification.progression, item_descriptions["N/A"]),
    "ignis_fatuus": ItemData("ignis_fatuus", 0x2F, ItemClassification.progression, item_descriptions["N/A"]),
    "ambrosia": ItemData("ambrosia", 0x2F, ItemClassification.progression, item_descriptions["N/A"]),
    "stone_mask": ItemData("stone_mask", 0x30, ItemClassification.progression, item_descriptions["N/A"]),
    "neo_generator": ItemData("neo_generator", 0x31, ItemClassification.progression, item_descriptions["N/A"]),
    "haywire_neo_generator": ItemData("haywire_neo_generator", 0x32, ItemClassification.progression,
                                      item_descriptions["N/A"]),
    "full_orihalcon": ItemData("full_orihalcon", 0x33, ItemClassification.progression, item_descriptions["N/A"]),
    "orihalcon_right": ItemData("orihalcon_right", 0x34, ItemClassification.progression, item_descriptions["N/A"]),
    "orihalcon_bottom": ItemData("orihalcon_bottom", 0x35, ItemClassification.progression, item_descriptions["N/A"]),
    "orihalcon_left": ItemData("orihalcon_left", 0x36, ItemClassification.progression, item_descriptions["N/A"]),
    "golden_sun": ItemData("golden_sun", 0x37, ItemClassification.progression, item_descriptions["N/A"]),
    "onyx_moonshard": ItemData("onyx_moonshard", 0x38, ItemClassification.progression, item_descriptions["N/A"]),
    "samsara": ItemData("samsara", 0x39, ItemClassification.progression, item_descriptions["N/A"]),
}


class Type(Enum):
    MELEE = 0
    GUN = 1,
    KEY = 2


weapons: [(ItemData, Type)] = {
    (dmc3_items["rebellion"], Type.MELEE),
    (dmc3_items["cerberus"], Type.MELEE),
    (dmc3_items["agni"], Type.MELEE),
    (dmc3_items["awakened_rebellion"], Type.MELEE),
    (dmc3_items["nevan"], Type.MELEE),
    (dmc3_items["beowulf"], Type.MELEE),

    (dmc3_items["ebony_and_ivory"], Type.GUN),
    (dmc3_items["shotgun"], Type.GUN),
    (dmc3_items["artemis"], Type.GUN),
    (dmc3_items["spiral"], Type.GUN),
    (dmc3_items["kalina_ann"], Type.GUN),
}

key_items: [str] = [
    "astroboard", "vajura", "soul_of_steel", "essence_fighting", "essence_technique", "essence_intelligence",
    "orihalcon_fragment", "sirens_shriek", "crystal_skull", "ignis_fatuus", "ambrosia", "stone_mask", "neo_generator",
    "haywire_neo_generator", "full_orihalcon", "orihalcon_right", "orihalcon_left", "orihalcon_bottom", "golden_sun",
    "onyx_moonshard", "samsara"

]


class DMC3Item(Item):
    game = "Devil May Cry 3"


# def is_progression(item_name):
#     if item_name in key_items:
#         return True
#     return False


def get_item_type(self):
    return True

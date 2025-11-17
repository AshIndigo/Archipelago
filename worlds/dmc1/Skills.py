from BaseClasses import ItemClassification
from .Items import ItemData

weapon_skills: dict[str, ItemData] = {
    # Alastor
    "Alastor - Progressive Stinger": ItemData(100, ItemClassification.useful),  # Two levels
    "Alastor - Round Trip": ItemData(102, ItemClassification.useful),
    "Alastor - Air Hike": ItemData(103, ItemClassification.useful),
    "Alastor - Air Raid": ItemData(104, ItemClassification.useful),
    "Alastor - Progressive Vortex": ItemData(105, ItemClassification.useful),  # Two levels

    # Ifrit
    "Ifrit - Rolling Blaze": ItemData(107, ItemClassification.useful),
    "Ifrit - Magma Drive": ItemData(108, ItemClassification.useful),
    "Ifrit - Progressive Kick 13": ItemData(109, ItemClassification.useful),  # Two levels
    "Ifrit - Progressive Meteor": ItemData(111, ItemClassification.useful),  # Two levels
    "Ifrit - Inferno": ItemData(113, ItemClassification.useful),

}

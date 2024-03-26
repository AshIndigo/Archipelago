from typing import NamedTuple

from BaseClasses import Location

location_descriptions = {
    "Blue Orb Fragment #1": "Mission 3 before entering Cerberus' boss fight",
}


class DMC3LocationData(NamedTuple):
    name: str
    missionNumber: int
    secret: bool = False


dmc3_locations: dict[str, DMC3LocationData] = {
    "Mission #2 - Vital Star S": ("Mission #2 - Vital Star S", 2),

    "Mission #3 - Shotgun": ("Mission #3 - Shotgun", 3),
    "Mission #3 - Blue Orb Fragment #1": ("Mission #3 - Blue Orb Fragment #1", 3),
    "Mission #3 - Combat Adjudicator #1": ("Mission #3 - Combat Adjudicator #1", 3),
    "Mission #3 - Cerberus": ("Mission #3 - Cerberus", 3),

    "Mission #4 - Blue Orb Fragment #2": ("Mission #4 - Blue Orb Fragment #2", 3),
    "Mission #4 - Astronomical Board": ("Mission #4 - Astronomical Board", 4),

    "Mission #5 - Vajura": ("Mission #5 - Vajura", 5),
    "Mission #5 - Soul of Steel": ("Mission #5 - Soul of Steel", 5),
    "Mission #5 - Combat Adjudicator #2": ("Mission #5 - Combat Adjudicator #2", 5),
    "Mission #5 - Agni and Rudra": ("Mission #5 - Agni and Rudra", 5),

    "Mission #6 - Essence of Technique": ("Mission #6 - Essence of Technique", 6),
    "Mission #6 - Essence of Intelligence": ("Mission #6 - Essence of Intelligence", 6),
    "Mission #6 - Essence of Fighting": ("Mission #6 - Essence of Fighting", 6),
    "Mission #6 - Artemis": ("Mission #6 - Artemis", 6),
    "Mission #6 - Combat Adjudicator #3": ("Mission #6 - Combat Adjudicator #3", 6),

    "Mission #7 - Orichalcum Fragment": ("Mission #7 - Orichalcum Fragment", 7),
    "Mission #7 - Holy Water": ("Mission #7 - Holy Water", 7),
    "Mission #7 - Blue Orb Fragment #3": ("Mission #7 - Blue Orb Fragment #3", 7),
    "Mission #7 - Vital Star S": ("Mission #7 - Vital Star S", 7),
    "Mission #7 - Siren's Shriek": ("Mission #7 - Siren's Shriek", 7),
    "Mission #7 - Combat Adjudicator #4": ("Mission #7 - Combat Adjudicator #4", 7),
    # : ("Mission #7 - Gold/Yellow Orb", 7),
    "Mission #7 - Crystal Skull": ("Mission #7 - Crystal Skull", 7),

    "Mission #8 - Blue Orb Fragment #4": ("Mission #8 - Blue Orb Fragment #4", 8),
    "Mission #8 - Ignis Fatuus": ("Mission #8 - Ignis Fatuus", 8),
    "Mission #8 - Combat Adjudicator #5": ("Mission #8 - Combat Adjudicator #5", 8),

    "Mission #9 - Blue Orb Fragment #5": ("Mission #9 - Blue Orb Fragment #5", 9),
    "Mission #9 - Spiral": ("Mission #9 - Spiral", 9),
    "Mission #9 - Combat Adjudicator #6": ("Mission #9 - Combat Adjudicator #6", 8),
    "Mission #9 - Ambrosia": ("Mission #9 - Ambrosia", 9),
    "Mission #9 - Devil Star": ("Mission #9 - Devil Star", 9),
    "Mission #9 - Nevan": ("Mission #9 - Nevan", 9),

    "Mission #10 - Stone Mask": ("Mission #10 - Stone Mask", 10),
    "Mission #10 - Neo Generator": ("Mission #10 - Neo Generator", 10),

    "Mission #11 - Devil Star": ("Mission #11 - Devil Star", 11),
    "Mission #11 - Blue Orb Fragment #6": ("Mission #11 - Blue Orb Fragment #6", 11),
    "Mission #11 - Combat Adjudicator #7": ("Mission #11 - Combat Adjudicator #7", 11),
    "Mission #11 - Holy Water": ("Mission #11 - Holy Water", 11),

    "Mission #12 - Haywire Neo Generator": ("Mission #12 - Haywire Neo Generator", 12),
    "Mission #12 - Vital Star L": ("Mission #12 - Vital Star L", 12),
    "Mission #12 - Quicksilver": ("Mission #12 - Quicksilver", 12),

    "Mission #13 - Devil Star": ("Mission #13 - Devil Star", 13),
    "Mission #13 - Orihalcon": ("Mission #13 - Orihalcon", 13),
    "Mission #13 - Combat Adjudicator #8": ("Mission #13 - Combat Adjudicator #8", 13),

    "Mission #14 - Beowulf": ("Mission #14 - Beowulf", 14),
    "Mission #14 - Combat Adjudicator #9": ("Mission #14 - Combat Adjudicator #9", 14),
    "Mission #14 - Vital Star S": ("Mission #14 - Vital Star S", 14),
    "Mission #14 - Blue Orb Fragment #7": ("Mission #14 - Blue Orb Fragment #7", 14),
    "Mission #14 - Devil Star": ("Mission #14 - Devil Star", 14),
    "Mission #14 - Holy Water": ("Mission #14 - Holy Water", 14),

    "Mission #15 - Orihalcon Fragment #1": ("Mission #15 - Orihalcon Fragment #1", 15),
    "Mission #15 - Orihalcon Fragment #2": ("Mission #15 - Orihalcon Fragment #2", 15),
    "Mission #15 - Orihalcon Fragment #3": ("Mission #15 - Orihalcon Fragment #3", 15),
    "Mission #15 - Blue Orb Fragment #8": ("Mission #15 - Blue Orb Fragment #8", 15),

    "Mission #16 - Devil Star": ("Mission #16 - Devil Star", 16),
    "Mission #16 - Onyx Moonshard": ("Mission #16 - Onyx Moonshard", 16),
    "Mission #16 - Golden Sun": ("Mission #16 - Golden Sun", 16),
    "Mission #16 - Vital Star S": ("Mission #16 - Vital Star S", 16),
    "Mission #16 - Blue Orb Fragment #9": ("Mission #16 - Blue Orb Fragment #9", 16),
    "Mission #16 - Kalina Ann": ("Mission #16 - Kalina Ann", 16),

    "Mission #17 - Vital Star S": ("Mission #17 - Vital Star S", 17),
    "Mission #17 - Combat Adjudicator #10": ("Mission #17 - Combat Adjudicator #10", 17),
    "Mission #17 - Blue Orb Fragment #10": ("Mission #17 - Blue Orb Fragment #10", 17),
    "Mission #17 - Doppelganger": ("Mission #17 - Doppelganger", 17),

    "Mission #18 - Blue Orb Fragment #11": ("Mission #18 - Blue Orb Fragment #11", 18),

    "Mission #19 - Vital Star L": ("Mission #19 - Vital Star L", 19),
    "Mission #19 - Samsara": ("Mission #19 - Samsara", 19),

    "Beat Vergil 3": ("Beat Vergil 3", 20),

    # Secret Missions (All are Blue Orbs)
    "Secret Mission #1": ("Secret Mission #1", 21, True),
    "Secret Mission #2": ("Secret Mission #2", 22, True),
    "Secret Mission #3": ("Secret Mission #3", 23, True),
    "Secret Mission #4": ("Secret Mission #4", 24, True),
    "Secret Mission #5": ("Secret Mission #5", 25, True),
    "Secret Mission #6": ("Secret Mission #6", 26, True),
    "Secret Mission #7": ("Secret Mission #7", 27, True),
    "Secret Mission #8": ("Secret Mission #8", 28, True),
    "Secret Mission #9": ("Secret Mission #9", 29, True),
    "Secret Mission #10": ("Secret Mission #10", 31, True),
    "Secret Mission #11": ("Secret Mission #11", 32, True),
    "Secret Mission #12": ("Secret Mission #12", 33, True)
}


class DMC3Location(Location):
    game = "Devil May Cry 3"

    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        super(DMC3Location, self).__init__(player, name, code, parent)
        self.event = code is None

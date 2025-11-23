from dataclasses import dataclass

from BaseClasses import Location

location_descriptions = {
    "Mission #1 - Blue Orb Fragment #1": "It's somewhere",
}


@dataclass
class BaseLocationData:
    mission_number: int  # Mission Number, 0 if irrelevant
    room_number: int  # Room Number
    track_number: int
    default_item: int  # Default Item
    secret: bool = False  # Secret mission?
    offset: int = 0x0  # Offset
    xCoord: int = 0
    yCoord: int = 0
    zCoord: int = 0

dmc1_locations: dict[str, BaseLocationData] = ({
    # M1 Prologue
    # Track 1
    "Mission #1 - Yellow Orb": BaseLocationData(mission_number=1, room_number=33, default_item=14, track_number=1),
    "Mission #1 - Blue Orb Fragment #1": BaseLocationData(mission_number=1, room_number=33, default_item=34, track_number=1),

    # M1
    "Mission #1 - Rusty Key": BaseLocationData(mission_number=1, room_number=0, default_item=16, track_number=1),
    "Mission #1 - Blue Orb Fragment #2": BaseLocationData(mission_number=1, room_number=0, default_item=34, track_number=1), # room 0?
    "Mission #1 - Blue Orb Fragment #3": BaseLocationData(mission_number=1, room_number=0, default_item=34, track_number=1),
    "Mission #1 - Blue Orb Fragment #4": BaseLocationData(mission_number=1, room_number=0, default_item=34, track_number=1),
    "Mission #1 - Blue Orb Fragment #5": BaseLocationData(mission_number=1, room_number=0, default_item=34, track_number=1),

    # M2
    "Mission #2 - Blue Orb Fragment #6": BaseLocationData(mission_number=2, room_number=0, default_item=34, track_number=1),
    "Mission #2 - Alastor": BaseLocationData(mission_number=2, room_number=0, default_item=8, track_number=1),
    "Mission #2 - Shotgun": BaseLocationData(mission_number=2, room_number=0, default_item=1, track_number=1),
    "Mission #2 - Staff of Judgement": BaseLocationData(mission_number=2, room_number=0, default_item=17, track_number=1),
    "Mission #2 - Rusty Key": BaseLocationData(mission_number=2, room_number=0, default_item=36, track_number=1),

    # M3
    "Mission #3 - Blue Orb Fragment #7": BaseLocationData(mission_number=3, room_number=0, default_item=34, track_number=1),
    "Mission #3 - Blue Orb Fragment #8": BaseLocationData(mission_number=3, room_number=0, default_item=34, track_number=1),
    "Mission #3 - Pride of Lion": BaseLocationData(mission_number=3, room_number=0, default_item=18, track_number=1),

    # M4
    "Mission #4 - Death Sentence": BaseLocationData(mission_number=4, room_number=0, default_item=19, track_number=1),
    "Mission #4 - Melancholy Soul": BaseLocationData(mission_number=4, room_number=0, default_item=20, track_number=1),

    # M5
    "Mission #5 - Blue Orb Fragment #9": BaseLocationData(mission_number=5, room_number=0, default_item=34, track_number=1),
    "Mission #5 - Untouchable": BaseLocationData(mission_number=5, room_number=0, default_item=12, track_number=1),

    # M6
    "Mission #6 - Rusty Key": BaseLocationData(mission_number=6, room_number=0, default_item=37, track_number=1),
    "Mission #6 - Guiding Light": BaseLocationData(mission_number=6, room_number=0, default_item=21, track_number=1),
    "Mission #6 - Blue Orb Fragment #10": BaseLocationData(mission_number=6, room_number=0, default_item=34, track_number=1),

    # M7 - N/A
    # M8 Prologue - N/A

    # M8
    "Mission #8 - Blue Orb Fragment #11": BaseLocationData(mission_number=8, room_number=0, default_item=34, track_number=1),
    "Mission #8 - Blue Orb Fragment #12": BaseLocationData(mission_number=8, room_number=0, default_item=34, track_number=1),
    "Mission #8 - Grenadegun": BaseLocationData(mission_number=8, room_number=0, default_item=3, track_number=1),
    "Mission #8 - Trident": BaseLocationData(mission_number=8, room_number=0, default_item=22, track_number=1),

    # M9
    "Mission #9 - Blue Orb Fragment #13": BaseLocationData(mission_number=9, room_number=0, default_item=34, track_number=1),
    "Mission #9 - Devil Star #1": BaseLocationData(mission_number=9, room_number=0, default_item=13, track_number=1),
    "Mission #9 - Devil Star #2": BaseLocationData(mission_number=9, room_number=0, default_item=13, track_number=1),
    "Mission #9 - Yellow Orb #1": BaseLocationData(mission_number=9, room_number=0, default_item=14, track_number=1),
    "Mission #9 - Holy Water": BaseLocationData(mission_number=9, room_number=0, default_item=15, track_number=1),
    "Mission #9 - Devil Star #3": BaseLocationData(mission_number=9, room_number=0, default_item=13, track_number=1),
    "Mission #9 - Yellow Orb #2": BaseLocationData(mission_number=9, room_number=0, default_item=14, track_number=1),
    "Mission #9 - Ifrit": BaseLocationData(mission_number=9, room_number=0, default_item=9, track_number=1),
    # There's another grenade gun here...

    # M10
    "Mission #10 - Holy Water": BaseLocationData(mission_number=10, room_number=0, default_item=15, track_number=1),

    # M11
    "Mission #11 - Blue Orb Fragment #14": BaseLocationData(mission_number=11, room_number=0, default_item=34, track_number=1),
    "Mission #11 - Blue Orb Fragment #15": BaseLocationData(mission_number=11, room_number=0, default_item=34, track_number=1),
    "Mission #11 - Devil Star": BaseLocationData(mission_number=11, room_number=0, default_item=13, track_number=1),
    "Mission #11 - Sign of Chastity": BaseLocationData(mission_number=11, room_number=0, default_item=23, track_number=1),
    "Mission #11 - Chalice": BaseLocationData(mission_number=11, room_number=0, default_item=24, track_number=1),

    # M12
    "Mission #12 - Untouchable": BaseLocationData(mission_number=12, room_number=0, default_item=12, track_number=1),
    "Mission #12 - Needlegun": BaseLocationData(mission_number=12, room_number=0, default_item=2, track_number=1),
    "Mission #12 - Blue Orb Fragment #16": BaseLocationData(mission_number=12, room_number=0, default_item=34, track_number=1),
    "Mission #12 - Devil Star": BaseLocationData(mission_number=12, room_number=0, default_item=13, track_number=1),

    # M13
    "Mission #13 - Blue Orb Fragment #17": BaseLocationData(mission_number=13, room_number=0, default_item=34, track_number=1),
    "Mission #13 - Staff of Hermes": BaseLocationData(mission_number=13, room_number=0, default_item=25, track_number=1),

    # M14 Prologue
    "Mission #14 - Blue Orb Fragment #18": BaseLocationData(mission_number=14, room_number=0, default_item=34, track_number=1),
    "Mission #14 - Holy Water #1": BaseLocationData(mission_number=14, room_number=0, default_item=15, track_number=1),

    # M14
    "Mission #14 - Holy Water #2": BaseLocationData(mission_number=14, room_number=0, default_item=15, track_number=1),
    "Mission #14 - Blue Orb Fragment #19": BaseLocationData(mission_number=14, room_number=0, default_item=34, track_number=1),
    "Mission #14 - Blue Orb Fragment #20": BaseLocationData(mission_number=14, room_number=0, default_item=34, track_number=1),
    "Mission #14 - Yellow Orb": BaseLocationData(mission_number=14, room_number=0, default_item=14, track_number=1),
    "Mission #14 - Devil Star": BaseLocationData(mission_number=14, room_number=0, default_item=13, track_number=1),
    "Mission #14 - Emblem Shield": BaseLocationData(mission_number=14, room_number=0, default_item=26, track_number=1),

    # M15
    # I should maybe make these 'paths'? Instead of specific locations
    # There are two different spawns for this IIRC
    "Mission #15 - Luminite": BaseLocationData(mission_number=15, room_number=0, default_item=28, track_number=1),
    # And to make my life harder, lances and NB swap places depending on order as well IIRC
    "Mission #15 - Pair of Lances": BaseLocationData(mission_number=15, room_number=0, default_item=27, track_number=1),
    "Mission #15 - Wheel of Destiny": BaseLocationData(mission_number=15, room_number=0, default_item=29, track_number=1),
    "Mission #15 - Nightmare Beta": BaseLocationData(mission_number=15, room_number=0, default_item=4, track_number=1),
    "Mission #15 - Blue Orb Fragment #21": BaseLocationData(mission_number=15, room_number=0, default_item=34, track_number=1),
    "Mission #15 - Blue Orb Fragment #22": BaseLocationData(mission_number=15, room_number=0, default_item=34, track_number=1),
    "Mission #15 - Blue Orb Fragment #23": BaseLocationData(mission_number=15, room_number=0, default_item=34, track_number=1),
    "Mission #15 - Untouchable": BaseLocationData(mission_number=15, room_number=0, default_item=12, track_number=1),
    "Mission #15 - Holy Water": BaseLocationData(mission_number=15, room_number=0, default_item=15, track_number=1),
    "Mission #15 - Yellow Orb #1": BaseLocationData(mission_number=15, room_number=0, default_item=14, track_number=1),
    "Mission #15 - Yellow Orb #2": BaseLocationData(mission_number=15, room_number=0, default_item=14, track_number=1),

    # M16
    # Wack
    "Mission #16 - Blue Orb": BaseLocationData(mission_number=16, room_number=0, default_item=5, track_number=1),
    "Mission #16 - Blue Orb Fragment #24": BaseLocationData(mission_number=16, room_number=0, default_item=34, track_number=1),
    "Mission #16 - Blue Orb Fragment #25": BaseLocationData(mission_number=16, room_number=0, default_item=34, track_number=1),
    "Mission #16 - Blue Orb Fragment #26": BaseLocationData(mission_number=16, room_number=0, default_item=34, track_number=1),
    "Mission #16 - Blue Orb Fragment #27": BaseLocationData(mission_number=16, room_number=0, default_item=34, track_number=1),
    "Mission #16 - Untouchable": BaseLocationData(mission_number=16, room_number=0, default_item=12, track_number=1),

     # M17
    "Mission #17 - Blue Orb Fragment #28": BaseLocationData(mission_number=17, room_number=0, default_item=34, track_number=1),
    "Mission #17 - Quicksilver": BaseLocationData(mission_number=17, room_number=0, default_item=30, track_number=1),

    # M18
    "Mission #18 - Blue Orb Fragment #29": BaseLocationData(mission_number=18, room_number=0, default_item=34, track_number=1),
    "Mission #18 - Blue Orb Fragment #30": BaseLocationData(mission_number=18, room_number=0, default_item=34, track_number=1),
    "Mission #18 - Blue Orb Fragment #31": BaseLocationData(mission_number=18, room_number=0, default_item=34, track_number=1),
    "Mission #18 - Philosopher's Egg": BaseLocationData(mission_number=18, room_number=0, default_item=31, track_number=1),
    "Mission #18 - Elixir": BaseLocationData(mission_number=18, room_number=0, default_item=32, track_number=1),
    # Perfect Amulet and Sparda are automatically given here...

    # M19
    "Mission #19 - Blue Orb Fragment #32": BaseLocationData(mission_number=19, room_number=0, default_item=34, track_number=1),
    "Mission #19 - Blue Orb Fragment #33": BaseLocationData(mission_number=19, room_number=0, default_item=34, track_number=1),
    "Mission #19 - Philosopher's Stone": BaseLocationData(mission_number=19, room_number=0, default_item=33, track_number=1),

    # M20 - N/A

    # M21
    "Mission #21 - Untouchable": BaseLocationData(mission_number=21, room_number=0, default_item=12, track_number=1),
    "Mission #21 - Holy Water": BaseLocationData(mission_number=21, room_number=0, default_item=15, track_number=1),

    # M22 - N/A
    # M23 - N/A

    # Secret missions
    # I'll need to check room numbers later
    "Secret Mission #1": BaseLocationData(mission_number=24, room_number=600, secret=True, default_item=34, track_number=1),
    "Secret Mission #2": BaseLocationData(mission_number=25, room_number=601, secret=True, default_item=34, track_number=1),
    "Secret Mission #3": BaseLocationData(mission_number=26, room_number=602, secret=True, default_item=34, track_number=1),
    "Secret Mission #4": BaseLocationData(mission_number=27, room_number=603, secret=True, default_item=34, track_number=1),
    "Secret Mission #5": BaseLocationData(mission_number=28, room_number=604, secret=True, default_item=34, track_number=1),
    "Secret Mission #6": BaseLocationData(mission_number=29, room_number=605, secret=True, default_item=34, track_number=1),
    "Secret Mission #7": BaseLocationData(mission_number=30, room_number=606, secret=True, default_item=34, track_number=1),
    "Secret Mission #8": BaseLocationData(mission_number=31, room_number=607, secret=True, default_item=34, track_number=1),
    "Secret Mission #9": BaseLocationData(mission_number=32, room_number=608, secret=True, default_item=34, track_number=1),
    "Secret Mission #10": BaseLocationData(mission_number=33, room_number=609, secret=True, default_item=34, track_number=1),
    "Secret Mission #11": BaseLocationData(mission_number=34, room_number=610, secret=True, default_item=34, track_number=1),
    "Secret Mission #12 - Bangle of Time": BaseLocationData(mission_number=35, room_number=611, secret=True, default_item=35, track_number=1),
    "Secret Mission #12 - Blue Orb": BaseLocationData(mission_number=35, room_number=611, secret=True, default_item=5, track_number=1),
}|
    {"Mission #{} Complete".format(mission_numb): BaseLocationData(mission_number=mission_numb, room_number=0, default_item=0, track_number=0)
     for mission_numb in range(1,24)})

location_name_groups = {
    f"Mission #{numb}": [location for location, data in dmc1_locations.items() if data.mission_number == numb] for numb in range(1,24)
}|{"Secret Missions": [f"Secret Mission #{numb}"] for numb in range(1,12)}|{"Secret Missions": ["Secret Mission #12 - Bangle of Time", "Secret Mission #12 - Blue Orb"]}

class DMC1Location(Location):
    game = "Devil May Cry 1"

    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        super(DMC1Location, self).__init__(player, name, code, parent)
        self.event = code is None
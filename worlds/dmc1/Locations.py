from dataclasses import dataclass

from BaseClasses import Location

location_descriptions = {
    "Mission #3 - Blue Orb Fragment #1": "It's somewhere",
}


@dataclass
class BaseLocationData:
    mission_number: int  # Mission Number, 0 if irrelevant
    room_number: int  # Room Number
    default_item: int  # Default Item
    secret: bool = False  # Secret mission?
    offset: int = 0x0  # Offset
    xCoord: int = 0
    yCoord: int = 0
    zCoord: int = 0

dmc1_locations: dict[str, BaseLocationData] = ({
    # Prelude
    # Track 1
    "Mission #1 - Yellow Orb": BaseLocationData(mission_number=1, room_number=33, default_item=14),
    "Mission #1 - Blue Orb Fragment #1": BaseLocationData(mission_number=1, room_number=33, default_item=34),
    # M1 Proper
    "Mission #1 - Rusty Key": BaseLocationData(mission_number=1, room_number=0, default_item=16),
    "Mission #1 - Blue Orb Fragment #2": BaseLocationData(mission_number=1, room_number=0, default_item=34), # room 0?
    "Mission #1 - Blue Orb Fragment #3": BaseLocationData(mission_number=1, room_number=0, default_item=34),
    "Mission #1 - Blue Orb Fragment #4": BaseLocationData(mission_number=1, room_number=0, default_item=34),
    "Mission #1 - Blue Orb Fragment #5": BaseLocationData(mission_number=1, room_number=0, default_item=34),
    # M2
    "Mission #2 - Blue Orb Fragment #6": BaseLocationData(mission_number=2, room_number=0, default_item=34),
    "Mission #2 - Alastor": BaseLocationData(mission_number=2, room_number=0, default_item=8),
    "Mission #2 - Shotgun": BaseLocationData(mission_number=2, room_number=0, default_item=1),
    "Mission #2 - Staff of Judgement": BaseLocationData(mission_number=2, room_number=0, default_item=17),
    "Mission #2 - Rusty Key": BaseLocationData(mission_number=2, room_number=0, default_item=16),
    # M3


    # Secret missions
    # I'll need to check room numbers later and check item id's (M12 is bangle)
    "Secret Mission #1": BaseLocationData(mission_number=24, room_number=600, secret=True, default_item=34),
    "Secret Mission #2": BaseLocationData(mission_number=25, room_number=601, secret=True, default_item=34),
    "Secret Mission #3": BaseLocationData(mission_number=26, room_number=602, secret=True, default_item=34),
    "Secret Mission #4": BaseLocationData(mission_number=27, room_number=603, secret=True, default_item=34),
    "Secret Mission #5": BaseLocationData(mission_number=28, room_number=604, secret=True, default_item=34),
    "Secret Mission #6": BaseLocationData(mission_number=29, room_number=605, secret=True, default_item=34),
    "Secret Mission #7": BaseLocationData(mission_number=30, room_number=606, secret=True, default_item=34),
    "Secret Mission #8": BaseLocationData(mission_number=31, room_number=607, secret=True, default_item=34),
    "Secret Mission #9": BaseLocationData(mission_number=32, room_number=608, secret=True, default_item=34),
    "Secret Mission #10": BaseLocationData(mission_number=33, room_number=609, secret=True, default_item=34),
    "Secret Mission #11": BaseLocationData(mission_number=34, room_number=610, secret=True, default_item=34),
    "Secret Mission #12": BaseLocationData(mission_number=35, room_number=611, secret=True, default_item=35),
}|
    {"Mission #{} Complete".format(mission_numb): BaseLocationData(mission_number=mission_numb, room_number=0, default_item=0)
     for mission_numb in range(1,24)})

location_name_groups = {
    f"Mission #{numb}": [location for location, data in dmc1_locations.items() if data.mission_number == numb] for numb in range(1,24)
}|{"Secret Missions": [f"Secret Mission #{numb}"] for numb in range(1,13)}

class DMC1Location(Location):
    game = "Devil May Cry 1"

    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        super(DMC1Location, self).__init__(player, name, code, parent)
        self.event = code is None
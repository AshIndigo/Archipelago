from dataclasses import dataclass

from BaseClasses import Location

location_descriptions = {
    "Mission #1 - Blue Orb Fragment #1": "It's somewhere",
}


@dataclass
class BaseLocationData:
    mission_number: int = 40  # Mission Number, 40 if generic (0 is used for very start of game)
    room_number: int = 0 # Room Number
    track_number: int = 0
    default_item: int = 0 # Default Item
    secret: bool = False  # Secret mission?
    offset: int = 0x0  # Offset
    xCoord: int = 0
    yCoord: int = 0
    zCoord: int = 0

default_shop_locations: dict[str, BaseLocationData] = ({
    # Blue Orb Purchases
    "Purchase Blue Orb #1": BaseLocationData(),
    "Purchase Blue Orb #2": BaseLocationData(),
    "Purchase Blue Orb #3": BaseLocationData(),
    "Purchase Blue Orb #4": BaseLocationData(),
    "Purchase Blue Orb #5": BaseLocationData(),
    "Purchase Blue Orb #6": BaseLocationData(),
    # Purple Orb Purchases
    "Purchase Purple Orb #1": BaseLocationData(),
    "Purchase Purple Orb #2": BaseLocationData(),
    "Purchase Purple Orb #3": BaseLocationData(),
    "Purchase Purple Orb #4": BaseLocationData(),
    "Purchase Purple Orb #5": BaseLocationData(),
    "Purchase Purple Orb #6": BaseLocationData(),
    "Purchase Purple Orb #7": BaseLocationData(),
})

dmc1_locations: dict[str, BaseLocationData] = ({
    # M1 Prologue
    # Track 1
    "Mission #1 - Yellow Orb": BaseLocationData(mission_number=0, room_number=33, default_item=15, track_number=1),
    "Mission #1 - Blue Orb Fragment #1": BaseLocationData(mission_number=0, room_number=33, default_item=35, track_number=1),

    # M1
    # First marionette encounter
    "Mission #1 - Rusty Key": BaseLocationData(mission_number=1, room_number=3, default_item=36, track_number=1),
    # Main Hall
    "Mission #1 - Blue Orb Fragment #2": BaseLocationData(mission_number=1, room_number=0, default_item=35, track_number=1), # room 0?
    # Knight room passed 45 red orb door
    "Mission #1 - Blue Orb Fragment #3": BaseLocationData(mission_number=1, room_number=1, default_item=35, track_number=1),
    # Castle room that wants the trident
    "Mission #1 - Blue Orb Fragment #4": BaseLocationData(mission_number=1, room_number=28, default_item=35, track_number=1),
    # Plane room
    "Mission #1 - Blue Orb Fragment #5": BaseLocationData(mission_number=1, room_number=27, default_item=35, track_number=1),

    # M2
    # Inside desk in room with divinity statue at the start of mission
    "Mission #2 - Blue Orb Fragment #6": BaseLocationData(mission_number=2, room_number=17, default_item=35, track_number=1),
    # End of hallway at mission start
    "Mission #2 - Alastor": BaseLocationData(mission_number=2, room_number=8, default_item=9, track_number=1),
    # Inside desk in library room where scissors are first fought
    "Mission #2 - Shotgun": BaseLocationData(mission_number=2, room_number=15, default_item=2, track_number=1),
    # Room past trap door after fountain area
    "Mission #2 - Staff of Judgement": BaseLocationData(mission_number=2, room_number=15, default_item=18, track_number=1),
    # Inside painting in library room where scissors are first fought
    "Mission #2 - Rusty Key": BaseLocationData(mission_number=2, room_number=15, default_item=36, track_number=1),

    # M3
    # After bridge shatters, go back to the end with hermes sign.
    "Mission #3 - Blue Orb Fragment #7": BaseLocationData(mission_number=3, room_number=12, default_item=35, track_number=1),
    # From main door, do parkour up to main floating platform. Need stinger, air raid or maybe air hike
    "Mission #3 - Blue Orb Fragment #8": BaseLocationData(mission_number=3, room_number=12, default_item=35, track_number=1),
    # Beat up phantom after doing parkour
    "Mission #3 - Pride of Lion": BaseLocationData(mission_number=3, room_number=10, default_item=19, track_number=1),

    # M4
    # After fighting the shadow, go up the moving platform to find the item
    "Mission #3 - Death Sentence": BaseLocationData(mission_number=3, room_number=6, default_item=20, track_number=1),
    # Using death sentence on the statue releases the soul
    "Mission #4 - Melancholy Soul": BaseLocationData(mission_number=4, room_number=16, default_item=21, track_number=1),

    # M5
    # Tower by untouchable, needs some movement upgrade
    "Mission #5 - Blue Orb Fragment #9": BaseLocationData(mission_number=5, room_number=18, default_item=35, track_number=1),
    # Jump up to flatter square tower near exit hole
    "Mission #5 - Untouchable": BaseLocationData(mission_number=5, room_number=18, default_item=13, track_number=1),

    # M6
    # First door down bigger hallway in sewer pipe
    "Mission #6 - Rusty Key": BaseLocationData(mission_number=6, room_number=11, default_item=38, track_number=1),
    # Past door that needs rusty key, fight red sin scissors
    "Mission #6 - Guiding Light": BaseLocationData(mission_number=6, room_number=26, default_item=22, track_number=1),
    # From entrance to sewers to down smaller hallway till dead end, then jump
    "Mission #6 - Blue Orb Fragment #10": BaseLocationData(mission_number=6, room_number=25, default_item=35, track_number=1),

    # M7 - N/A
    # M8 Prologue - N/A

    # M8
    # Horse parkour, jump between statues
    "Mission #8 - Blue Orb Fragment #11": BaseLocationData(mission_number=8, room_number=4, default_item=35, track_number=1),
    # Past iron gate once Trident is used
    "Mission #8 - Blue Orb Fragment #12": BaseLocationData(mission_number=8, room_number=1, default_item=35, track_number=1),
    # Take it off a skeleton in lever room
    "Mission #8 - Grenadegun": BaseLocationData(mission_number=8, room_number=29, default_item=4, track_number=1),
    # Beat up Phantom #2 and jump down
    "Mission #8 - Trident": BaseLocationData(mission_number=8, room_number=4, default_item=23, track_number=1),

    # M9
    "Mission #9 - Blue Orb Fragment #13": BaseLocationData(mission_number=9, room_number=0, default_item=35, track_number=2),
    # Behind plaque in starting room
    "Mission #9 - Devil Star #1": BaseLocationData(mission_number=9, room_number=0, default_item=14, track_number=2),
    # Up two ledges on a mini stand in room past big courtyard
    "Mission #9 - Devil Star #2": BaseLocationData(mission_number=9, room_number=0, default_item=14, track_number=2),
    # In corner once you enter big room with lizards
    "Mission #9 - Yellow Orb #1": BaseLocationData(mission_number=9, room_number=1, default_item=15, track_number=2),
    # On top of smaller building in back corner
    "Mission #9 - Holy Water": BaseLocationData(mission_number=9, room_number=1, default_item=16, track_number=2),
    # Hop up ledge in room with 200 red orb door, behind secret grave. Needs Ifrit
    "Mission #9 - Devil Star #3": BaseLocationData(mission_number=9, room_number=0, default_item=14, track_number=2),
    # Up two ledges on a mini stand in room past big courtyard
    "Mission #9 - Yellow Orb #2": BaseLocationData(mission_number=9, room_number=2, default_item=15, track_number=2),
    # After obtaining Ifrit and beating up the bird, go down the stairs and hop up a ledge. Needs Ifrit
    "Mission #9 - Yellow Orb #3": BaseLocationData(mission_number=9, room_number=5, default_item=15, track_number=2),
    # Do parkour on platforms in room past courtyard.
    "Mission #9 - Ifrit": BaseLocationData(mission_number=9, room_number=2, default_item=10, track_number=2),
    # There's another grenade gun here...

    # M10
    # Follow the light till room with Kyklops, item is found in the back of the room
    "Mission #10 - Holy Water": BaseLocationData(mission_number=10, room_number=21, default_item=16, track_number=2),

    # M11
    # Down hole to sign of chastity
    "Mission #11 - Blue Orb Fragment #14": BaseLocationData(mission_number=11, room_number=30, default_item=35, track_number=2),
    # Jump up a side wall to get through broken glass wall, then jump down ledges
    "Mission #11 - Blue Orb Fragment #15": BaseLocationData(mission_number=11, room_number=6, default_item=35, track_number=2),
    # Do some jumping up a wall to get to a floating platform
    "Mission #11 - Devil Star": BaseLocationData(mission_number=11, room_number=6, default_item=14, track_number=2),
    # Down hole in courtyard-ish room, then through breakable wall and back up
    "Mission #11 - Sign of Chastity": BaseLocationData(mission_number=11, room_number=6, default_item=25, track_number=2),
    # Needs sign of chastity to unlock
    "Mission #11 - Chalice": BaseLocationData(mission_number=11, room_number=7, default_item=25, track_number=2),

    # M12
    # In first underwater section with lizard
    "Mission #12 - Untouchable": BaseLocationData(mission_number=12, room_number=1, default_item=13, track_number=5),
    # Found on ground after swimming into ship then hopping out
    "Mission #12 - Needlegun": BaseLocationData(mission_number=12, room_number=2, default_item=3, track_number=5),
    # Stinger jump off of crows nest to boat tip
    "Mission #12 - Blue Orb Fragment #16": BaseLocationData(mission_number=12, room_number=4, default_item=35, track_number=5),
    # In chest next to needlegun
    "Mission #12 - Devil Star": BaseLocationData(mission_number=12, room_number=2, default_item=14, track_number=5),

    # M13
    # Dead end room after getting staff of hermes
    "Mission #13 - Blue Orb Fragment #17": BaseLocationData(mission_number=13, room_number=10, default_item=35, track_number=5),
    # Found at mission start
    "Mission #13 - Staff of Hermes": BaseLocationData(mission_number=13, room_number=5, default_item=26, track_number=5),

    # M14 Prologue
    # Get out of boat to find fragment in nearby pool
    "Mission #14 - Blue Orb Fragment #18": BaseLocationData(mission_number=14, room_number=7, default_item=35, track_number=5),
    # In open treasure chest after leaving boat
    "Mission #14 - Holy Water #1": BaseLocationData(mission_number=14, room_number=7, default_item=16, track_number=5),

    # M14
    # Found in waterfall after taking elevator out of booby trap room
    "Mission #14 - Holy Water #2": BaseLocationData(mission_number=14, room_number=23, default_item=16, track_number=2),
    # Up ledge by gazebo, same room with holy water. Needs Air Hike
    "Mission #14 - Blue Orb Fragment #19": BaseLocationData(mission_number=14, room_number=23, default_item=35, track_number=2),
    # By red orb cache on a ledge?
    "Mission #14 - Blue Orb Fragment #20": BaseLocationData(mission_number=14, room_number=22, default_item=35, track_number=2),
    # Up a series of ledges after jumping from gazebo roof. Needs Air Hike.
    "Mission #14 - Yellow Orb": BaseLocationData(mission_number=14, room_number=23, default_item=15, track_number=2),
    # After 200 red orb door, on ledge
    "Mission #14 - Devil Star": BaseLocationData(mission_number=14, room_number=9, default_item=14, track_number=2),
    # Found on skeleton at end of spikey wall
    "Mission #14 - Emblem Shield": BaseLocationData(mission_number=14, room_number=12, default_item=27, track_number=2),

    # M15
    # Luminite can spawn at the start of either path. I probably want to have it be one location, then the mod will send it regardless of which path is taken.
    "Mission #15 - Luminite #1": BaseLocationData(mission_number=15, room_number=8, default_item=29, track_number=2), # I forgot which color this was
    "Mission #15 - Luminite #2": BaseLocationData(mission_number=15, room_number=4, default_item=29, track_number=2),
    # At end of spike traps and small parkour
    "Mission #15 - Pair of Lances": BaseLocationData(mission_number=15, room_number=11, default_item=28, track_number=2),
    # After beating griffon 2
    "Mission #15 - Wheel of Destiny": BaseLocationData(mission_number=15, room_number=11, default_item=30, track_number=2),
    # Small bit of parkour after evading traps
    "Mission #15 - Nightmare Beta": BaseLocationData(mission_number=15, room_number=11, default_item=5, track_number=2),
    # Behind broken wall in blue(?) shield path
    "Mission #15 - Blue Orb Fragment #21": BaseLocationData(mission_number=15, room_number=4, default_item=35, track_number=2),
    # Red path, jump under item pedestal
    "Mission #15 - Blue Orb Fragment #22": BaseLocationData(mission_number=15, room_number=11, default_item=35, track_number=2),
    # Stand in middle of top most bridge section in griffon arena
    "Mission #15 - Blue Orb Fragment #23": BaseLocationData(mission_number=15, room_number=3, default_item=35, track_number=2),
    # Supposedly same area as ifrit? Once it is dark
    "Mission #15 - Untouchable": BaseLocationData(mission_number=15, room_number=29, default_item=13, track_number=2),
    # Behind broken wall in blue(?) shield path, might be in barrel/crate
    "Mission #15 - Holy Water": BaseLocationData(mission_number=15, room_number=4, default_item=16, track_number=2),
    # Behind broken wall in red(?) shield path
    "Mission #15 - Yellow Orb #1": BaseLocationData(mission_number=15, room_number=8, default_item=15, track_number=2),
    # In upper portion of griffon arena
    "Mission #15 - Yellow Orb #2": BaseLocationData(mission_number=15, room_number=3, default_item=15, track_number=2),

    # M16
    # At mission start
    "Mission #16 - Blue Orb": BaseLocationData(mission_number=16, room_number=11, default_item=6, track_number=2),
    # Main castle room after wheel used
    "Mission #16 - Blue Orb Fragment #24": BaseLocationData(mission_number=16, room_number=0, default_item=35, track_number=3),
    # Jump up by large painting in hallway near div statue room
    "Mission #16 - Blue Orb Fragment #25": BaseLocationData(mission_number=16, room_number=8, default_item=35, track_number=3),
    # Bedroom portal after using staff of hermes
    "Mission #16 - Blue Orb Fragment #26": BaseLocationData(mission_number=16, room_number=16, default_item=35, track_number=3),
    # Main castle hall after wheel used
    "Mission #16 - Blue Orb Fragment #27": BaseLocationData(mission_number=16, room_number=0, default_item=35, track_number=3),
    # Bedroom portal after using staff of hermes
    "Mission #16 - Untouchable": BaseLocationData(mission_number=16, room_number=16, default_item=13, track_number=3),

    # M17
    # Stand in the center of balcony area by crank
    "Mission #17 - Blue Orb Fragment #28": BaseLocationData(mission_number=17, room_number=19, default_item=35, track_number=3),
    # Defeat the dragon! Might need alastor tbh
    "Mission #17 - Quicksilver": BaseLocationData(mission_number=17, room_number=19, default_item=31, track_number=3),

    # M18 - Need needle gun
    # In barrel in underwater portal
    "Mission #18 - Blue Orb Fragment #29": BaseLocationData(mission_number=18, room_number=24, default_item=35, track_number=3),
    # Start from bottom of room that floods with water, go up a little bit and jump to small platform. Might warrant air hike
    "Mission #18 - Blue Orb Fragment #30": BaseLocationData(mission_number=18, room_number=0, default_item=35, track_number=3),
    # From courtyard where lion was/Egg is cooked, go up to the side door and follow the hallway
    "Mission #18 - Blue Orb Fragment #31": BaseLocationData(mission_number=18, room_number=9, default_item=35, track_number=3),
    # At the top of room that fills with water when dial is activated
    "Mission #18 - Philosopher's Egg": BaseLocationData(mission_number=18, room_number=5, default_item=32, track_number=3),
    # Cook the egg
    "Mission #18 - Elixir": BaseLocationData(mission_number=18, room_number=13, default_item=33, track_number=3),
    # Perfect Amulet and Sparda are automatically given here... T3 R21??

    # M19
    # After using elixir on the mirror, go outside to find the fragment
    "Mission #19 - Blue Orb Fragment #32": BaseLocationData(mission_number=19, room_number=44, default_item=35, track_number=3),
    # Needs the fragment above, spawns in the small tower
    "Mission #19 - Blue Orb Fragment #33": BaseLocationData(mission_number=19, room_number=44, default_item=35, track_number=3),
    # Found outside after going through the elixir mirror
    "Mission #19 - Philosopher's Stone": BaseLocationData(mission_number=19, room_number=44, default_item=34, track_number=3),

    # M20 - N/A

    # M21
    # Go back to Nightmare fight room and go near entrance and wheel device
    "Mission #21 - Untouchable": BaseLocationData(mission_number=21, room_number=1, default_item=13, track_number=4),
    # Mission start room
    "Mission #21 - Holy Water": BaseLocationData(mission_number=21, room_number=2, default_item=16, track_number=4),

    # M22 - N/A
    # M23 - N/A

    # Secret missions
    # I'll need to check room numbers later
    "Secret Mission #1": BaseLocationData(mission_number=24, room_number=600, secret=True, default_item=35, track_number=1), # Room 13. Ass.
    "Secret Mission #2": BaseLocationData(mission_number=25, room_number=601, secret=True, default_item=35, track_number=1),
    "Secret Mission #3": BaseLocationData(mission_number=26, room_number=602, secret=True, default_item=35, track_number=1),
    "Secret Mission #4": BaseLocationData(mission_number=27, room_number=603, secret=True, default_item=35, track_number=1),
    "Secret Mission #5": BaseLocationData(mission_number=28, room_number=604, secret=True, default_item=35, track_number=1), ## 11
    "Secret Mission #6": BaseLocationData(mission_number=29, room_number=605, secret=True, default_item=35, track_number=1),
    "Secret Mission #7": BaseLocationData(mission_number=30, room_number=606, secret=True, default_item=35, track_number=1),
    "Secret Mission #8": BaseLocationData(mission_number=31, room_number=607, secret=True, default_item=35, track_number=1),
    "Secret Mission #9": BaseLocationData(mission_number=32, room_number=608, secret=True, default_item=35, track_number=1),
    "Secret Mission #10": BaseLocationData(mission_number=33, room_number=609, secret=True, default_item=35, track_number=1),
    "Secret Mission #11": BaseLocationData(mission_number=35, room_number=610, secret=True, default_item=34, track_number=1),
    # Right by divinity statue in M21
    # Go run around until there's the vessel wall. Do parkour and fist fight a dragon
    "Secret Mission #12 - Bangle of Time": BaseLocationData(mission_number=35, room_number=4, secret=True, default_item=17, track_number=4),
    # Wander around...
    "Secret Mission #12 - Blue Orb": BaseLocationData(mission_number=35, room_number=3, secret=True, default_item=6, track_number=4),
}|
    {"Mission #{} Complete".format(mission_numb): BaseLocationData(mission_number=mission_numb, room_number=0, default_item=0, track_number=0)
     for mission_numb in range(1,24)}|default_shop_locations)

location_name_groups = {
    f"Mission #{numb}": [location for location, data in dmc1_locations.items() if data.mission_number == numb] for numb in range(1,24)
}|{"Secret Missions": [f"Secret Mission #{numb}"] for numb in range(1,12)}|{"Secret Missions": ["Secret Mission #12 - Bangle of Time", "Secret Mission #12 - Blue Orb"]}

class DMC1Location(Location):
    game = "Devil May Cry 1"

    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        super(DMC1Location, self).__init__(player, name, code, parent)
        self.event = code is None
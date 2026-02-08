from dataclasses import dataclass

from Options import Toggle, Choice, PerGameCommonOptions, OptionCounter, Range


class StartMelee(Choice):
    """Set your starting melee weapon"""
    display_name = "Starting Melee"
    option_force_edge = 0
    option_alastor = 1
    option_ifrit = 2
    option_sparda = 3
    default = 0


class StartGun(Choice):
    """Set your starting gun"""
    display_name = "Starting Gun"
    option_handgun = 0
    option_shotgun = 1
    #option_needlegun = 2
    option_grenade_launcher = 3
    option_nightmare_beta = 4
    default = 0


class RandomizeSkills(Toggle):
    """Should weapon skills be items?"""
    display_name = "Randomize Skills"


class PurpleOrbMode(Toggle):
    """
    On: 10 Purple orbs will be added to the item pool (DT Item will be worth 0 runes if it is in the item pool)

    Off: 7 Purple orbs will be added to the item pool as well as the Devil Trigger Item (Worth 3 DT Runes)
    """
    display_name = "Purple Orb Mode"


class DevilTriggerMode(Toggle):
    """
    **On**: Devil Trigger item will be needed to access Devil Trigger (DT Item will be added to the item pool)

    **Off**: Devil Trigger will be accessible upon reaching 3 runes
    """
    display_name = "Devil Trigger Mode"


class DeathLinkSettings(Choice):
    """
    **DeathLink**: Standard DeathLink behavior.

    **HurtLink**: Sends DeathLink messages out when you die. But any received DeathLink's will cause (Difficulty Dependent) damage rather than insta kill.

    **None**: No death link features will be enabled
    """
    display_name = "Death Link"
    option_none = 0
    option_deathlink = 1
    option_hurtlink = 2
    default = 0


class DMC1Goal(Choice):
    """
    Which goal setting to use:

    **Standard**: Beat M23 in linear order M1-M23

    **All**: Beat all missions, all are unlocked at start

    **Random Order**: Beat all missions in a random linear order
    """
    display_name = "Goal"
    option_standard = 0
    option_all = 1
    option_random_order = 2
    default = 0


class MissionShuffle(Choice):
    """
    **Grouped**: All 23 missions are divided into blocks of 5 missions. The order of these blocks is then randomized

    **Pure RNG**: Leave it all up to chance. You may get Mission #1 as your first, or you may get Mission #23.
    Not recommended for Synchronous games.

    **Weighted**: Mission order is based on the provided weights
    """
    display_name = "Mission Order Setting"
    option_weighted = 0
    option_grouped = 1
    option_rng = 2
    default = 1

class MissionOrderGroup(Range):
    """
    Used for the "Grouped" Mission order setting

    Set's how many mission "groups" there are

    I.e 20/N where N is number of groups.
    """
    display_name = "Mission Order Group Count"
    range_start = 1
    range_end = 20
    default = 4

class MissionOrderWeights(OptionCounter):
    """
    Mission weight setting for the weighted mission order option

    Bigger number means it's more likely to be picked near the beginning. Smaller number means it has less of a chance of being picked.

    (If you don't know what to do, leave this alone)
    """
    display_name = "Mission Order Weights"
    valid_keys = [f"Mission #{mission_name}" for mission_name in range(1, 24)]
    min = 1
    default = {
        "Mission #1": 30,
        "Mission #2": 30,
        "Mission #3": 20,
        "Mission #4": 20,
        "Mission #5": 20,
        "Mission #6": 20,
        "Mission #7": 15,
        "Mission #8": 20,
        "Mission #9": 20,
        "Mission #10": 20,
        "Mission #11": 20,
        "Mission #12": 20,
        "Mission #13": 5,
        "Mission #14": 20,
        "Mission #15": 20,
        "Mission #16": 20,
        "Mission #17": 20,
        "Mission #18": 10,
        "Mission #19": 5,
        "Mission #20": 5,
        "Mission #21": 5,
        "Mission #22": 5,
        "Mission #23": 5,
    }


@dataclass
class DMC1Options(PerGameCommonOptions):
    start_melee: StartMelee
    start_gun: StartGun
    randomize_skills: RandomizeSkills
    death_link: DeathLinkSettings
    purple_orb_mode: PurpleOrbMode
    devil_trigger_mode: DevilTriggerMode
    goal: DMC1Goal
    mission_shuffle: MissionShuffle
    mission_weights: MissionOrderWeights
    mission_group: MissionOrderGroup

dmc1_presets = {
    "Ash's Default": {
        # "randomize_skills": True,
        # "purple_orb_mode": False,
        # "devil_trigger_mode": True,
        # "goal": "standard",
        # "exclude_locations": ["Secret Mission #3", "Secret Mission #6", "Secret Mission #7", "Secret Mission #12"]
    }
}
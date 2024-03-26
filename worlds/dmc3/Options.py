from typing import Dict

import Options
from Options import Toggle, Option, DeathLink


class RandomizeAdjudicators(Toggle):
    """Randomizes Adjudicators in the game, changing their required weapon type"""
    display_name = "Randomize Adjudicators"


class StartMelee(Options.ItemSet):
    valid_keys = ["rebellion", "cerberus", "agni_and_rudra", "nevan", "beowulf"]


class StartGun(Options.ItemSet):
    valid_keys = ["ebony_and_ivory", "shotgun", "artemis", "spiral", "kalina_ann"]


dmc3_options: Dict[str, type(Option)] = {
    "random_adjudicators": RandomizeAdjudicators,
    "start_melee": StartMelee,
    "start_gun": StartGun,
    "death_link": DeathLink
}


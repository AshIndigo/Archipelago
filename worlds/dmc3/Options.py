import typing

from Options import Toggle, Option


class EnableDLCOption(Toggle):
    """STUFF"""
    display_name = "Enable ??"


dmc3_options: typing.Dict[str, Option] = {
    "enable_dlc": EnableDLCOption
}
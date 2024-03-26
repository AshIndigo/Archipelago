from typing import TypedDict, List, Dict, NamedTuple

# class ConnectionDict(TypedDict, total=False):
#     target: str
#
#
# class RegionDict(TypedDict, total=False):
#     name: str
#     connections: List[ConnectionDict]
#
#
# class Mission(NamedTuple):
#     name: str
#     secret_num: int = 0


# regions: Dict[int, Mission] = {
#     1: Mission()
# }

dmc3_regions: [int, [int]] = {
    # First number is mission number, 2nd is secret mission indexes. 0 if the mission doesn't have one
    1: [0],
    2: [0],
    3: [1],
    4: [0],
    5: [2],
    6: [0],
    7: [3],
    8: [4],
    9: [5],
    10: [6],
    11: [7],
    12: [0],
    13: [8, 9],
    14: [0],
    15: [0],
    16: [10],
    17: [11],
    18: [12],
    19: [0],
    20: [0]

}

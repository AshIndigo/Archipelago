import json
import os
from dataclasses import asdict

from worlds.dmc1.Locations import dmc1_locations


def main():
    _dict = {k: asdict(v) for k, v in dmc1_locations.items()}
    out_file = os.path.join(".", "locations.json")
    with open(out_file, 'w') as json_file:
        json.dump(_dict, json_file)


if __name__ == '__main__':
    main()

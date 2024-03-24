from __future__ import annotations

import ModuleUpdate
ModuleUpdate.update()

from worlds.dmc3.Client import launch
import Utils

if __name__ == "__main__":
    Utils.init_logging("DMC3Client", exception_logger="Client")
    launch()

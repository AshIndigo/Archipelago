from .Items import *
from .Skills import *

item_name_to_id = {name: data.code for name, data in (dmc3_items | combined_upgrades |
                                                      dante_items | vergil_items |
                                                      styles_dante | styles_vergil).items() if
                   data.code is not None}

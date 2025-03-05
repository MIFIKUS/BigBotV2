from bots.alchemy.lists import roll_00_items
from bots.alchemy.extensions.items_grade import *
from bots.alchemy.extensions import forecast_colors

ROLL_00 = {
    'slot_to_check': 0,
    'items': roll_00_items.ITEMS,
    'min_avg': 60,
    'red_slots': None,
    'roll_items': {BLUE: 2, GREEN: 1},
    'colors': [forecast_colors.WHITE, forecast_colors.BLUE]
}



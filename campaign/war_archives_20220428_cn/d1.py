from ..campaign_war_archives.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger

MAP = CampaignMap('D1')
MAP.shape = 'H8'
MAP.camera_data = ['D2', 'D6', 'E2', 'E6']
MAP.camera_data_spawn_point = ['E6']
MAP.map_data = """
    ++ ++ ++ ME ME Me -- ++
    MB MB ++ -- -- ME -- ++
    -- -- -- -- MS -- MS ++
    -- -- Me -- -- -- -- ME
    ME __ -- Me -- ++ -- --
    Me MS ME -- MS -- -- ME
    ++ ++ -- -- ++ ME -- --
    ++ ++ ME -- ME -- SP SP
"""
MAP.map_data_loop = """
    ++ ++ ++ ME -- Me -- ++
    MB MB ++ -- -- ME -- ++
    -- -- -- -- MS -- MS ++
    ME -- Me -- ME -- -- ME
    -- __ -- Me -- ++ -- --
    Me MS ME -- MS -- -- ME
    ++ ++ -- -- ++ ME -- --
    ++ ++ ME -- ME -- SP SP
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 4, 'siren': 2},
    {'battle': 1, 'enemy': 2},
    {'battle': 2, 'enemy': 4},
    {'battle': 3, 'enemy': 2},
    {'battle': 4, 'enemy': 4},
    {'battle': 5, 'enemy': 2, 'boss': 1},
]
MAP.spawn_data_loop = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2},
    {'battle': 5, 'enemy': 1, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, \
A2, B2, C2, D2, E2, F2, G2, H2, \
A3, B3, C3, D3, E3, F3, G3, H3, \
A4, B4, C4, D4, E4, F4, G4, H4, \
A5, B5, C5, D5, E5, F5, G5, H5, \
A6, B6, C6, D6, E6, F6, G6, H6, \
A7, B7, C7, D7, E7, F7, G7, H7, \
A8, B8, C8, D8, E8, F8, G8, H8, \
    = MAP.flatten()


class Config:
    # ===== Start of generated config =====
    MAP_SIREN_TEMPLATE = ['Z2', 'Leipzig', 'PrinzEugen']
    MOVABLE_ENEMY_TURN = (2,)
    MAP_HAS_SIREN = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_MAP_STORY = True
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_AMBUSH = False
    MAP_HAS_MYSTERY = False
    # ===== End of generated config =====

    MAP_HAS_DECOY_ENEMY = True
    INTERNAL_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (120, 255 - 33),
        'width': (1.5, 10),
        'prominence': 10,
        'distance': 35,
    }
    EDGE_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (255 - 33, 255),
        'prominence': 10,
        'distance': 50,
        'wlen': 1000
    }
    HOMO_CANNY_THRESHOLD = (50, 75)
    HOMO_EDGE_COLOR_RANGE = (0, 33)
    HOMO_EDGE_HOUGHLINES_THRESHOLD = 300
    MAP_ENSURE_EDGE_INSIGHT_CORNER = 'bottom-right'
    MAP_SWIPE_MULTIPLY = (0.985, 1.004)
    MAP_SWIPE_MULTIPLY_MINITOUCH = (0.953, 0.971)
    MAP_SWIPE_MULTIPLY_MAATOUCH = (0.925, 0.942)


class Campaign(CampaignBase):
    MAP = MAP
    ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'

    def battle_0(self):
        if self.clear_siren():
            return True
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=0):
            return True

        return self.battle_default()

    def battle_5(self):
        return self.fleet_boss.clear_boss()

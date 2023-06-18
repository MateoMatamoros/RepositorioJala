from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPACESHIP, MINIATURE_TYPE

class Miniature(PowerUp):
    def __init__(self):
        super().__init__(SPACESHIP, MINIATURE_TYPE)
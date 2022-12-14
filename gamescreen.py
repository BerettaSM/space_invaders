from time import sleep
from turtle import Screen

from gamemanager import GameManager
from projectiles import Projectile

WIDTH = 1000
HEIGHT = 700


class GameScreen:

    def __init__(self, game_manager: GameManager):
        self.screen = Screen()
        self.screen.title("Space Invaders")
        self.screen.bgcolor("black")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)
        self.game_manager: GameManager = game_manager
        self.projectiles: [Projectile] = []
        self._setup()

    def exitonclick(self):
        self.screen.exitonclick()

    def update(self):
        sleep(0.03)
        self.game_manager.update_projectiles()
        self.screen.update()

    def _setup(self):
        self.screen.listen()
        self.screen.onkeypress(self.game_manager.player.move_left, "Left")
        self.screen.onkeypress(self.game_manager.player.move_right, "Right")
        self.screen.onkeypress(self.game_manager.player.shoot, "space")
        self.game_manager.screen = self
        self.game_manager.screenwidth = WIDTH
        self.game_manager.screenheight = HEIGHT

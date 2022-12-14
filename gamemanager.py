from random import random
from turtle import Turtle

from ships import Ship
from projectiles import Projectile, PlayerProjectile
from scoreboard import Scoreboard


ALIEN_COLOR = (1, 0, 0)
X_OFFSET = 75
Y_OFFSET = 50


class GameManager:

    def __init__(self, player: Ship):
        self.player: Ship = player
        self.player.game_manager = self
        self.screenwidth = None
        self.screenheight = None
        self.screen = None
        self.aliens: [Ship] = []
        self.projectiles: [Projectile] = []
        self.aliens_moving_right = True
        self.player_lives = 3
        self.scoreboard: Scoreboard = Scoreboard()

    def setup(self):
        player_y = -self.screenheight // 2 + 50
        self.player.goto(0, player_y)
        self.player.left(90)
        self.player.screen_limit = (self.screenwidth // 2) - 50
        scoreboard_x = self.screenwidth // 2 - 80
        scoreboard_y = -self.screenheight // 2 + 10
        self.scoreboard.goto(scoreboard_x, scoreboard_y)
        self.scoreboard.print_lives(self.player_lives)

    def update_projectiles(self):
        limit = (self.screenheight // 2 + 150)
        for projectile in self.projectiles:
            projectile.move()
            if abs(projectile.ycor()) > limit:
                self.projectiles.remove(projectile)

    def spawn_aliens(self):
        y_start = (self.screenheight // 2) - Y_OFFSET
        x_limit = (self.screenwidth // 2) - X_OFFSET * 2
        for y in range(y_start, (y_start - (Y_OFFSET * 3)), -Y_OFFSET):
            for x in range(0, x_limit, X_OFFSET):
                alien = Ship(ALIEN_COLOR)
                alien.goto(x, y)
                alien.right(90)
                alien.game_manager = self
                self.aliens.append(alien)
            for x in range(0 - X_OFFSET, -x_limit, -X_OFFSET):
                alien = Ship(ALIEN_COLOR)
                alien.goto(x, y)
                alien.right(90)
                alien.game_manager = self
                self.aliens.append(alien)

    def move_aliens(self):
        x_limit = (self.screenwidth // 2) - 25
        for alien in self.aliens:
            if abs(alien.xcor()) > x_limit:
                self.aliens_moving_right = not self.aliens_moving_right
                break
        steps = 3
        if self.aliens_moving_right:
            steps *= -1
        for alien in self.aliens:
            alien.goto(alien.xcor() - steps, alien.ycor())

    def make_aliens_shoot(self, probability: float = .005):
        for alien in self.aliens:
            if random() < probability:
                alien.shoot()

    def evaluate_hits(self):
        for projectile in self.projectiles:
            if isinstance(projectile, PlayerProjectile):
                for alien in self.aliens:
                    if projectile.has_hit(alien):
                        self.aliens.remove(alien)
                        self.projectiles.remove(projectile)
                        self._send_off_screen(alien)
                        self._send_off_screen(projectile)
            else:
                if projectile.has_hit(self.player):
                    self._send_off_screen(projectile)
                    self.projectiles.remove(projectile)
                    self.player_lives -= 1
                    self.scoreboard.print_lives(self.player_lives)

    def all_aliens_defeated(self):
        return len(self.aliens) == 0

    def _send_off_screen(self, entity: Turtle):
        x = self.screenwidth * 2
        y = self.screenheight * 2
        entity.goto(x, y)

from turtle import Turtle
from projectiles import Projectile, PlayerProjectile

STEPS = 10


class Ship(Turtle):

    def __init__(self, color: tuple):
        super().__init__()
        self.shape("arrow")
        self.speed("fastest")
        self.penup()
        self.ship_color = color
        self.color(color)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.game_manager = None
        self.screen_limit = None

    def move_left(self):
        new_y_coord = self.xcor() - STEPS
        if abs(new_y_coord) < self.screen_limit:
            self.goto(self.xcor() - STEPS, self.ycor())

    def move_right(self):
        new_y_coord = self.xcor() + STEPS
        if new_y_coord < self.screen_limit:
            self.goto(self.xcor() + STEPS, self.ycor())

    def shoot(self):
        p = Projectile(self.ship_color)
        p.setheading(self.heading())
        p.goto(self.xcor(), self.ycor())
        self.game_manager.projectiles.append(p)


class Player(Ship):

    def __init__(self, color: tuple):
        super().__init__(color)

    def shoot(self):
        p = PlayerProjectile(self.ship_color)
        p.setheading(self.heading())
        p.goto(self.xcor(), self.ycor())
        self.game_manager.projectiles.append(p)

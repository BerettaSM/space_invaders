from turtle import Turtle


PROJECTILE_SPEED = 10


class Projectile(Turtle):

    def __init__(self, color: tuple):
        super().__init__()
        self.shape("arrow")
        self.speed("fastest")
        self.color(color)
        self.shapesize(stretch_wid=0.15, stretch_len=0.8)
        self.penup()

    def move(self):
        self.forward(PROJECTILE_SPEED)

    def has_hit(self, entity: Turtle):
        tolerance = 30
        x1, y1 = self.pos()
        x2, y2 = entity.pos()
        x3, y3 = abs(x1 - x2), abs(y1 - y2)
        return x3 < tolerance // 2 and y3 < tolerance


class PlayerProjectile(Projectile):

    def __init__(self, color: tuple):
        super().__init__(color)

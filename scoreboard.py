from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def print_lives(self, lives):
        self.clear()
        score_string = f"Lives - {lives}"
        self.write(score_string, align=ALIGNMENT, font=FONT)

    def print_game_over_message(self, message: str):
        self.goto(x=0, y=0)
        self.write(message, align=ALIGNMENT, font=FONT)

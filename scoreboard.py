from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#F7F7EE")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()

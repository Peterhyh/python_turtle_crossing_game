from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.goto(-240, 260)
        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.write(f"Level: {self.level}", align="center",
                   font=("Arial", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Ariel", 20, "normal"))

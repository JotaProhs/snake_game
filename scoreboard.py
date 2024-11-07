from turtle import Turtle
# Constants for the values that could be changed in the future so code is not modified.
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Blueprint to create text in the game screen that inherits from turtle
    """

    def __init__(self):
        # When and object of this class is initialized, All the following values are set:
        super().__init__()
        self.color("white")
        self.penup()
        # Moves the object to the top center of the screen.
        self.goto(x=0, y=270)
        self.score = 0
        # Call to this method so the score gets printed when the game starts and
        # when the object is created.
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Characteristic with which the score is created
        """
        self.hideturtle()
        self.write(
            arg=f"Score {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT
        )

    def game_over(self):
        """
        Characteristics for how the game over message is created.
        """
        self.goto(0, 0)
        self.write(
            arg="Game Over!",
            move=False,
            align=ALIGNMENT,
            font=FONT
        )

    def increase_score(self):
        """
        adds a point to the score everytime the snake head collides with food.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

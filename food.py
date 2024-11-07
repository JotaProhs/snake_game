from turtle import Turtle
import random


class Food(Turtle):
    """
    Blueprint to create a food object, which inherits from the super class Turtle
    """
    def __init__(self):
        # super.() calls the init method in the super class so we can use all the
        # attributes and methods in the Turtle class.
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # We call this method to have some food created at the beginning of the game.
        self.refresh()

    def refresh(self):
        """
        once the snake collides with food, assigns another
        random position for the food to appear.
        """
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(random_x, random_y)
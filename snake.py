from turtle import Turtle
# Constants for the values that could be changed in the future so code is not modified.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Blueprint to create an object of the class snake
    """
    def __init__(self):
        self.name = "snake object"
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        """
        Loops through the starting positions and adds a segment to the snake,
        initially creating 3 segments to represent the snake body.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Sets the snake characteristics, defines its position and appends the segment
        to the snake_segments list in line 17. This is also the function that gets
        executed, every time we loop through STARTING_POSITIONS in the for loop in line
        26.
        """
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        """
        Extends the body of the snake by adding a segment to the latest position
        in the snake_segments
        """
        # .position() gets the position of the self.snake_segments[-1]. Then self.add_segment
        # call the function in line 29 to add the segment at the position -1 of the
        # snake_segments
        self.add_segment(self.snake_segments[-1].position())

    def __repr__(self):
        return self.name

    def move(self):
        # Moves snake[2] to position snake[1] in iteration 1 and then, on iteration 2, moves
        # snake[1] to snake[0]
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            # Getting a hold of the second to the last segment (2, 1, 0)
            # In the first iteration, we are iterating over 2, so the second to the last is 1
            # In the second iteration, we iterate over 1 so the second to the last is 0
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            # In the first iteration snake[2], which is square 3 of the snake body,
            # goes to 2 (last) - 1 = 1 (second to the last).
            # Since snake[2] moved to snake[1] and there is nothing on snake[2] anymore. The new last one
            # in the next iteration is snake[1]
            # In the second iteration snake[1], square 2, goes to snake[1] - 1 = snake[0]
            self.snake_segments[segment].goto(new_x, new_y)

        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        All the following set the heading of the snake to a particular direction
        only if the snake is not going on the opposite direction we want to head to.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


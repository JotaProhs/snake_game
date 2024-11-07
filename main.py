from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Creating and setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake, food and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Calling the methods to listen for user input
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Starting the game loop
game_is_on = True

while game_is_on:
    # Updates the screen to create the .gif image effect
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 1:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
    ):
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

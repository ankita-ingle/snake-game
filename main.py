from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()  # create a screen
screen.setup(width=600, height=600)
screen.bgcolor("#2B2B2B")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()  # update the screen once all segments have moved forward
    time.sleep(0.1)
    snake.move()

    #  Detect collision with food
    if snake.head.distance(food) < 15:  # if distance between snake and food is < than 15px
        scoreboard.update_score()
        snake.extend()
        food.refresh()

    #  Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.display_game_over()

    #  Detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.display_game_over()

screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()

score=ScoreBoard()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >280 or snake.segments[0].ycor() <-280:

        score.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass

        elif snake.segments[0].distance(segment) < 10:

            score.reset()


screen.exitonclick()
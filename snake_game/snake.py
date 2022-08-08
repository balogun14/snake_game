import time
from turtle import *
from men import *
from food import *
from score import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(" leo snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

snakes = []

game_is_on = True
9
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or -280 > snake.head.xcor() or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.snakes:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()

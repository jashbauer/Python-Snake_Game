from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")


snake = Snake()
food = Food()
scorer = Scoreboard()


game_on = True
while game_on:
    screen.update()
    time.sleep(0.10)

    scorer.update_scoreboard()
    snake.move()
    snake.turn_snake()

    if snake.food_collision(food):
        snake.increase_segment()
        food.hideturtle()
        food = Food()
        scorer.increase_score()

    if snake.game_over_checker():
        scorer.reset_score()
        snake.reset_snake()

    scorer.save_score()


screen.exitonclick()

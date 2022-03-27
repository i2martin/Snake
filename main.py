import time
from turtle import Turtle, Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
game_on = True
food = Food()
scoreboard = Scoreboard()

while game_on:
    scoreboard.update_score(scoreboard.score)
    screen.update()
    time.sleep(0.05)
    if snake.segments[0].distance(food) < 15:
        snake.add_segment()
        food.change_location()
        scoreboard.score += 1
        scoreboard.update_score(scoreboard.score)
    snake.move()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 20:
            game_on = False
    game_on = snake.collision_with_wall()
screen.exitonclick()

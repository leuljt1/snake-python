from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scor_board import ScoreBoard
import time

def egdee():
    rec = Turtle()
    rec.speed("fastest")
    rec.color("red")
    rec.hideturtle()
    rec.penup()
    rec.goto(-270, 270)
    rec.pendown()
    rec.goto(270, 270)
    rec.goto(270, -270)
    rec.goto(-270, -270)
    rec.goto(-270, 270)

egdee()
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("snake game")
screen.setup(height=600, width=600)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
score = ScoreBoard()
while is_game_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 15:
        food.refrashe()
        snake.extend()
        score.update()

    # collision with wall
    if snake.head.xcor() > 269.8 or snake.head.xcor() < -269.8 or snake.head.ycor() > 269.8 or snake.head.ycor() < -269.8:
        score.reset()
        snake.reset()
    # detect collision with tail

    for segment in snake.all_turtle[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()












screen.exitonclick()

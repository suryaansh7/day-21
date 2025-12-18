from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")



screen.tracer(0)
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.down, "s")
game_on=True
p=""
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if (ball.ycor() > 280 or ball.ycor()<-280):
        ball.collide()
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce1()
    if(ball.xcor()>400 or ball.xcor()<-400):
        ball.reset()
        ball.bounce1()




























screen.exitonclick()
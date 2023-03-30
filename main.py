from turtle import Screen,Turtle
from paddle import  Paddle
from ball import Ball
from  scoreboard import  Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)
ball=Ball()
scoreboard=Scoreboard()
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_on=True
while game_on:
    time.sleep(ball.speeding)
    screen.update()
    ball.b_move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or  ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_y()
        ball.bounce_x()
    if ball.xcor()>380:
        scoreboard.score_up_r()
        ball.restart()

    if ball.xcor()<-380:
        scoreboard.score_up_l()
        ball.restart()




screen.exitonclick()
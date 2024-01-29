from turtle import Screen
from paddle import Paddle
import time
from score import Score
from pong import Pong
import time



screen=Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor('black')
screen.title('The pong game')

pad_left=Paddle((-270,0))
pad_right=Paddle((270,0))

scoreboard_left=Score((-20,260))
scoreboard_right=Score((20,260))

ball=Pong()
scoreboard_right.in_line()
screen.listen()
screen.onkey(pad_left.up,"Up")
screen.onkey(pad_left.down,"Down")
screen.onkey(pad_right.up,"w")
screen.onkey(pad_right.down,"s")
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()

    if (ball.distance(pad_right)<50 and ball.xcor()>260) or (ball.distance(pad_left)<50 and ball.xcor()>-260):
        ball.bounce_x()
    if ball.xcor()>290:
        ball.reset()
        scoreboard_left.edit_score()
    elif ball.xcor()<-290:
        ball.reset()
        scoreboard_right.edit_score()

    # elif  ball.ycor()<-290:
    #     ball.move(-10,10)





















screen.exitonclick()
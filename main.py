from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if paddle misses the ball
    if ball.xcor() > 380:
        time.sleep(0.5)
        # left paddle score up
        ball.reset_position()
        scoreboard.l_point()
        ball.x_move = 10

    if ball.xcor() < -380:
        time.sleep(0.5)
        # right paddle score up
        ball.reset_position()
        scoreboard.r_point()
        ball.x_move = 10

    if scoreboard.l_score == 3 or scoreboard.r_score == 3:
        game_is_on = False


end_of_game = Turtle()
end_of_game.color("white")
end_of_game.hideturtle()
if scoreboard.l_score > scoreboard.r_score:
    end_of_game.write("Left player wins!")
else:
    end_of_game.write("Right player wins!", align="center", font=("Courier", 80, "normal"))

screen.exitonclick()
import turtle

window = turtle.Screen()
window.title("Pong the Ball Game!")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)


score_x = 0
score_y = 0


paddle_x = turtle.Turtle()
paddle_x.speed(0)
paddle_x.shape("square")
paddle_x.color("White")
paddle_x.shapesize(stretch_wid=5, stretch_len=1)
paddle_x.penup()
paddle_x.goto(-350, 0)

paddle_y = turtle.Turtle()
paddle_y.speed(0)
paddle_y.shape("square")
paddle_y.color("White")
paddle_y.shapesize(stretch_wid=5, stretch_len=1)
paddle_y.penup()
paddle_y.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


abhi = turtle.Turtle()
abhi.speed(0)
abhi.color("white")
abhi.penup()
abhi.hideturtle()
abhi.goto(0, 260)
abhi.write("Player A: 0     Player B: 0", align="center", font=("Roboto", 24, "normal"))


def paddle_x_up():
    y = paddle_x.ycor()
    y += 20
    paddle_x.sety(y)


window.listen()
window.onkeypress(paddle_x_up, "w")


def paddle_x_down():
    y = paddle_x.ycor()
    y -= 20
    paddle_x.sety(y)


window.listen()
window.onkeypress(paddle_x_down, "s")


def paddle_y_up():
    y = paddle_y.ycor()
    y += 20
    paddle_y.sety(y)


window.listen()
window.onkeypress(paddle_y_up, "Up")


def paddle_y_down():
    y = paddle_y.ycor()
    y -= 20
    paddle_y.sety(y)


window.listen()
window.onkeypress(paddle_y_down, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_x += 1
        abhi.clear()
        abhi.write(f"Player A: {score_x}     Player B: {score_y}", align="center", font=("Roboto", 24, "normal"))

    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_y += 1
        abhi.clear()
        abhi.write(f"Player A: {score_x}     Player B: {score_y}", align="center", font=("Roboto", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_y.ycor() + 50 and ball.ycor() > paddle_y.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_x.ycor() + 50 and ball.ycor() > paddle_x.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

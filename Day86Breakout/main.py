import turtle

# Set up the screen
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Bricks
bricks = []
colors = ["red", "orange", "green", "yellow"]
for i in range(4):  # 4 rows of bricks
    for j in range(10):  # 10 bricks per row
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(-350 + (j * 80), 200 - (i * 40))
        bricks.append(brick)

# Functions to move the paddle
def paddle_left():
    x = paddle.xcor()
    x -= 40
    if x < -350:
        x = -350
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 40
    if x > 350:
        x = 350
    paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# Game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision for the ball
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 60 and ball.xcor() < paddle.xcor() + 60):
        ball.sety(-230)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if (ball.ycor() > brick.ycor() - 10 and ball.ycor() < brick.ycor() + 10) and (ball.xcor() > brick.xcor() - 30 and ball.xcor() < brick.xcor() + 30):
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move the brick off-screen
            bricks.remove(brick)

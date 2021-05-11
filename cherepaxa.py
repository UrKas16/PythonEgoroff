import turtle

def pryamougol(x, y):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)

def povtor(x, y):
    for i in range(2):
        pryamougol(x, y)

turtle.speed(1)
turtle.up()
turtle.goto(50, 50)
turtle.down()

povtor(160, 90)
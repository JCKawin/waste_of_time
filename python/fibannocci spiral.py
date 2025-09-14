import turtle
import math

def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b
    factor = 1

    x = turtle.Turtle()
    x.speed(1000)

    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    for i in range(n):
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)

        temp = a
        a = b
        b = temp + b
n = int(input('Enter the number of iterations: '))
if n > 0:
    print(f"Fibonacci series for  {n}  elements:")
    fiboPlot(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")

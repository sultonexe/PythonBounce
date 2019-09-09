#BOUNCE BALL SIMULATOR with Python3 Programming
#Coded By @sulton.exe
#TOLONG JANGAN RECODE YA :) HARGAI SI PEMBUAT TERIMA KASIH :D

import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bounce Ball Simulator By @sulton.exe")
wn.tracer(0)

balls = []

for _ in range(20):
    balls.append(turtle.Turtle())

colors = ["white" , "red" , "purple" , "gray" , "orange" , "yellow" , "green" , "blue"]

for ball in balls:
    #draw ball
    ball.shape("circle")
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3 ,3)

    gravity = 0.1


while True:
    wn.update()

    for ball in balls:    
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        #check for wall collision
        if ball.xcor() > 300:
            ball.dx *= -1
        
        if ball.xcor() < -300:
            ball.dx *= -1

        #check for bounce
        if ball.ycor() < -300:
            ball.dy *= -1   



wn.mainloop()
# Fast try
import turtle
import pygame

pygame.mixer.init()
pygame.mixer.music.load('Amar Sonar ! Bengali Bgm Theme.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)


obj=turtle.Turtle()
obj.speed(1)

win=turtle.Screen()
win.bgcolor("white")


obj.penup()
obj.goto(-100,150)
obj.pendown()
obj.begin_fill()
obj.fillcolor("seagreen")
obj.setheading(0)
obj.forward(250)
obj.setheading(270)
obj.forward(150)
obj.setheading(180)
obj.forward(250)
obj.setheading(90)
obj.forward(150)
obj.end_fill()

obj.setheading(270)
obj.forward(122)
obj.setheading(360)

obj.penup()
obj.forward(120)
obj.pendown()

obj.begin_fill()
obj.fillcolor("red")
obj.circle(50)
obj.end_fill()

obj.setheading(180)
obj.penup()
obj.forward(120)
obj.pendown()

obj.begin_fill()
obj.fillcolor("cyan")

obj.setheading(90)
obj.forward(150)
obj.setheading(180)
obj.forward(20)
obj.setheading(270)
obj.forward(400)
obj.setheading(180)
obj.forward(50)
obj.setheading(270)
obj.forward(30)
obj.setheading(360)
obj.forward(120)
obj.setheading(90)
obj.forward(30)
obj.setheading(180)
obj.forward(50)
obj.setheading(90)
obj.forward(400)
obj.end_fill()





obj.hideturtle()

turtle.done()

# Second Try
# import turtle as t
# t.speed(1)
# def ractangle(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     for i in range(2):
#         t.forward(300)
#         t.right(90)
#         t.forward(200)
#         t.right(90)
#     t.end_fill()
# def circle(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     t.circle(-70)
#     t.end_fill()
#
# t.up()
# t.goto(0, -200)
# t.down()
# t.goto(0, 200)
# ractangle('green')
#
# t.goto(0,170)
# t.color('green')
# t.forward(150)
# circle('red')



import turtle
from MyProject import *#import from different files 

cianna=turtle.Turtle()#turtles
tye=turtle.Turtle()
tenay=turtle.Turtle()
christopher=turtle.Turtle()
tracey=turtle.Turtle()
wn = turtle.Screen()#screen color
turtle.colormode(255)
wn.bgcolor("black")
tracey.speed(0)
cianna.speed(0)
for times in range(50):
    tracey.right(345348236489369246)
    tracey.forward(times*5+5)
    cianna.penup()
    cianna.goto(-400,400)#transport to different parts of the screen
    cianna.pendown()
    tracey.color("cyan")
    cianna.color("cyan")
    cianna.forward(times*5+5)
    cianna.left(46)#angle
    tye.speed(0)
    tye.penup()
    tye.goto(400,400)
    tye.pendown()
    tye.color("cyan")
    tye.right(56)
    tye.forward(times*5+5)
    tenay.speed(0)
    tenay.color("cyan")
    tenay.penup()
    tenay.goto(-400,-400)
    tenay.pendown()
    tenay.forward(times*5+5)
    tenay.left(343)
    christopher.speed(0)
    christopher.color("cyan")
    christopher.penup()
    christopher.goto(400,-400)
    christopher.pendown()
    christopher.forward(times*5+5)
    christopher.right(38)
   

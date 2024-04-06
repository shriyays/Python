from turtle import Turtle, Screen

screen = Screen()
screen.setup(750,450)
screen.bgcolor("lavender")
screen.title("Sketch Book")

t= Turtle()

#t.circle(90)
#t.forward(50)z
t.speed(0)
t.turtlesize(0.1)
#t.pensize(10)
t.penup()
t.goto(-345,-185)
t.color("blue")
t.ondrag(t.goto)
t.pendown()

#t.heading()
t.shape("circle")

p=Turtle()
p.speed(0)
p.turtlesize(3)
p.pensize(10)
p.shape("circle")
p.penup()
p.goto(-300,-185)
p.color("pink")
p.ondrag(p.goto)
p.pendown()

#t.heading()
#p.shape("arrow")






t.exitonclick()
print(t.position())
'''
import turtle

wn = turtle.Screen()
wn.setup(width=700,height=400)
wn.title("Python Turtle Movement")

def playerUp():
  player.sety(player.ycor()+10)
def playerDown():
  player.sety(player.ycor()-10)
def playerRight():
  player.setx(player.xcor()+10)
def playerLeft():
  player.setx(player.xcor()-10)

player = turtle.Turtle()
player.speed(0) #this will make your player created instantly
player.shape("square") #set player shape
player.color("red") #set player color
player.penup() #prevent drawing lines
player.goto(0,0) #set player location

wn.onkeypress(playerUp, "w") #function, key
wn.onkeypress(playerDown, "s")
wn.onkeypress(playerRight, "d")
wn.onkeypress(playerLeft, "a")

#update the window
while True:
  wn.update()
  '''

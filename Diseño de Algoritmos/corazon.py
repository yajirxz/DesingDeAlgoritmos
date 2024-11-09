import turtle
import time

screen  = turtle.Screen()
screen.setup(800,800)
screen.bgcolor("pink")

t = turtle.Turtle()
t.hideturtle()
t.speed(3)

def pintarCorazon(x,y,size,color,thickness):
	t.penup()
	t.goto(x,y)
	t.color(color)
	t.pensize(thickness)
	t.pendown()
	t.begin_fill()
	t.left(140)
	t.forward(size)

	for _ in range(200):
		t.right(1)
		t.forward(size * 0.009)

	t.left(120)

	for _ in range(200):
		t.right(1)
		t.forward(size * 0.009)

	t.forward(size)
	t.end_fill()
	t.setheading(0)

corazones = [
	(0,-150,300,"#FF9999",5),
	(0,-135,270,"#FFCCCC",5),
	(0,-120,240,"#FFE6E6",5),
	(0,-105,210,"#FFCCCC",5),
	(0,-90,180,"#FF99CC",5),
	(0,-75,150,"#FFCCFF",5),
	(0,-50,100,"#FF6666",5)
]

for corazon in corazones:
	pintarCorazon(*corazon)
	time.sleep(2.5)
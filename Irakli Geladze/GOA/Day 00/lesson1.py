from turtle import *

#we want to draw a house

#step 1: draw a square

width(7)
color("green")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
end_fill()
#end of square

left(90)
forward(70)

color("purple")

begin_fill()
left(90)
forward(120)

right(90)
forward(60)

right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)

end_fill()


penup()
goto(70,130)
pendown()

begin_fill()
color("blue")
right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(130, 130)
pendown()

begin_fill()
right(180)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
exitonclick()
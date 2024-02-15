from turtle import *
#we want to paint a house
shape("turtle")
#step 1;  draw a square
speed(10)
width(7)
begin_fill()
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#draw a door

forward(75)
left(90)
begin_fill()
color("orange")

forward(100)
right(90)

forward(50)
right(90)

forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 120)
pendown()

begin_fill()
color("blue")
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180, 120)
pendown()

begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
exitonclick()
from turtle import Turtle,Screen
# Basic setup 
screen=Screen()
screen.title("Snake")
screen.setup(width=600,height=600)
starting_pos=[(0,0),(-20,0),(-40,0)]
for pos in starting_pos:
    new_seg=Turtle("square")
    new_seg.color("white")
    new_seg.goto(pos)
screen.bgcolor("black")

#To exit the screen 
screen.exitonclick()



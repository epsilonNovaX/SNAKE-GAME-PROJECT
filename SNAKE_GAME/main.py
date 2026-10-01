from turtle import Turtle,Screen
import time
# Basic setup 
screen=Screen()
screen.title("Snake")
screen.setup(width=600,height=600)
starting_pos=[(0,0),(-20,0),(-40,0)]
segments=[]
screen.bgcolor("black")
#Creation of the initial snake body
for pos in starting_pos:
    new_seg=Turtle("square")
    new_seg.color("white")
    new_seg.goto(pos)
    segments.append(new_seg)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_number in range(2,0,-1):
        X=segments[seg_number-1].xcor()
        Y=segments[seg_number-1].ycor()
        segments[seg_number].goto(X,Y) # last segment with next last
    segments[0].forward(20)
    segments[0].left(90)

#To exit the screen 
screen.exitonclick()



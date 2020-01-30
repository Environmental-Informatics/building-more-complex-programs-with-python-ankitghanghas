"""
Created on Thursday Jan 30 2020
by Ankit Ghanghas

Exercise 4.2 Think Python

This code uses the swampy drawing package and creates 3 flowers with 7, 10 and 20 petals

"""

import turtle
import math
bob=turtle.Turtle() # creates a turtle object bob using the package turtle
print(bob)

def polyline(t,n,length,angle):
    """
    This function creates polylines
    
    n: specifies the number of sides
    t: input object in this case the turtle(bob)
    length : length size of each side
    angle :  angle between sides
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polygon(t,n,length):
    """
    This function creates n sided regular polygons from polylines
    
    n: specifies the number of sides of polygon
    t: input object in this case the turtle(bob)
    length : length size of each side
    """
    angle=360.0/n
    polyline(t,n,length,angle)

def circle(t,r):
    """
    This function draws a circle of radius r using arc funciton
    r: radius of circle
    t: input object in this case the turtle (bob)
    """
    arc(t,r,360)
    
def arc(t,r,angle):
    """
    This funciton draws an arc of specified angle and radius
    r: radius used to draw the arc
    angle: angle of the arc(angle made by arc at the center)
    t: input object in this case the turtle
    """
    arc_len=2*math.pi*r*angle/360
    n=int(arc_len/3)+1
    step_length=arc_len/n
    step_angle=float(angle)/n
    t.lt(step_angle/2)
    polyline(t,n,step_length,step_angle)
    t.rt(step_angle/2)

def pettle(t,r,angle):
    """
    This funciton draws a pettle using arc function
    r: radius of the arc of the pettle
    angle: angle of the arc
    t: input object (turtle here)
    """
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)

def flower(t,r,n,angle):
    """
    this funciotn draws a flower of specified number of pettals
    t: input object (turtle here)
    r: radius of the arc of pettal
    angle : angle of the arc of pettal
    n: number of pettals in the flower
    """
    theta=(360.0/n)
    for i in range(n):
        pettle(t,r,angle)
        t.lt(theta)
def move_turtle(t,distance):
    """
    This funciton moves the turtle by a specified distance without leaving a trace
    on the canvas
    distance: distance we want to move the circle
    """
    t.pu()
    t.fd(distance)
    t.pd()

flower(bob,60,7,48)
move_turtle(bob,125)
flower(bob,30,10,96)
move_turtle(bob,125)
flower(bob,96,20,30)
bob.hideturtle() # hides the turtle at end
turtle.mainloop()
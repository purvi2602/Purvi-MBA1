# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:22:02 2023

@author: LENOVO
"""

import turtle
print("1.Triangle ")
print("2.Rectangle")
print("3.circle")
shape=input("Enter any of the above shape: ")
if (shape=='Rectangle') or (shape=='rectangle') or (shape=='1'):
    l=float(input("Enter the length of rectangle:"))
    b=float(input("Enter the breath of rectangle:"))
    t=turtle.Turtle()
    for i in range(2):
        t.fd(l)
        t.left(90)
        t.fd(b)
        t.left(90)
        
elif (shape=='Triangle') or (shape=='triangle') or (shape=='2'):
    side=float(input("Enter the side of triangle:"))
    t=turtle.Turtle()
    for i in range(3):
        t.left(120)
        t.fd(side)
        
elif (shape=='Circle') or (shape=='circle') or (shape=='3'): 
    radius= float(input("Enter the radius of circle"))
    t=turtle.Turtle()
    for i in range (1):
        t.circle(radius)
        
        
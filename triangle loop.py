# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:57:34 2023

@author: LENOVO
"""

import turtle
a=200
y=120
t=turtle.Turtle()
for i in range(3):
    t.fd(a)
    t.left(y)
    t.fd(a)
    t.left(y)
    t.fd(a-20)
    t.left(y)
    t.fd(20)
    a=a-60
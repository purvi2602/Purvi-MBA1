import turtle
a=200
y=90
t=turtle.Turtle()
for i in range(5):
    t.fd(a)
    t.left(y)
    t.fd(a)
    t.left(y)
    t.fd(a)
    t.left(y)
    t.fd(a-20)
    t.left(y)
    t.fd(20)
    a=a-40
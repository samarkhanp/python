import turtle
c=['red','blue','green']
i=0
turtle.pensize(5)

for angle in range(0,360,30):
    if i>2:
        i=0
    turtle.color(c[i])
    turtle.seth(angle)
    turtle.circle(50)
    i=i+1

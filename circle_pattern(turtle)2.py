import turtle
c=['red','blue','green']
i=0
turtle.pensize(2)

for angle in range(36):
    if i>2:
        i=0
    turtle.color(c[i])
    for j in range(4):
        turtle.forward(70)
        turtle.left(90)
    turtle.left(10)
    i=i+1



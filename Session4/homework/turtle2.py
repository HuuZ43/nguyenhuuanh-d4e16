from turtle import *
shape("turtle")
color("blue")
speed(-1)
for i in range(20, 70):
    left(10)
    for j in range(4):
        forward(i)
        left(90)
mainloop()
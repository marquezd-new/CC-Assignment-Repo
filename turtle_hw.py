from turtle import *
import random
shape('turtle')
speed(0)
pencolor(random(255),random(255),random(255))

def euler_curve (step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        right(angle)
        forward(step_size)
        angle += angle_step

euler_curve(step_size = 4, angle_step = random.random(), n_steps = 10000)

tracer(True)
exitonclick()
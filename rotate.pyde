import time

t = 0

xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

xscl = 0
yscl = 0

def setup():
    size(1000, 1000)
    rectMode(CENTER)

def draw():
    translate(width/2, height/2)
    global t
    draw_grid()
    stroke(0)
    rotate(radians(t))
    for i in range(12):
        pushMatrix()
        ellipse(225, 25, 10, 10)
        translate(225, 25)
        rotate(radians(t))
        rect(0, 0, 50, 50)
        # rect(-25, -25, 50, 50)
        # ellipse(0, 0, 50, 50)
        popMatrix()
        rotate(radians(360/12))
    t += 1
    
def draw_grid():
    background(255)
    xscl = width / rangex
    yscl = -height / rangey
    stroke(255, 0, 0)
    strokeWeight(1)
    for i in range(xmin, xmax+1):
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
    for i in range(ymin, ymax+1):
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)
    stroke(0)
    strokeWeight(2)
    line(xmin * xscl, 0, xmax * xscl, 0)
    line(0, ymin * yscl, 0, ymax * yscl)

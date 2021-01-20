# the magnitude or absolute value of a complex number is how far the complex number 
# is away from the origin on the complex coordinate plane.

# in math terms, getting close to a number is called converging; converge means two lines move towards the same point where they will meet.
# getting too big is called diverging


# width = 600
# height = 600

# global x_scl, y_scl, xmin, xmax, ymin, ymax
# -0.25, 0.25, -1, -0.5
xmin = -2
xmax = 2
ymin = -2
ymax = 2
x_range = xmax - xmin
y_range = ymax - ymin


def setup():
    global x_scl, y_scl
    size(1000, 1000)
    noStroke()
    x_scl = float(x_range)/width
    y_scl = float(y_range)/height
    colorMode(HSB)
    
def draw():
    # background(255)
    # translate(width/2, height/2)
    # draw_grid()
    # # calculte MS
    # z = [0.1, 0.1]
    # println(mandelbrot(z, 100))
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * x_scl), (ymin + y * y_scl)]
            col = mandelbrot(z, 100)
            if col == 100:
                fill(0)
            else:
                fill(255-3*col, 255, 255)
            rect(x, y, 1, 1)
    fill(255)
    textSize(32)
    text("f(x) = f^2(x-1) + ({}+{}i)".format(zz[0], zz[1]), 10, 50)
    pass

def draw_grid():
    # global x_scl, y_scl, xmin, xmax, ymin, ymax
    # xmin = -5
    # xmax = 5
    # ymin = -5
    # ymax = 5
    # x_range = xmax - xmin
    # y_range = ymax - ymin
    # x_scl = width/x_range
    # y_scl = -height/y_range
    stroke(0, 255, 0)
    for i in range(xmin, xmax):
        line(i*x_scl, ymin*y_scl, i*x_scl, ymax*y_scl)
    for i in range(ymin, ymax):
        line(xmin*x_scl, i*y_scl, xmax*x_scl, i*y_scl)
    stroke(0)
    line(xmin*x_scl, 0, xmax*x_scl, 0)
    fill(0)
    triangle(0, ymax*y_scl, -0.2*x_scl, (ymax-0.2)*y_scl, 0.2*x_scl, (ymax-0.2)*y_scl)
    line(0, ymin*y_scl, 0, ymax*y_scl)
    triangle(xmax*x_scl, 0, (xmax-0.2)*x_scl, 0.2*y_scl, (xmax-0.2)*x_scl, -0.2*y_scl)
    # draw title
    fill(255, 0, 0)
    textSize(32)
    text("MANDELBROT SET", -1.5*x_scl, 4.5*y_scl)
            
from math import sqrt

# a and b are lists including the real part and imaginary part of a complex number
def cAdd(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def cMult(a, b):
    return [a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

def mandelbrot(z, num):
    # noFill()
    # stroke(255., 0, 0)
    # ellipse(0, 0, 4*x_scl, 4*y_scl)
    count = 0
    z1 = z
    global zz 
    zz = [.285, 0.01]
    
    # stroke(0)
    # fill(0)
    while count <= num:
        # line(0, 0, z1[0]*x_scl, z1[1]*y_scl)
        # text("%d"%count, z1[0]*x_scl, z1[1]*y_scl)
        # ellipse(z1[0]*x_scl, z1[1]*y_scl, 7, 7)
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMult(z1, z1), zz)
        count += 1
    return num

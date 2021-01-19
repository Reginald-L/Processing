xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax -xmin
rangey = ymax - ymin

# run once when the programe be executed
def setup():
    global xscl, yscl
    size(1000, 1000)
    xscl = width / rangex
    yscl = -height / rangey
    

def draw():
    global xscl, yscl
    background(255)
    translate(width/2, height/2)
    draw_grid()
    graphFunction()

def graphFunction():
    fill(0)
    stroke(255, 0, 0)
    x = xmin
    while x <= xmax:
        y = f(x)
        # print(y)
        # ellipse(x * xscl, y * yscl, 10, 10)
        line(x * xscl, y * yscl, (x+.1) * xscl, f(x+.1) * yscl)
        x += .1
        

def f(x):
    # return x**2
    # return 6*x**3 + 31*x**2 + 3*x - 10
    # return 2 * x**2 + 7 * x - 15
    return x**2

def draw_grid():
    # set the width of the lines
    strokeWeight(1)
    # set the color of the lines
    stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax + 1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) # black
    line(xmin*xscl, 0, xmax*xscl, 0)
    line(0, ymax*yscl, 0, ymin*yscl)
        
        
        

width = 1000
height = 1000

r1 = 100
r2 = 5

t = 0

circleList = []

def setup():
    size(width, height)

def draw():
    global t, circleList
    translate(width/4, height/2)
    # must set the background
    background(225)
    # big circle
    noFill()
    stroke(0)
    ellipse(0, 0, 2*r1, 2*r1)
    
    stroke(255,0,0)
    line(200,500, 200, -500)
    line(0, 0, 750, 0)
    
    # calculate x and y
    x = r1*cos(t)
    y = r1*sin(t)
    # circleList.insert(0, y)    
    # get first 300
    circleList = [y] + circleList[:199]
    fill(255, 0, 0)
    ellipse(x, y, 2*r2, 2*r2)
    
    # draw a green line
    stroke(0, 255, 0)
    line(x, y, 200, y)
    
    fill(0, 255, 0)
    for i, c in enumerate(circleList):
        ellipse(200+i, c, 2*r2, 2*r2)
    
    
    t += 0.05

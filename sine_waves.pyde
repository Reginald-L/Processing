r1 = 100
r2 = 5
t = 0

circleList = []

def setup():
    size(1000, 1000)

def draw():
    global t, circleList
    translate(width/4, height/2)
    background(200)
    stroke(0)
    noFill()
    ellipse(0, 0, 2*r1, 2*r1)
    
    fill(255, 0, 0)
    y = r1*sin(t)
    x = r1*cos(t)
    # circleList = [y] + circleList[:249]
    ellipse(x, y, 2*r2, 2*r2)
    
    # stroke(0, 255, 0)
    # line(x, y, 200, y)
    # fill(0, 255, 0)
    # ellipse(200, y, 2*r2, 2*r2)
    
    # for i, c in enumerate(circleList):
    #     ellipse(200+i, c, r2, r2)
    t += .05

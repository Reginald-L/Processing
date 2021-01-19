t = 0

def setup():
    size(1000, 1000)

def draw():
    global t
    translate(width/2,height/2)
    stroke(255, 0, 0)
    rotate(radians(t))
    # draw_shape()
    # draw_six_sides_shape(50)
    polygon(5, 100)
    t += .5

def draw_shape():
    beginShape()
    vertex(0, 100)
    vertex(100, 0)
    vertex(0, -100)
    vertex(-100, 0)
    endShape(CLOSE)
    
def draw_six_sides_shape(r=100):
    beginShape()
    for i in range(6):
        vertex(r*cos(radians(60*i)), r*sin(radians(60*i)))
    endShape(CLOSE)
    
def polygon(sides, sz):
    if sides == 0 or sides == 1 or sides ==2:
        sides = 3
    beginShape()
    radian = 360/sides
    for i in range(sides):
        vertex(sz*cos(radians(radian*i)), sz*sin(radians(radian*i)))
    endShape(CLOSE)

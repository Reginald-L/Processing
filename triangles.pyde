def setup():
    size(1200, 1200)
    rectMode(CENTER)
    colorMode(HSB)

t = 0

def draw():
    global t
    background(255)
    translate(width/2, height/2)
    rotate(radians(t))
    # triangle(0,0, 100, 100, 200, -200)
    spin(t)
        
        
    t += .5
    
def spin(t):
    for i in range(90):
        rotate(radians(360 / 90))
        stroke(i*3, 255, 255)
        pushMatrix()
        translate(200, 0)
        rotate(radians(t+3*i*360/90))
        draw_equilateral_triangle(100)
        popMatrix()

def draw_equilateral_triangle(length = 100):
    noFill()
    triangle(0, -length, -length*sqrt(3)/2, length/2, length*sqrt(3)/2, length/2)

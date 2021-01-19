scl = 30

def setup():
    size(1200, 1200)
    rectMode(CENTER)
    colorMode(HSB)

def draw():
    background(0)
    translate(20, 20)
    for x in range(width/scl):
        for y in range(height/scl):
            d = dist(x * scl, y * scl, mouseX, mouseY)
            fill(.5 * d, 255, 255)
            rect(x * scl, y * scl, 25, 25)
            
            

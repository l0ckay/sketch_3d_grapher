from Vector import *

x_id = Vector3(1,0,0)
y_id = Vector3(0,1,0)
z_id = Vector3(0,0,1)

x_proj = Vector2(100,0)
y_proj = Vector2(70,70)
z_proj = Vector2(0,50)

def f(x, y):
    return x**2-y**2

def setup():
    size(600,600)
    frameRate(30)

    
p1 = Vector3(1,3,f(1,3))
p2 = Vector3(-2, 2, f(-2, 2))

field = []

minX = -2
maxX = 2
x_int = 0.4

minY = -2
maxY = 2
y_int = 0.1

for y in range(int(minY/y_int), int(maxY/y_int)):
    y *= y_int
    row = []
    for x in range(int(minX/x_int), int(maxX/x_int)):
        x *= x_int
        row.append(Vector3(x,y,f(x,y)))
    field.append(row)

def draw():
    
    # Translate matrix
    scale(1,-1)
    translate(width/2, -height/2)
    background(80)

    # Draw axis
    strokeWeight(2)
    stroke(255, 0, 0)
    line(0, 0, x_proj.x, x_proj.y)
    stroke(0,255,0)
    line(0, 0, y_proj.x, y_proj.y)
    stroke(0,0,255)
    line(0, 0, z_proj.x, z_proj.y)
    

    fill(0)
    stroke(255)
    strokeWeight(1)
    stroke(255)
    
    for y,vr in enumerate(field):
        for x,v in enumerate(vr):
            for ne in [[-1,0],[0,1],[1,0],[0,-1]]:
                if (x+ne[1] >= 0) and (y+ne[0]) >= 0:
                    try:
                        if ne[0] == 0:
                            stroke(255,200,200)
                        else:
                            stroke(200,255,200)
                        p2 = field[y+ne[0]][x+ne[1]]
                        v.drawLine(p2,x_proj, y_proj, z_proj)
                    except:
                        pass

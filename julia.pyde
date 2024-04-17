from math import sqrt

#range of x-values
xmin = -0.25
xmax = 0.25

#range of y-values
ymin = -1
ymax = -0.5

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(800,800)
    colorMode(HSB)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    translate(width/2,height/2)
    
def draw():
    #origin in center
    
    #go over all x's and y's on the grid
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * xscl),
                 (ymin + y * yscl) ]
            # put it into the mandelbrot function
            col=mandelbrot(z,100)
            #if mandelbrot returns 0
            if col == 100:
                fill(0)
            else:
                fill(3*col,255,255)
            rect(x,y,1,1)
            
    


def mandelbrot(z,num):
    count = 0
    #define z1 as z
    z1 = z
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(z1) > 2.0:
            #return the step it was diverged on
            return count
        #iterate z
        z1 =cAdd(cMult(z1,z1),z)
        count+=1
    #if z hasn't diverged by the end
    return num




def cAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

    
    

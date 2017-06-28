from display import *
from matrix import *
from math import *

def add_box( points, x, y, z, width, height, depth ):
    x2 = x + width
    y2 = y - height
    z2 = z - depth

    # top edges
    add_edge(points, x, y, z, x + 2, y, z)
    add_edge(points, x2, y, z, x2 + 2, y, z)
    add_edge(points, x2, y, z2, x2 + 2, y, z2)
    add_edge(points, x, y, z2, x + 2, y, z2)

    # lateral edges
    # add_edge(points, x, y, z, x, y2, z)
    # add_edge(points, x2, y, z, x2, y2, z)
    # add_edge(points, x2, y, z2, x2, y2, z2)
    # add_edge(points, x, y, z2, x, y2, z2)

    # bottom edges
    add_edge(points, x, y2, z, x + 2, y2, z)
    add_edge(points, x2, y2, z, x2 + 2, y2, z)
    add_edge(points, x2, y2, z2, x2 + 2, y2, z2)
    add_edge(points, x, y2, z2, x + 2, y2, z2)
'''
step = 0.1
n = 1/step
for i =0; i <= n; i += 1
     t = i/n
     x = rcos(2 * pi * t)
'''
def add_sphere( points, cx, cy, cz, r, step ):
    sphere_matrix = generate_sphere(points, cx, cy, cz, r, step)

    for point in sphere_matrix:
        add_edge(points, point[0], point[1], point[2],
                         point[0] + 1, point[1] + 1, point[2] + 1)
    
def generate_sphere( points, cx, cy, cz, r, step ):
    sphere_matrix = []

    n = 1.0 / step
    for i in range(int(n)):
        t1 = i / n
        for j in range(int(n)):
            t2 = j / n
            # calculate x, y, z
            x = r * math.cos(t2 * math.pi) + cx
            y = r * math.sin(t2 * math.pi) * math.cos(t1 * 2 * math.pi) + cy
            z = r * math.sin(t2 * math.pi) * math.sin(t1 * 2 * math.pi) + cz            
            # add_points
            sphere_matrix.append([x, y, z])

    return sphere_matrix
        
def add_torus( points, cx, cy, cz, r0, r1, step ):
    torus_matrix = generate_torus(points, cx, cy, cz, r0, r1, step)

    for point in torus_matrix:
        add_edge(points, point[0], point[1], point[2],
                         point[0] + 1, point[1] + 1, point[2] + 1)
    
def generate_torus( points, cx, cy, cz, r0, r1, step ):
    torus_matrix = []

    n = 1.0 / step
    for i in range(int(n)):
        t1 = i / n
        for j in range(int(n)):
            t2 = j / n
            # calculate x, y, z
            x = math.cos(t2 * 2 * math.pi) * (r0 * math.cos(t1 * 2 * math.pi) + r1) + cx
            y = r0 * math.sin(t1 * 2 * math.pi) + cy
            z = -math.sin(t2 * 2 * math.pi) * (r0 * math.cos(t1 * 2 * math.pi) + r1) + cz            
            # add_points
            torus_matrix.append([x, y, z])

    return torus_matrix
    
def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    t = step

    while t <= 1.00001:
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    t = step
    while t <= 1.00001:
        x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line

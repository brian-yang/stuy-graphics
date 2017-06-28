from display import *

# Breshau's Line Algorithm
# ========================
# f(x,y) = Ax + By + C
# A = dy
# B = -dx
# C = (dx)b where b is the y-intercept
# ========================
def draw_line( screen, x0, y0, x1, y1, color ):
    if x0 > x1:
        tmp = x0
        x0 = x1
        x1 = tmp

        tmp = y0
        y0 = y1
        y1 = tmp
        
    A = y1 - y0
    B = -(x1 - x0)

    x = x0
    y = y0

    # Quadrant IV
    if y0 >= y1 and x0 <= x1:
        # Octant 7
        if abs(A) > abs(B):
            distance = A - 2 * B
            while y >= y1:
                plot(screen, color, x, y)
                if distance > 0:
                    x += 1
                    distance += 2 * A
                y -= 1
                distance -= 2 * B
        # Octant 8
        else:
            distance = 2 * A - B
            while x <= x1:
                plot(screen, color, x, y)
                if distance < 0:
                    y -= 1
                    distance -= 2 * B
                x += 1
                distance += 2 * A
    # Quadrant I
    else:
        # Octant 2
        if abs(A) > abs(B):
            distance = A + 2 * B

            while y <= y1:
                plot(screen, color, x, y)
                if distance < 0:
                    x += 1
                    distance += 2 * A
                y += 1
                distance += 2 * B
        # Octant 1
        else:
            distance = 2 * A + B

            while x <= x1:
                plot(screen, color, x, y)
                if distance > 0:
                    y += 1
                    distance += 2 * B
                x += 1
                distance += 2 * A

    return screen

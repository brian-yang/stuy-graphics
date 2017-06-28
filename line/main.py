from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

XRES = 500
YRES = 500

# draw_line(screen, 50, 100, 250, 200, [255, 0, 0]) # octant 1
# draw_line(screen, 50, 100, 70, 160, [0, 255, 0]) # octant 2
# draw_line(screen, 50, 100, 250, 70, [255, 255, 0]) # octant 7
# draw_line(screen, 50, 100, 60, 75, [255, 165, 0]) # octant 8

# draw_line(screen, 50, 100, 20, 160, [0, 255, 255]) # octant 3
# draw_line(screen, 50, 100, 20, 120, [0, 0, 255]) # octant 4
# draw_line(screen, 50, 100, 20, 80, [238, 130, 238]) # octant 5
# draw_line(screen, 50, 100, 20, 50, [238, 130, 238]) # octant 6

# draw_line(screen, 50, 100, 30, 100, [0, 255, 255]) # left
# draw_line(screen, 50, 100, 120, 100, [0, 0, 255]) # right
# draw_line(screen, 50, 100, 50, 150, [238, 130, 238]) # top
# draw_line(screen, 50, 100, 50, 50, [238, 130, 238]) # bottom

# for i in range(0, 500):
#     for j in range(0, 500):
#         draw_line(screen, 250, 250, i, j, [255, 0, 0])

# draw_line(screen, 250, 250, 499, 0, [255, 255, 255])

# octants 1 and 5
draw_line(s, 0, 0, XRES-1, YRES-1, c);
draw_line(s, 0, 0, XRES-1, YRES / 2, c);
draw_line(s, XRES-1, YRES-1, 0, YRES / 2, c);

# octants 8 and 4
c[2] = 255;
draw_line(s, 0, YRES-1, XRES-1, 0, c);
draw_line(s, 0, YRES-1, XRES-1, YRES/2, c);
draw_line(s, XRES-1, 0, 0, YRES/2, c);

# octants 2 and 6
c[0] = 255;
c[1] = 0;
c[2] = 0;
draw_line(s, 0, 0, XRES/2, YRES-1, c);
draw_line(s, XRES-1, YRES-1, XRES/2, 0, c);

# octants 7 and 3
c[2] = 255;
draw_line(s, 0, YRES-1, XRES/2, 0, c);
draw_line(s,XRES-1, 0, XRES/2, YRES-1, c);

# horizontal and vertical
c[2] = 0;
c[1] = 255;
draw_line(s, 0, YRES/2, XRES-1, YRES/2, c);
draw_line(s, XRES/2, 0, XRES/2, YRES-1, c);

display(s)
save_extension(s, 'img.png')

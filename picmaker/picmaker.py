# Header
header = "P3\n"

# Resolution
xres = 500
yres = 500
resolution = "%d %d\n" % (xres, yres)

# Max Color
max_color = "255\n"

# Body
body = ""

r = 255
g = 255
b = 255

for i in range(500):
    for j in range(500):
        body += " %d %d %d\n" % ((r + i + j) % 255 , (g + i + j) % 255, (b + i + j) % 255)

# Create image
f = open("color.ppm", 'w')
f.write(header + resolution + max_color + body)
f.close()

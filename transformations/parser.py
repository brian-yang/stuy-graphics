from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, edges, transform, screen, color ):
    print "If you are displaying the edge matrix more than once, only one window will appear at a time."
    print "Press ESC to close the current window to go to the next window."
    
    transformations = ["scale", "move", "rotate"]
    stack = []
    argument_list = []

    f = open(fname, 'r')

    command = f.readline().strip()
    while (command != "quit" and command != ""):
        # line
        if command == "line":
            arguments = f.readline().strip()
            coordinates = [float(value) for value in arguments.split()]
            add_edge(edges,
                     coordinates[0], coordinates[1], coordinates[2],
                     coordinates[3], coordinates[4], coordinates[5])
        # transformations
        elif command in transformations:
            stack.append(command)
            arguments = f.readline().strip()
            argument_list.append(arguments)
        # identity matrix
        elif command == "ident":
            ident(transform)
        # apply
        elif command == "apply":
            transform = parse_transformations(transform, stack, argument_list)
            matrix_mult(transform, edges)
            stack = []
            argument_list = []
        # display
        elif command == "display":
            clear_screen(screen)
            draw_lines(edges, screen, color)
            display(screen)
            clear_screen(screen)
        # save
        elif command == "save":
            clear_screen(screen)
            draw_lines(edges, screen, color)
            savefile = f.readline().strip()
            save_extension(screen, savefile)
            clear_screen(screen)
        command = f.readline().strip()

def parse_transformations(matrix, stack, parameters):
    for index in range(len(stack)):
        # scale
        if stack[index] == "scale":
            s = [float(parameter) for parameter in parameters[index].split()]
            m = make_scale(s[0], s[1], s[2])
        # translate
        elif stack[index] == "move":
            t = [float(parameter) for parameter in parameters[index].split()]
            m = make_translate(t[0], t[1], t[2])
        # rotate
        elif stack[index] == "rotate":
            polar_coords = parameters[index].split()

            axis = polar_coords[0]
            theta = float(polar_coords[1])
            if axis == "x":
                m = make_rotX(theta)
            elif axis == "y":
                m = make_rotY(theta)
            elif axis == "z":
                m = make_rotZ(theta)

        matrix_mult(m, matrix)
    return matrix

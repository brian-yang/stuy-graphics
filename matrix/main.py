from display import *
from draw import *

def main():
    screen = new_screen()
    color = [ 0, 255, 0 ]
    matrix = new_matrix()

    print "============="
    print "|MATRIX DEMO|"
    print "============="

    print
    print "Original Matrix:"
    print "======================="
    print_matrix(matrix)

    print
    print "Identity Matrix:"
    print "======================="
    ident(matrix)
    print_matrix(matrix)

    print
    print "Identity matrix multiplied by a scalar: "
    print "======================="
    scalar_mult(matrix, 32)
    print_matrix(matrix)

    print
    print "Original Matrix 2:"
    print "======================="
    matrix = [[10, 20, 30], [1, 2, 3], [100, 200, 300]]
    print_matrix(matrix)

    print
    print "Identity Matrix 2:"
    print "======================="
    ident(matrix)
    print_matrix(matrix)

    print
    print "Identity matrix multiplied by a scalar: "
    print "======================="
    scalar_mult(matrix, 32)
    print_matrix(matrix)
    
    print
    print "Matrix multiplication (A x B): "
    print "======================="
    row1 = 3
    col1 = 5
    a = [[round(random.random() * 5) for i in range(col1)] for j in range(row1)]
    print "Matrix A:"
    print
    print_matrix(a)
    print

    row2 = 5
    col2 = 1
    b = [[round(random.random() * 5) for i in range(col2)] for j in range(row2)]
    print "Matrix B:"
    print
    print_matrix(b)
    print

    matrix_mult(a, b)
    print "Resulting matrix:"
    print
    print_matrix(b)
    print

    print
    print "Resulting matrix multiplied by a scalar: "
    print "======================="
    scalar_mult(b, 2)
    print_matrix(b)

    #==========================================================
    print "======================"
    print "|GRAPHICS MATRIX DEMO|"
    print "======================"

    matrix = []

    # for i in range(0, 500):
    #     for j in range(0, 500):
    #         add_edge(matrix,i,j,0,250,250,0)

    add_edge(matrix, 0, 250, 0, 250, 500, 0)
    add_edge(matrix, 250, 500, 0, 500, 250, 0)
    add_edge(matrix, 0, 250, 0, 250, 0, 0)
    add_edge(matrix, 250, 0, 0, 500, 250, 0)
    add_edge(matrix, 0, 250, 0, 500, 250, 0)
    add_edge(matrix, 250, 500, 0, 250, 0, 0)

    add_edge(matrix, 0 / 2, 250 / 2, 0, 250 / 2, 500 / 2, 0)
    add_edge(matrix, 250 / 2, 500 / 2, 0, 500 / 2, 250 / 2, 0)
    add_edge(matrix, 0 / 2, 250 / 2, 0, 250 / 2, 0 / 2, 0)
    add_edge(matrix, 250 / 2, 0 / 2, 0, 500 / 2, 250 / 2, 0)
    add_edge(matrix, 0 / 2, 250 / 2, 0, 500 / 2, 250 / 2, 0)
    add_edge(matrix, 250 / 2, 500 / 2, 0, 250 / 2, 0 / 2, 0)

    # add_edge(matrix, 0, 250 / 2, 0, 250, 500, 0)
    # add_edge(matrix, 250, 500 / 2, 0, 500, 250, 0)
    # add_edge(matrix, 0, 250 / 2, 0, 250, 0, 0)
    # add_edge(matrix, 250, 0 / 2, 0, 500, 250, 0)
    # add_edge(matrix, 0, 250 / 2, 0, 500, 250, 0)
    # add_edge(matrix, 250, 500 / 2, 0, 250, 0, 0)

    # add_edge(matrix, 0, 250, 0, 250 / 2, 500, 0)
    # add_edge(matrix, 250, 500, 0, 500 / 2, 250, 0)
    # add_edge(matrix, 0, 250, 0, 250 / 2, 0, 0)
    # add_edge(matrix, 250, 0, 0, 500 / 2, 250, 0)
    # add_edge(matrix, 0, 250, 0, 500 / 2, 250, 0)
    # add_edge(matrix, 250, 500, 0, 250 / 2, 0, 0)

    # add_edge(matrix, 0, 250, 0, 250, 500 / 2, 0)
    # add_edge(matrix, 250, 500, 0, 500, 250 / 2, 0)
    # add_edge(matrix, 0, 250, 0, 250, 0 / 2, 0)
    # add_edge(matrix, 250, 0, 0, 500, 250 / 2, 0)
    # add_edge(matrix, 0, 250, 0, 500, 250 / 2, 0)
    # add_edge(matrix, 250, 500, 0, 250, 0 / 2, 0)

    print "Graphics matrix:"
    print_matrix(matrix)

    draw_lines( matrix, screen, color )
    display(screen)

main()

import math
import random

def print_matrix( matrix ):
    row = "["

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # print space
            if j == 0 and i != 0:
                row += " "
            # print matrix element
            if j == len(matrix[i]) - 1:
                row += str(matrix[i][j])
            else:
                row += str(matrix[i][j]) + '  '
        # print newline
        if i != len(matrix) - 1:
            row += ',\n'

    row += "]"

    print row

def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

def scalar_mult( matrix, s ):
    for row in matrix:
        for i in range(len(row)):
            row[i] *= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    # initialize copy of m2 and determine the num of rows and columns in resulting matrix
    num_rows = len(m1)
    num_cols = len(m2[0])
    arr = [[m2[i][j] for j in range(len(m2[0]))] for i in range(len(m2))]

    # reset m2
    for i in range(len(m2)):
        for j in range(len(m2[i])):
            m2[i][j] = 0

    # add more rows if necessary
    if num_rows > len(m2):
        for i in range(len(m2), num_rows):
            m2.append([0 for j in range(num_cols)])

    # matrix multiplication
    for cur_row in range(num_rows):
        cur_col = 0
        while cur_col < num_cols:
            for j in range(len(arr)):
                m2[cur_row][cur_col] += m1[cur_row][j] * arr[j][cur_col]
            cur_col += 1

    # backwards remove the other rows in m2
    if num_rows < len(m2):
        for i in range(len(m2) - 1, num_rows - 1, -1):
            m2.pop(i)

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

# # ==============================================
# # TESTING
# # ==============================================
# m = new_matrix()
# print_matrix(m)
# ident(m)
# scalar_mult(m, 2)
# print
# print_matrix(m)

# row1 = 3
# col1 = 5
# a = [[round(random.random() * 5) for i in range(col1)] for j in range(row1)]
# print
# print "Matrix A:"
# print_matrix(a)

# row2 = 5
# col2 = 1
# b = [[round(random.random() * 5) for i in range(col2)] for j in range(row2)]
# print
# print "Matrix B:"
# print_matrix(b)

# matrix_mult(a, b)
# print
# print "Resulting matrix:"
# print_matrix(b)

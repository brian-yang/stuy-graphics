from matrix import *

class TransformStack:
     def __init__(self):
          self.transformations = []
          i = new_matrix()
          ident(i)
          self.transformations.append(i)

     def push(self):
          curTop = self.transformations[-1]

          copy = new_matrix()
          for i in range(len(curTop)):
               for j in range(len(curTop[i])):
                    copy[i][j] = curTop[i][j]

          self.transformations.append(copy)

     def pop(self):
          return self.transformations.pop()

     def peek(self):
          return self.transformations[-1]

     def size(self):
          return len(self.transformations)

     def get_list(self):
         return self.transformations
      
# ts = TransformStack()
# ts.push()
# top = ts.peek()
# translate = make_translate(1, 2, 3)
# matrix_mult(translate, top)
# print_matrix(top)
# ts.pop()
# top = ts.peek()
# print_matrix(top)

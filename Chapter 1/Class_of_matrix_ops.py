import numpy as np

#MatrixA and MatrixB should be of the same size and the same dimension. I have assumed both as 3 by 1 or 1 by 3.
#Please ignore this file. :) I am just practicing knowledge about classes and objects.
class matrix_op(object):

    __slots__ = ('MatrixA', 'MatrixB')  
  
    def __init__(self, MatrixA, MatrixB):
        self.MatrixA = MatrixA
        self.MatrixB = MatrixB
         
    def addition(self):
        return np.add(self.MatrixA, self.MatrixB)
    
    def substraction(self):
        return np.subtract(self.MatrixA, self.MatrixB)
      
    def dotproduct(self):
        return np.dot(self.MatrixA, self.MatrixB)
    
    def crossproduct(self):
        return np.cross(self.MatrixA, self.MatrixB)
    
A = matrix_op([2,2,2],[2,2,2])
print(A.dotproduct())

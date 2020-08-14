import numpy as np

#MatrixA and MatrixB should be of the same size and the same dimension. I have assumed both as 3 by 1 or 1 by 3.
Class matrix_op(object):

    __slots__ = ('_choice', '_MatrixA', '_MatrixB')  
  
    def __init__(self, choice, MatrixA, MatrixB):
        self.choice = choice
        self.MatrixA = MatrixA
        self.MatrixB = MatrixB
        
    def addition(self, choice, MatrixA, MatrixB):
        if choice == 1:
            resultadd = np.add(MatrixA, MatrixB)
        return resultadd
    
    def substraction(self, choice, MatrixA, MatrixB):
        if choice == 2:
            resultsub = np.subtract(MatrixA, MatrixB)
        return resultsub
      
    def dotproduct(self, choice, MatrixA, MatrixB):
        if choice == 3:
            resultdot = np.dot(MatrixA, MatrixB)
        return resultdot
    
    def crossproduct(self, choice, MatrixA, MatrixB):
        if choice == 4:
            resultcross = np.cross(MatrixA, MatrixB)
        return resultcross
    
     

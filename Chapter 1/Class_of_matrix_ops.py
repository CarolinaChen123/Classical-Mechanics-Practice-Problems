import numpy as np

#MatrixA and MatrixB should be of the same size and the same dimension. I have assumed both as 3 by 1 or 1 by 3.
#Please ignore this file. :) I am just practicing knowledge about classes and objects.
class matrix_op(object):

    __slots__ = ('_choice', '_MatrixA', '_MatrixB')  
  
    def __init__(self, choice, MatrixA, MatrixB):
        self.choice = choice
        self.MatrixA = MatrixA
        self.MatrixB = MatrixB
         
    def addition(self):
        if self.choice == 1:
            resultadd = np.add(self.MatrixA, self.MatrixB)
        return resultadd
    
    def substraction(self):
        if self.choice == 2:
            resultsub = np.subtract(self.MatrixA, self.MatrixB)
        return resultsub
      
    def dotproduct(self):
        if self.choice == 3:
            resultdot = np.dot(self.MatrixA, self.MatrixB)
        return resultdot
    
    def crossproduct(self):
        if self.choice == 4:
            resultcross = np.cross(self.MatrixA, self.MatrixB)
        return resultcross
    
if __name__ == '__main__':
    main()
     

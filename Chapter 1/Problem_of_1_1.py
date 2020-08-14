#Find the transformation matrix that rotates the axis x3 of a rectangular coordinate system 45 degrees toward x1 around the x2 axis.
#In this code, I would just define a function called transformation that ONLY specifies this rotation.

#Full solutions may be given later.
#I have not tested the code.

from math import sqrt

#A is supposed to be a matrix with 3 rows and 1 column
def transformation(A):
    #Let me just define a 3 by 1 matrix here with all zero elements
    initials = [0, 0, 0]
    Transformation = [[1/sqrt(2), 0, -1/sqrt(2)], [0, 1, 0], [1/sqrt(2), 0, 1/sqrt(2)]]
    for i in range(len(Transformation)):
        for j in range(len(A)):
            initials[i] += Transformation[i][j]*A[j]
    return initials

if __name__ == '__main__':
    main()

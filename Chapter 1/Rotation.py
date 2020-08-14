#A would still be an array of 3 by 1 or 1 by 3. Sorry I did not figure out how to print out the column array in Python. :)
#There are three choices for the input choice: 1, 2, 3.
#choice 1 is the rotation around x-axis.
#choice 2 is the rotation around y-axis.
#choice 3 is the rotation around z-axis.
from math import sin, cos
#You just need to input a vector, the axis you want to rotate about, and the angle you want to rotate.
def Rotation(A, choice, angle):
    initials = [0, 0, 0]
    if choice == 1:
        Transformation = [[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]]
        for i in range(len(Transformation)):
            for j in range(len(A)):
                initials[i] += Transformation[i][j]*A[j]
    elif choice == 2:
        Transformation = [[cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]]
        for i in range(len(Transformation)):
            for j in range(len(A)):
                initials[i] += Transformation[i][j]*A[j]
    elif choice == 3:
        Transformation = [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
        for i in range(len(Transformation)):
            for j in range(len(A)):
                initials[i] += Transformation[i][j]*A[j]   
    return initials
  
  if __name__ == '__main__':
    main()

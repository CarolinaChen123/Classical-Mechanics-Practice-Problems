import numpy as np
from math import sqrt

A = [1, 2, -1]
B = [-2, 3, 1]

#I have two vectors。 A is [1, 2, -1] and B is [-2, 3, 1].
#Problem (a) requires us to find A - B and the norm of it.

print("This is the Problem(a).")
print(np.subtract(A, B))
print(np.linalg.norm(np.subtract(A,B)))
print()

#Problem (b) requires us to find the component of B along A.

print("This is the Problem(b).")
unit_A = A / np.linalg.norm(A)
print("The unit vector of A is " + str(unit_A))
print("We know that Project a onto b = (A dot B / norm(A)) * unit(A).")
Project_A_B = np.dot((np.dot(A, B)/np.linalg.norm(A)), unit_A)
print("So the answer is " + str(Project_A_B))
print()

#Problem (c) requires us to find the angle between A and B

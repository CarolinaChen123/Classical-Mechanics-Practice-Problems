import numpy as np

A = [[1, 2, -1], [0, 3, 1], [2, 0, 1]]
B = [[2, 1, 0], [0, -1, 2], [1, 1, 3]]
C = [[2, 1], [4, 3], [1, 0]]

#Problem (a) requires us to find the determinant of the product of AB.

print("Below is the answer for Problem (a)")
print(np.dot(A, B))
print(np.linalg.det(np.dot(A, B)))
print()

#Problem (b) requires us to find the product of AC.

print("Below is the answer for Problem (b)")
print(np.dot(A, C))
print()

#Problem (c) requires us to find the product of ABC.

print("Below is the answer for Problem (c)")
print(np.dot(np.dot(A, B), C))
print()

#Problem (d) requires us to find the AB-transposeBtransposeA

print("Below is the answer for Problem (d)")
print(np.dot(A, B) - np.dot(np.transpose(B), np.transpose(A)))

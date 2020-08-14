import random
import numpy as np

#This is a problem requiring students to prove something. I yet to know how to put letters instead of numbers.
#I would just put 10 random cases of three vectors A, B, C to prove this to some extent.
#I need to confirm if (A cross B) dot C = A dot (B cross C) = B dot (C cross A) = (C cross A) dot B

#Now I am just initializing the test result.
test = False

for _ in range(10):
    A=[random.randint(-1000000,1000000), random.randint(-1000000,1000000), random.randint(-1000000,1000000)]
    B=[random.randint(-1000000,1000000), random.randint(-1000000,1000000), random.randint(-1000000,1000000)]
    C=[random.randint(-1000000,1000000), random.randint(-1000000,1000000), random.randint(-1000000,1000000)]
    Results1 = np.dot(np.cross(A, B), C)
    Results2 = np.dot(A, np.cross(B, C))
    Results3 = np.dot(B, np.cross(C, A))
    Results4 = np.dot(np.cross(C, A), B)
    test = (Results1 == Results2 == Results3 == Results4)
    print(test)

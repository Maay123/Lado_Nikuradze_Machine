#6
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
print("factorial: ",factorial(5))


#7
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
print("factorial: ",fac(3))     

#9
def search_in_lists(lst1, lst2):
    check = any(item in lst1 for item in lst2)
    if check:
        return True
    else:
        return False
print(search_in_lists([1, 8, 7, 2], [1, 5, 9]))

#10

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
print(arr+arr2)


#10_2
from numpy import random
x=random.randint(100, size=(5))
x2=random.randint(100, size=(5))
print(x)
print("+")
print(x2)
print("=")
print(x+x2)
#11
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])
matrix2 = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])
print(matrix)
print("+")
print(matrix2)
print("=")
print(matrix+matrix2)

#11_2

from numpy import random
x = random.randint(10, size=(3, 5))
x2 = random.randint(10, size=(3, 5))
print(x)
print("+")
print(x2)
print("=")
print(x+x2)

#12

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
print(arr)
print("*")
print(arr2)
print("=")
print(arr*arr2)
#12_2

from numpy import random
x=random.randint(10, size=(5))
x2=random.randint(10, size=(5))
print(x)
print("*")
print(x2)
print("=")
print(x*x2)


#13

import numpy as np
matrix = np.array([[0, 0],
                   [0, 1],
                   [1, 0]])
matrix2 = np.array([[0, 0],
                   [0, 1],
                   [1, 0]])
print(matrix)
print("*")
print(matrix2)
print("=")
print(matrix*matrix2)

#13_2

from numpy import random
x = random.randint(10, size=(4, 2))
x2 = random.randint(10, size=(4, 2))
print(x)
print("*")
print(x2)
print("=")
print(x*x2)
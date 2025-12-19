#Rectabgular Method of Integration

print("Rectangular Method of finding integral of xsin(sin(x))")
# importing libraries
import math
import numpy as np

def rectangular_method(n):
    # dividing the interval into n equal parts
    a = np.linspace(0, math.pi, n+1)
    # converting array to list
    a = list(a)
    # width of each rectangle, division of total interval
    dx = (math.pi - 0) / n
    # process of finding midpoints
    B = []
    A = []
    for j in range(len(a)-1):
        m = (a[j] + a[j+1]) / 2
        B.append(m)
    # process of finding area of each rectangle
    for i in B:
        f = i * math.sin(math.sin(i))
        A.append(f)
    # sum of all the areas
    print(dx * (sum(A)))
    # taking input

n = int(input("Enter total no.of points:"))
rectangular_method(n)

#Trapizoidal Method of Integration

print("Trapezoidal Method of finding integral of 3x² + 2x")

# importing Libraries
import math
import numpy as np

def trapezoidal_method(n):
    # dividing the interval into n equal parts
    a = np.linspace(0, math.pi, n+1)
    # converting array to list
    a = list(a)
    # width of each rectangle, division of total interval
    dx = (math.pi - 0) / (2 * n)
    # segregation of the first and last element
    c = []
    c.append(a[0])
    c.append(a[-1])
    a.pop(0)
    a.pop(-1)
    # finding area of each trapezoid
    for i in a:
        c.append(2 * (3 * (i ** 2) + 2 * i))
    # sum of all the areas
    print(dx * (sum(c)))

# taking input
n = int(input("Enter total no.of points:"))
trapezoidal_method(n)

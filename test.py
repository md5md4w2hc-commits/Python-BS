import random
import math
import numpy
import sys
l = []
l1 = [0]
l2 = [0,1]
print(sys.getsizeof(l))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
x = list(range(10))
s = set(range(10))
print(sys.getsizeof(x))
print(sys.getsizeof(s))
z = {'amit', 'neeru', 'anamika', 'vasrha', 'nitin'}
print('amar' in z)
z.add("Pranjal")
print(z)
print("Pranjal" in z)
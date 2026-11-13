t = {2, 7, 18, 64, 101, 108, 65}
print(t)
l = [2, 7, 18, 64, 101, 108, 65]
print(l)
print(len(t))
print(len(l))
import sys
print(sys.getsizeof(l))
print(sys.getsizeof(t))
t1 = (2, 7, 18, 64, 101, 108, 65)
print(sys.getsizeof(t1))
print(t1[0])
s = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8]
print(set(s)) 
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
s = string.ascii_letters
s1 = set(s)
print(s1) 
alpha = tuple(s)
print(alpha)
alpha = tuple(list(s))
print(alpha)
print(list(s))
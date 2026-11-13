import sys
a = list(range(5))
t = tuple(range(5))
print(a == list(t))
print(sys.getsizeof(a) > sys.getsizeof(t))
t = (2, 7, 18, 64)
print(t[0])
print(t)
print(a[0])
print(sys.getsizeof(a))
print(sys.getsizeof(t))
alpha = tuple("abcde")
r = []
for ch in "cabbage123":
    if ch in alpha:
        r.append(ch)
print("".join(r))
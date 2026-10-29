x = int(input())
r = 1
while x > 1:
    r = x*(x - 1)*r
    x = x - 2
print(r)
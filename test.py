n = int(input())
if n > 1:
    for i in range(1, n):
        n = n * i
    print(n)
elif n == 0:
    print("1")
else:
    print("Invalid Input")

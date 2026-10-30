x = input("Enter a number")
i = 0
n = len(x)
while i < n:
    i += 1
if int(x) < 0:
    print(i - 1)
else:
    print(i)
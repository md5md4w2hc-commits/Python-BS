x = int(input("Enter a number"))
if x < 0:
    y = str(abs(x))
    print('-' + y[::-1])
else:
    y = str(x)
    print(y[::-1])


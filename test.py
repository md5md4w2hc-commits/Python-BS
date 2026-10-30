x = int(input("Enter a number"))
if x < 0:
    y = str(abs(x))
    s = '-' + y[::-1]
    if s == str(x):
        print("Palindrome")
    else:
        print("Not a Palindrome")
else:
    y = str(x)
    s = y[::-1]
    if s == str(x):
        print("Palindrome")
    else:
        print("Not a Palindrome")


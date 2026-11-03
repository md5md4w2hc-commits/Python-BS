num = int(input())
strNum = str(abs(num))
revNum = ""
for c in strNum:
    revNum = c + revNum
if num >= 0:
    print(revNum)
else:
    print('-' + revNum)
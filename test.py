email = input()
str = ''
for c in email:
    if c == '@':
        break
    str += c
print(str)
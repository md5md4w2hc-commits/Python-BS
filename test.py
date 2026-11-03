email = input()
name = ''
mail = ''
for c in email:
    if c == '@':
        print('')
        continue
    print(c, end = '')
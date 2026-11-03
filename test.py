total = 0
found = False
for i in range(1, 5):
    if found:
        break
    for j in range(1, 5):
        if j % 2 == 0:
            continue
        total += i * j
        if total > 15:
            found = True
            break
print(total)
s = input("Print the sequence: ")
t = s
count = 0
for i in range(len(s)):
    for j in range(len(s)):
        print(i, j, s[i], s[j])
        count += 1
print(count)
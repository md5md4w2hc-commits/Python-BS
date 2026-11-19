def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if(l[i] < mini):
            mini = l[i]
    return mini

def list_max(l):
    maxi = l[0]
    for i in range(len(l)):
        if(l[i] > maxi):
            maxi = l[i]
    return maxi

def list_appendbefore(l, z):
    new_list = z + l
    return new_list

def list_append(l, z):
    return (l + z)

def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    ans = sum / len(l)
    return ans

l = [1, 7, 8, 10]
z = ['a', 'v', 'c']
print(list_min(l))
print(list_max(l))
print(list_appendbefore(l, z))
print(list_append(l, z))
print(list_average(l))
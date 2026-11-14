def discount(cost, d):
    ans = cost - (cost * (d/100))
    return ans

print("Enter the cost price")
c = int(input())
print("Enter the discount")
disc = int(input())

print("The final discount is: ", discount(c, disc))
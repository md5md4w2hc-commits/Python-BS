import random
t = int(((random.random())*100)%2)+1
if(t == 1):
    print("HEADS")
else:
    print("TAILS")
print(random.choice(["HEADS", "TAILS"]))
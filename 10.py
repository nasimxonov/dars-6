import random

n = int(input("boshlang'ich sonni kiritng: "))
m = int(input("ohirgi sonni kiritng: "))

random_1 = random.sample(range(n,m+1),5)

print(random_1)

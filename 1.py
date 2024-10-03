import datetime

t = int(input("Vaqt zonasini kiriting (masalan, 0): "))

n = datetime.datetime(2008, 1, 29)

now = datetime.datetime.now()

days = (now - n).days

print(days)

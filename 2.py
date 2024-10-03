import datetime

t = input("Birinchi sanani kiriting: ")
t_2 = input("Ikkinchi sanani kiriting: ")

n = datetime.datetime.strptime(t, "%Y-%m-%d")
now = datetime.datetime.strptime(t_2, "%Y-%m-%d")

sum = abs((now - n).days)

print(f"sanalar orasidagi farq:{sum}")

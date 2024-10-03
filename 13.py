import datetime

n = datetime.datetime(2008, 1, 29)
now = datetime.datetime.now()

print(now)


from datetime import datetime

now = datetime.now()

format = now.strftime("%Y-%m-%d %H:%M:%S")
print("Hozirgi vaqt:", format)


from datetime import datetime

n = input("Birinchi sanani kiriting : ")
m = input("Ikkinchi sanani kiriting : ")

try:
    now = datetime.strptime(n, "%Y-%m-%d")
    now_2 = datetime.strptime(m, "%Y-%m-%d")

    m = abs((now_2 - now).days)

    print(f"Sana orasidagi farq: {m} kun.")
except ValueError:
    print("Error")




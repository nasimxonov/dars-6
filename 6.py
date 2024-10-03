import os

a = input("Papka yo'lini kiriting: ")

for root, dirs, files in os.walk(a):

    for i in dirs:

        print(os.path.join(root, i))

    for file_name in files:

        print(os.path.join(root, file_name))

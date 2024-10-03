import os

path = input("Papka: ")

txt = 0

for root, dirs, files in os.walk(path):

    for i in files:

        if i.endswith('.txt'):
            txt += 1

print("txt fayllar soni:", txt)

import os

yangi_papka = input("Yangi papka nomini kiriting: ")

os.mkdir(yangi_papka) 

os.chdir(yangi_papka) 

print("Nomi ozgartirildi:", os.getcwd())  

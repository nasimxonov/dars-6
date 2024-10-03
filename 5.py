import os

papka_nomi = "test"

if os.path.exists(papka_nomi) and os.path.isdir(papka_nomi):

    os.rmdir(papka_nomi)  

    print(f'"{papka_nomi}" papkasi ochirildi.')
else:
    print(f'"{papka_nomi}" papkasi mavjud emas.')

import random

lista=[]

def fej_iras():
    print("2. Feladat")
    for i in range(0, 7, 1):
        veletlen=random.randint(0,1)
        lista.append(veletlen)
        if i < 6:
            print(veletlen, end="-")
        else:
            print(veletlen, end="")
                    

def fejek_szama():
     return lista.count(1)

def konzol_kiir():
     return lista.count(1)
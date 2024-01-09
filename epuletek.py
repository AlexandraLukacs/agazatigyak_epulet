from Epulet import Epulet

epulet_lista=[]
fajlom = open("gep.txt", "r", encoding='utf-8')
fajlom.readline()
lista=fajlom.readlines()
fajlom.close()
for i in range(0, len(lista), 1):
    aktsor:str=lista[i].strip()
    print(aktsor)
    sor_lista=aktsor.split(", ")
    print(sor_lista[0])
    print(sor_lista[1])
    print(sor_lista[2])
    print(sor_lista[3])
    print(sor_lista[4])
    print(sor_lista[5])
    print(sor_lista[6])
    epulet=Epulet(int(sor_lista[0]), int(sor_lista[1]), sor_lista[2], int(sor_lista[3]))
    epulet_lista.append(epulet)

for i in range(0, len(epulet_lista), 1):
    print(f"{epulet_lista[i].nev}, {epulet_lista[i].varos}, {epulet_lista[i].orszag}, {epulet_lista[i].magassag}, {epulet_lista[i].emelet}, {epulet_lista[i].ev}")



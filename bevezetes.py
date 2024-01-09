def feladat1():
    print("1. Feladat")
    jatekos_neve=input("Játékos neve: ")
    szerepkor=input("Szerepkört: ")
    if "varázsló" in szerepkor:
        print(f"Üdvözlünk {jatekos_neve}, 2 életed van!")
    elif "harcos" in szerepkor:
        print(f"Üdvözlünk {jatekos_neve}, 10 élete van!")
    else:
         print(f"Üdvözlünk {jatekos_neve}, 8 élete van!")
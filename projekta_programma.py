print("Laipni lūdzām programmā")
print("Izvēlieties vienu no opcijas")
print("*******************************")
print("1 - Ziņot par pārkāpumu")
print("2 - Ziedot naudu")
print("3 - Mūsu kontakti")
print("4 -  Iziet no programmas")
print("*******************************")
def menu(x):
    if x<1 or x>4:
        print("Nepareiza ievade")
        quit()
    elif x == 1: 
        b=input("Ievadiet pārkāpumu:  ")
        quit()
    elif x == 2:
        c=float(input("Ievadiet ziedojuma summu:  "))
        quit()
    elif x== 3:
        print("Mūsu tālruņa numurs 1560")
        quit()
    elif x==4:
        quit()
a= int(input("Tava izvēle: "))
menu(a)
        
        
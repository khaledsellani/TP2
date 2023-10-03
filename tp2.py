# Probleme du nombre mystere
# TP universitaire python
import random 
import sys
MYSTER_NUMBER = random.randint(0,100)
attempts = 5

mystr = f"""*** Le jeu du nombre mystere ***
il te reste {attempts} essais
Devine le nombre : """



user_choise = input(mystr)
while not user_choise.isdigit():
    print("Entrez un nombre valide.")
    user_choise = input(mystr)
    print(f"il te reste {attempts} essais.")

while int(user_choise) not in [i for i in range(101)]:
    user_choise = input("Entrez un nombre dans l'intervalle [0-100].")

while attempts >= 1:
    if int(user_choise) > MYSTER_NUMBER:
        print(f"le nombre mystere est plus petit que {user_choise}")
        attempts -= 1
        if attempts == 0:
            break
        print(f"il te reste {attempts} essais.")
        user_choise = input("Devine un nombre ")
        while not user_choise.isdigit():
            print("Entrez un nombre valide.")
            user_choise = input(f"il te reste {attempts} essais. Devine un nombre : ")
        while int(user_choise) not in [i for i in range(101)]:
            user_choise = input("Entrez un nombre dans l'intervalle [0-100].")
    elif int(user_choise) < MYSTER_NUMBER:
        print(f"le nombre mystere est plus grand que {user_choise}")
        attempts -= 1
        if attempts == 0:
            break
        print(f"il te reste {attempts} essais.")
        user_choise = input("Devine un nombre ")
        while not user_choise.isdigit():
            print("Entrez un nombre valide.")
            user_choise = input(f"il te reste {attempts} essais. Devine un nombre : ")
        while int(user_choise) not in [i for i in range(101)]:
            user_choise = input("Entrez un nombre dans l'intervalle [0-100]. Devine un nombre : ")
    else:
        print("Bravo , Vous avez gagné !".upper())
        print("Fin de jeu")
        sys.exit()

if attempts == 0:
    print(f"\nMalheuresement , Vous avez echoué ! , le nombre mystere est : {MYSTER_NUMBER}".upper())
    print("Fin de jeu")



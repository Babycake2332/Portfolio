# Skrivet av Alexander Skoog för kurs Programmering 1 - 2024-09-20.
# Kommentarerna förklarar enbart de förändringar som är gjorda från version 1,
# för jämförelse och tidigare kommentarer hänvisas till Gissa Talet_v1 - uppdrag2_uppgift2.py

import random
import os # modul för åtkomst till funktionalitet ur operativsystemet.
import sys # tillåter manipulering av IDE-miljön. 

# Introduktion vid start. 
os.system('cls') # Rensar output i terminalen.
print("--------------------------- Gissa Talet ----------------------------------\n")
input("Du ska nu gissa ett tal mellan 1 och 100, tryck enter för att fortsätta...")
os.system('cls')

# Initiering av variabler för gameplay-loop.
secret_num = random.randint(1, 100)
tries, user_num = 0, 0
game_loops = 0 # initiering av omgångsräknare.
best_record = float('inf') # initiering av rekord-cache, oändligt positivt värde som default.

# Hela gameplay-loopen är nu implementerad i samma kontrollstruktur.
while True:
    user_num = int(input("\nSkriv in ett tal: "))
    os.system('cls')

    if user_num > 100 or user_num < 1:
        print("Du måste skriva in ett heltal mellan 1 och 100!")

    elif user_num > secret_num:
        print("Din gissning är för hög...")
        if abs(user_num - secret_num) <= 3:
            print("Men du är så nära att det bränns!")

    elif user_num < secret_num:
        print("Din gissning är för låg...")
        if abs(user_num - secret_num) <= 3:
            print("Men du är så nära att det bränns!")

    # Hanterar vinst i spelet.
    elif user_num == secret_num:
        print(f"Du gissade rätt! Det hemliga talet var {secret_num}!\n"
            f"Du löste mysteriet på {tries} försök.")
        game_loops += 1 # Adderar varje spelomgång i variabel.
       
        if tries < best_record:  # Kontrollerar om nuvarande försök är ett lägre antal än sparat rekord.
            best_record = tries  # Om sant ges nytt lägstavärde till variabel.

        new_game = '' # initiering av variabel för nästlad while-loop. Tom sträng för 'True'-värde i loop.

        while new_game not in ['j', 'n']: # Jämför input med strängar i lista, bryter loop vid matchning.
            new_game = input("\nVill du spela igen? J/N?: ").lower()
            os.system('cls')

            # Återställer spelplanen
            if new_game == "j":
                tries = 0
                secret_num = random.randint(1, 100)

            # Presenterar statistik för spelsessionen och avslutar programmet.
            elif new_game == "n":
                print("==============================================================")
                print(f"Du spelade {game_loops} rundor. \nDin snabbaste gissning gjorde du på bara {best_record} försök!")
                print("==============================================================")
                print("\nTack för att du spelade Gissa Talet!")
                sys.exit()

    tries += 1 # Adderar till antalet försök.

# Bingo! Skrivet av Alexander Skoog för Hermods kurs Programmering 1 2024-09-21.
import random
import os
import sys

# Funktion som hanterar huvudprogram-loop.
def main():
    # Itererar över slumpade listor och skapar en tuple av listor för bingobrickan.
    for _ in range(5):
        bingo_card = num_generator()
        bingo_card = list(bingo_card) # konverterar till lista av listor för att kunna manipulera innehållet.
    
    os.system('cls')
    # Välkomstmeddelande och utskrift av spelarens bingobricka.
    print("___________________________________________")
    print(f"Välkommen till Byhålans Pensionärsbingo.\n\nHär är din bingobricka för kvällens dragning.")
    print_card(bingo_card)
    print("___________________________________________")
    input("\nTryck ENTER för att fortsätta...")
    os.system('cls')

    print("\nLuta dig tillbaka i stolen, njut av spänningen och vänligen håll kaffesörplandet på minimal nivå...\n\nNu kör vi!\n")
    input("Tryck ENTER för att fortsätta...")
    os.system('cls')

    index = 0 # Initiering av indexräknare för plockning av bingonummer.
    current_number = draw_number() # Spelomgångens aktuella nummer.

    # Huvudloop för spel. Bryter när variabeln index är samma värde som antal element i nummerlistan.
    while index < len(current_number):
        print(f"\nBollen faller med vana ut ur tombolan. Den visar numret: {current_number[index]}\n") # Skriver ut värdet i listan som motsvarar nuvarande index.
        fill_card(bingo_card) # Anropar funktion för att fylla i bingobricka vid matchande nummer.
        print_card(bingo_card) # Skriver ut den aktuella bingobrickan, med eventuella kryss för matchade nummer.

        # Kontrollerar om bingo finns på någon rad.
        if (
            bingo_card[0][0] == 'X' and bingo_card[1][0] == 'X' and bingo_card[2][0] == 'X' and bingo_card[3][0] == 'X' and bingo_card[4][0] == 'X' or # lodrät bingo
            bingo_card[0][1] == 'X' and bingo_card[1][1] == 'X' and bingo_card[2][1] == 'X' and bingo_card[3][1] == 'X' and bingo_card[4][1] == 'X' or # +
            bingo_card[0][2] == 'X' and bingo_card[1][2] == 'X' and bingo_card[2][2] == 'X' and bingo_card[3][2] == 'X' and bingo_card[4][2] == 'X' or # ++
            bingo_card[0][3] == 'X' and bingo_card[1][3] == 'X' and bingo_card[2][3] == 'X' and bingo_card[3][3] == 'X' and bingo_card[4][3] == 'X' or # +++
            bingo_card[0][4] == 'X' and bingo_card[1][4] == 'X' and bingo_card[2][4] == 'X' and bingo_card[3][4] == 'X' and bingo_card[4][4] == 'X' or # ++++
            bingo_card[0][0] == 'X' and bingo_card[1][1] == 'X' and bingo_card[2][2] == 'X' and bingo_card[3][3] == 'X' and bingo_card[4][4] == 'X' or # diagonal bingo upp-vä -> ned-hö
            bingo_card[4][0] == 'X' and bingo_card[3][1] == 'X' and bingo_card[2][2] == 'X' and bingo_card[1][3] == 'X' and bingo_card[0][4] == 'X' or # diagonal bingo ned-vä -> upp-hö
            bingo_card[0][0] == 'X' and bingo_card[0][1] == 'X' and bingo_card[0][2] == 'X' and bingo_card[0][3] == 'X' and bingo_card[0][4] == 'X' or # vågrät bingo
            bingo_card[1][0] == 'X' and bingo_card[1][1] == 'X' and bingo_card[1][2] == 'X' and bingo_card[1][3] == 'X' and bingo_card[1][4] == 'X' or # +
            bingo_card[2][0] == 'X' and bingo_card[2][1] == 'X' and bingo_card[2][2] == 'X' and bingo_card[2][3] == 'X' and bingo_card[2][4] == 'X' or # ++ 
            bingo_card[3][0] == 'X' and bingo_card[3][1] == 'X' and bingo_card[3][2] == 'X' and bingo_card[3][3] == 'X' and bingo_card[3][4] == 'X' or # +++
            bingo_card[4][0] == 'X' and bingo_card[4][1] == 'X' and bingo_card[4][2] == 'X' and bingo_card[4][3] == 'X' and bingo_card[4][4] == 'X'    # ++++
        ):
            print("\nBINGO! Grattis till vinsten.")
            new_game() # Omstart-/avslutafunktion

        input("\nTryck ENTER för att fortsätta...")
        os.system('cls')
        index += 1 # Adderar 1 till variabel index för att flytta till nästa nummer i listan current_numbers.
    
    # Vid uppfyllt villkor och avslutad while-loop:
    print("Tyvärr blev det inget bingo denna gång! Bättre lycka nästa gång.\n")
    new_game()

# Genererar de nummer som ska nyttjas i respektive spelomgång.
def draw_number():
    random_draw = [] # Initiering av lista.

    for i in range(15): # STÄLL IN SPELLÄNGD HÄR.
        r = random.randint(1, 76) # Nummerspann enligt klassiskt 75-bollarsbingo.
        if r not in random_draw: # Kontrollerar att inga dubbletter tillförs initierad lista.
            random_draw.append(r)

    return random_draw

# Fyller i bingobrickan med ett X där matchande nummer finns.
def fill_card(player_card):
    # Felhantering när annat värde än ett heltal fylls i vid inmatning.
    while True:
        try:
            current_num = int(input("Fyll i din bingobricka med det dragna numret: ")) # Datatyp konverterat till heltal för att kunna jämföras med bingobrickans listor (bingo_card).
            break
        except ValueError:
            print("Var vänlig ange ett giltigt nummer.\n")

    for lists in player_card: # Itererar alla listor i spelarens bricka (list of lists).
        for i, num in enumerate(lists): # Itererar över varje nummer i respektive lista (dubbla index lista och position i lista).
            if num == current_num: # Kontrollsats om angivet nummer finns på brickan.
                lists[i] = 'X' # Ersätter matchat index med sträng X.
                print("\nNumret matchar din bingobricka! Du sätter ett X i rätt rad.")

    return player_card

#Genererar lista med slumpmässiga nummer till respektive variabel. Används för att skapa spelarens bingobricka.
def num_generator():
    B = random.sample(range(1, 16), 5)
    I = random.sample(range(16, 31), 5)
    N = random.sample(range(31, 46), 5)
    G = random.sample(range(46, 61), 5)
    O = random.sample(range(61, 76), 5)

    return B, I, N, G, O

# Skriver ut bingobrickan i terminalen.
# Dubbla index i lista av listor (högra index specificerar respektive listas index, vänstra index respektive värde i specificerad lista).
# >3 är formatering för f-strängen. > = högerställd, 3 = Varje värde tar ett utrymme av tre tecken, fyller ut med white space om färre än tre tecken.
def print_card(bingo_card):
    print('\n   B   I   N   G   O   ')
    print(f' {bingo_card[0][0]:>3} {bingo_card[1][0]:>3} {bingo_card[2][0]:>3} {bingo_card[3][0]:>3} {bingo_card[4][0]:>3}')
    print(f' {bingo_card[0][1]:>3} {bingo_card[1][1]:>3} {bingo_card[2][1]:>3} {bingo_card[3][1]:>3} {bingo_card[4][1]:>3}')
    print(f' {bingo_card[0][2]:>3} {bingo_card[1][2]:>3} {bingo_card[2][2]:>3} {bingo_card[3][2]:>3} {bingo_card[4][2]:>3}')
    print(f' {bingo_card[0][3]:>3} {bingo_card[1][3]:>3} {bingo_card[2][3]:>3} {bingo_card[3][3]:>3} {bingo_card[4][3]:>3}')
    print(f' {bingo_card[0][4]:>3} {bingo_card[1][4]:>3} {bingo_card[2][4]:>3} {bingo_card[3][4]:>3} {bingo_card[4][4]:>3}')

# Startar om eller avslutar programmet efter spelarens önskemål.
def new_game():
    new_game = ''
    while new_game not in ['j', 'n']: # Jämför input med strängar i lista, bryter loop vid matchning.
        new_game = input("\nVill du spela igen? J/N?: ").lower()
        os.system('cls')

        # Omstart av programmet genom anrop till huvudfunktion.
        if new_game == "j":
            main()

        elif new_game == "n":
            print("==================================================")
            print(f"Tack för att du spelade Byhålans Pensionärsbingo!")
            print("==================================================")
            sys.exit()

main() # Anropar main()-funktion och startar programmet. Ingen kod har exekverats innan detta.

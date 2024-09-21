# Skrivet av Alexander Skoog för kurs Programmering 1 2024-08-31.

import random

secret_num = random.randint(1, 100) # Slumpmässigt nummer mellan och inklusive parametrarna.

print("--- Gissa Talet ---\n")
print("Du ska nu gissa ett tal mellan 1 och 100, så varsågod...")
        
tries, user_num = 0, 0 # Initiering av räknare och användar-input med defaultvärde 0.

while user_num != secret_num: # Loopar till dess att användaren gissar rätt.
    user_num = int(input("\nSkriv in ett tal: ")) # Omvandlar användarens nummer till ett heltal.

    # Kontrollerar om användaren befinner sig mellan specificerade värden.
    if user_num > 100 or user_num < 1:
        print("Du måste skriva in ett heltal mellan 1 och 100!")

    # Om gissningen är för hög - påtala i output, samt om numren är nära varandra.
    elif user_num > secret_num:
        print("Din gissning är för hög...")
        if abs(user_num - secret_num) <= 3: # Kontrollerar om gissningen är inom absolut värde om 3.
            print("Men du är så nära att det bränns!")

    elif user_num < secret_num:
        print("Din gissning är för låg...")
        if abs(user_num - secret_num) <= 3:
            print("Men du är så nära att det bränns!")

    tries += 1 # Adderar till antalet försök.

print(f"Du gissade rätt! Det hemliga talet var {secret_num}!\n"
    f"Du löste mysteriet på {tries} försök.")

input("\nTryck Enter för att avsluta...")

# Skrivet av Alexander Skoog för kurs Programmering 1 Hermods 2024-08-27.

from datetime import date # Modul för datum och tid, specifikt objektet date för år, månad, dag.

print("Välkomna till denna pensionssimulator!\n")
name = input("Vad heter du i förnamn? > ")
age = int(input("Hur gammal är du? > ")) # Tar emot användardata som heltal.

current_date = date.today() # Hämtar dagens datum.
current_year = current_date.year # Hämtar enbart årtalet ur dagens datum.

year_born = current_year - age
retirement_year = year_born + 65 # Födelseår adderat med median-värde pensionsålder i Sverige (Pensionsmyndigheten 2024).

years_left = retirement_year - current_year # Antal år kvar till pension.

# Kontroll av när pensionsålder infinner sig.
if years_left < 0: # Om åldern överstiger median, påtala i output.
    print(f"\nHej {name}, du borde redan ha gått i pension. Lämna kontoret omedelbart!")

elif years_left == 0: # Om ålder är samma som median, påtala i output.
    print(f"\nHej, {name}, du kan gå i pension från och med i år. Grattis!")
    
else: # I alla andra fall presenteras i output differensen mellan ålder och median pensionsålder.
    print(f"\nHej {name}. Du går i pension om {years_left} år.")

input("\nTryck Enter för att avsluta...")

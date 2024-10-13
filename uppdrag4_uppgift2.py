# Bastutemperatur. Skrivet av Alexander Skoog för Hermods kurs Programmering 1 - 2024-09-22.
import random
import sys

# Överlagringsmetoder är så vitt jag förstår inte en feature i Python. 
# Däremot kan man implementera valfria parametrar och kontrollsatser för att simulera liknande funktion.

def fahr_to_cel(fahrenheit: int, secret=None):
    if secret == 0: # Kontrollsats om användarinmatning ska trigga överraskningsmoment.
        surprise_temp = int(random.randint(1, 500))
        print(f"\nTermometern ger kort ifrån sig en serie märkliga ljud och visar sedan temperaturen {fahr_to_cel(surprise_temp)}°C.\n")
    else:
        celsius = (fahrenheit - 32) * 5/9
        return '{0:.5g}'.format(celsius) # formaterar returvärdet med 5 tecken. g ignorerar släpande nollor.

def main():
    celsius = 0

    # Programloop med felhantering.
    while celsius < 82 or celsius > 87:
        try:
            fahrenheit = int(input("Fyll i temperaturen (°F) för att konvertera till celsius: "))
            celsius = float(fahr_to_cel(fahrenheit))
            
            if fahrenheit == 0: # Särskild trigger. Anropar slumpgenererat nummer för temperaturkonvertering.
                fahr_to_cel(None, fahrenheit) # Anrop med enbart det valfria trigger-argumentet.

            elif celsius < 82:
                print(f"\nNuvarande temperatur är {celsius}°C. Bastun är för kall!\n")
            elif celsius > 87:
                print(f"\nNuvarande temperatur är {celsius}°C. Bastun är för varm!\n")
            else:
                print(f"\nTemperaturen är nu lagom {celsius}°C.\n")

        except ValueError: # Skriver ut om inmatat värde är någonting annat än ett heltal.
            print("\nVänligen skriv ett giltigt nummer.\n")

main()
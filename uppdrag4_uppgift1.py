# Fahrenheit to Celsius converter. Skapad av Alexander Skoog för Hermodskurs Programmering 1 - 2024-09-21.
def fahr_to_cel(fahrenheit: int):
    celsius = round((fahrenheit - 32) * 5/9)
    return celsius

def main():
    f_temp = int(input("Fyll i temperaturen (°F) för att konvertera till celsius: "))
    print(f"\n{f_temp}°F är detsamma som {fahr_to_cel(f_temp)}°C.")

main()
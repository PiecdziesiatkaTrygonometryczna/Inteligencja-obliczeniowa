#-------
#---D---
#-------

from datetime import datetime, date
import math

# użyłem chatgpt 3.5

# prompt: wklejenie treści skryptu oraz treść:
# "co poprawiłbyś w tym programie np. lepsze formatowanie, nazwy zmiennych, zrobienie powtarzalnych sekwencji w funkcjach?"

# jak widać, liczenie fali i wyświetlanie komunikatów, gdzie ja napisałem praktycznie to samo 3 razy, on zmienił na jedną funkcję.
# wstawił też pytanie użytkownika o datę urodzenia do pętli while True, oraz wyświetlenie errora po podaniu nieprawidłowych danych


# wynik:

# początkowo funkcję calculate_wave zrobił tak:

# def calculate_wave(days, period):
#     wave = math.sin(2 * math.pi / period * days)
#     if wave > 0.5:
#         return "Gratuluję dobrego wyniku!"
#     elif wave < -0.5:
#         return "Pocieszam Cię w złym dniu"
#     return ""


# po zwróceniu uwagi, do return wstawił również wave, więcej o tym napisalem niżej
def calculate_wave(days, period):
    wave = math.sin(2 * math.pi / period * days)
    if wave > 0.5:
        return wave, "Gratuluję dobrego wyniku!"
    elif wave < -0.5:
        return wave, "Pocieszam Cię w złym dniu"
    return wave, ""

print("Podaj swoje imię")
name = input()

while True:
    try:
        print("Podaj rok urodzenia")
        year_of_birth = int(input())
        print("Podaj miesiąc urodzenia")
        month_of_birth = int(input())
        print("Podaj dzień urodzenia")
        day_of_birth = int(input())

        date_of_birth = date(year_of_birth, month_of_birth, day_of_birth)
        break
    except ValueError:
        print("Podano nieprawidłowe dane. Spróbuj ponownie.")

today = date.today()
amount_of_days = (today - date_of_birth).days
current_day_of_life = amount_of_days + 1  # Dzisiaj jest Twój x dzień życia

print(f"Witaj {name}. Dzisiaj jest Twój {current_day_of_life} dzień życia.")

# fizyczna = calculate_wave(amount_of_days, 23)
# emocjonalna = calculate_wave(amount_of_days, 28)
# intelektualna = calculate_wave(amount_of_days, 33)

# print(f"Twoja fizyczna fala: {fizyczna}")
# print(f"Twoja emocjonalna fala: {emocjonalna}")
# print(f"Twoja intelektualna fala: {intelektualna}")

# najpierw dał tak jak wyżej ^, ale w ten sposób w konsoli nie wyświetlały się wartości sinusów.
# zwróciłem mu na to uwagę i poprawił w poniższy sposób, oraz zmienił returny w funkcji calculate_wave.

fizyczna, fizyczna_message = calculate_wave(amount_of_days, 23)
emocjonalna, emocjonalna_message = calculate_wave(amount_of_days, 28)
intelektualna, intelektualna_message = calculate_wave(amount_of_days, 33)

print(f"Twoja fizyczna fala: {fizyczna}. {fizyczna_message}")
print(f"Twoja emocjonalna fala: {emocjonalna}. {emocjonalna_message}")
print(f"Twoja intelektualna fala: {intelektualna}. {intelektualna_message}")


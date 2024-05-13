#-------
#---E---
#-------

import datetime
import math

# użyłem chatgpt 3.5
# prompt: po prostu treść polecenia (wstęp, podpunkt A oraz B (bez informacji o używaniu narzędzi AI))
# dodatkowo opisałem mu czym dokładnie jest "t" we wzorach:
# "gdzie t, to ile łącznie dni żyjesz. w dniu twoich narodzin, t=0, w kolejnym dniu, t=1, itd."

# początkowo zwrócil skrypt, który spełnił wszystkie wymogi zadania oprócz sprawdzania, czy w 
# przypadku niskiego wyniku jutro będzie lepiej. Zwrócilem mu na to uwagę, i zwrócił
# skrypt, w którym pojawił się inny błąd. Niezależnie od wprowadzonych danych, skrypt zawsze zwracał wyniki 0.00
# Okazało się, że do funkcji calculate_biorhythms, zamiast ilości dni życia osoby, podstawiał 0.
# napisałem mu tylko, że to podejrzane, że program zawsze zwraca 0.00.
# znalazł błąd, poprawił i program działa w 100%. reszta to tylko formatowanie i "ulepszanie" kodu

# co ciekawe, sam z siebie nie zrobił funkcji odpowiedzialnej za wyświetlanie wyników,
# tylko zrobił 3 identyczne instrukcje warunkowe dla każdego biorytmu.
# Tak samo nie sprawdza, czy rok, miesiac i dzień są cyframi.
# napisałem mu:
# "co jeszcze byś usprawnił w tym skrypcie?"
# wtedy zauważył dokładnie to, co wyżej wymieniłem, i poprawił

# na początku zrobił wyniki dobrze, ale po którejś poprawce chat pocieszał użytkownika,
# gdy wynik był mniejszy od 0,5 zamiast od -0,5. To poprawiłem już ręcznie.

#15:37 start i pisanie promptu
#15:40 wyslanie do chata
#15:43 otrzymanie satysfakcjonującego skryptu.
# więc łącznie 6 minut, co jest zawrotne 8.5x szybciej, niż ja. 


# odpowiedź (komenatarze poniżej zrobił chat):

class InvalidDateError(Exception):
    pass

def get_birth_date():
    while True:
        try:
            year = int(input("Podaj rok urodzenia: "))
            month = int(input("Podaj miesiąc urodzenia: "))
            day = int(input("Podaj dzień urodzenia: "))
            birth_date = datetime.datetime(year, month, day)
            if birth_date <= datetime.datetime.now():
                return birth_date
            else:
                print("Podano datę z przyszłości. Spróbuj ponownie.")
        except ValueError:
            print("Podano niepoprawną datę. Spróbuj ponownie.")
        except Exception as e:
            print("Wystąpił błąd:", e)

def calculate_biorhythms(birth_date, days_alive):
    # Obliczanie wartości biorytmów dla danych cykli
    physical = math.sin((2 * math.pi / 23) * days_alive)
    emotional = math.sin((2 * math.pi / 28) * days_alive)
    intellectual = math.sin((2 * math.pi / 33) * days_alive)
    
    return physical, emotional, intellectual

def check_next_day_biorhythm(birth_date):
    # Obliczenie dni życia
    today = datetime.datetime.now()
    days_alive = (today - birth_date).days
    
    # Obliczanie wyników biorytmów dla następnego dnia
    physical_next, emotional_next, intellectual_next = calculate_biorhythms(birth_date, days_alive + 1)
    
    return physical_next, emotional_next, intellectual_next

def display_results(name, days_alive, physical, emotional, intellectual):
    print("\nWitaj {}, dzisiaj jest {} dzień twojego życia.".format(name, days_alive))
    print("Twoje wyniki biorytmów:")
    print("Fizyczny: {:.2f}".format(physical))
    print("Emocjonalny: {:.2f}".format(emotional))
    print("Intelektualny: {:.2f}".format(intellectual))

def check_biorhythm(name, result, next_day_result, result_type):
    if result > 0.5:
        print("Gratulacje! Twój wynik biorytmu {} jest wysoki.".format(result_type))
    elif result < -0.5:
        print("Uważaj, twój wynik biorytmu {} jest niski.".format(result_type))
        # Sprawdzenie wyniku biorytmu na następny dzień
        if abs(next_day_result) > abs(result):
            print("Nie martw się. Jutro będzie lepiej!")
    else:
        print("Twój wynik biorytmu {} jest w normie.".format(result_type))


def main():
    # Pytanie o dane użytkownika
    name = input("Podaj swoje imię: ")
    try:
        birth_date = get_birth_date()
    except InvalidDateError:
        print("Podano niepoprawną datę urodzenia.")
        return
    
    # Obliczenie dni życia
    days_alive = (datetime.datetime.now() - birth_date).days
    
    # Obliczenie wyników biorytmów
    physical, emotional, intellectual = calculate_biorhythms(birth_date, days_alive)
    
    # Wyświetlenie wyników
    display_results(name, days_alive, physical, emotional, intellectual)
    
    # Sprawdzenie wyników biorytmów
    check_biorhythm(name, physical, check_next_day_biorhythm(birth_date)[0], "fizycznego")
    check_biorhythm(name, emotional, check_next_day_biorhythm(birth_date)[1], "emocjonalnego")
    check_biorhythm(name, intellectual, check_next_day_biorhythm(birth_date)[2], "intelektualnego")

if __name__ == "__main__":
    main()

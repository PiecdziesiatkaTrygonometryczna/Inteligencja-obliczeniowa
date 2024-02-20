from datetime import datetime
from datetime import date
import math


#-------
#---A---
#-------

print("Podaj swoje imę")
name = input()
print("Podaj rok urodzenia")
yearOfBirth = int(input())
print("Podaj miesiąc urodzenia")
monthOfBirth = int(input())
print("Podaj dzień urodzenia")
dayOfBirth = int(input())

dateOfBirth = date(yearOfBirth, monthOfBirth, dayOfBirth)
print(dateOfBirth)

today = date.today()
amountOfDays = (today - dateOfBirth).days

print("Witaj " + name + ". Dzisiaj jest twój " + str(amountOfDays + 1) + " dzień życia.")


#-------
#---B---
#-------


# nie byłem pewien dokładnie, czy w poleceniu:

# "Po obliczeniu biorytmów program powinien sprawdzić, czy są one wysokie (powyżej 
# 0,5) i pogratulować dobrego wyniku, niskie (mniejsze niż -0,5) i pocieszyć w złym dniu."

# czy chodziło o każdy biorytm z osobna, czy zbiorczo, czyli np. jeżeli wszystkie 3 biorytmy byłyby większe od 0,5,
# dopiero wtedy wyświetlałby się komunikat. Zakładam, że sytuacja w której wszystkie 3 biorytmy są większe od 0,5,
# lub wszystkie są mniejsze od -0,5, występuje stosunkowo rzadko, dlatego zrobiłem komunikat dla każdego biorytmu
# z osobna.

fizyczna = math.sin(2*math.pi/23*amountOfDays)
print("Twoja fizyczna fala: " + str(fizyczna), end='. ')
if fizyczna > 0.5:
    print("Gratuluję dobrego wyniku!")
elif fizyczna < -0.5:
    print("Pocieszam Cię w złym dniu", end='. ')
    fizycznaJutro = math.sin(2*math.pi/23*(amountOfDays+1))
    if fizycznaJutro > fizyczna:
        print("Nie martw się. Jutro będzie lepiej!")
    else:
        print()
else:
    print()

emocjonalna = math.sin(2*math.pi/28*amountOfDays)
print("Twoja emocjonalna fala: " + str(emocjonalna), end='. ')
if emocjonalna > 0.5:
    print("Gratuluję dobrego wyniku!")
elif emocjonalna < -0.5:
    print("Pocieszam Cię w złym dniu", end='. ')
    emocjonalnaJutro = math.sin(2*math.pi/28*(amountOfDays+1))
    if emocjonalnaJutro > emocjonalna:
        print("Nie martw się. Jutro będzie lepiej!")
    else:
        print()
else:
    print()

intelektualna = math.sin(2*math.pi/33*amountOfDays)
print("Twoja intelektualna fala: " + str(intelektualna), end='. ')
if intelektualna > 0.5:
    print("Gratuluję dobrego wyniku!")
elif intelektualna < -0.5:
    print("Pocieszam Cię w złym dniu", end='. ')
    intelektualnaJutro = math.sin(2*math.pi/233*(amountOfDays+1))
    if intelektualnaJutro > intelektualna:
        print("Nie martw się. Jutro będzie lepiej!")
    else:
        print()
else:
    print()


#-------
#---C---
#-------
    
#skrypt tworzyłem w godzinach 14:31 - 15:22, czyli 51 minut 😀
from mlist import MLista
import sys


class Main:

    def argument():
        while True:
            x = input("Podaj liczbe: ")
            try:
                x = int(x)
                return x
            except ValueError:
                print("Bład - podana wartosc nie jest liczba")
                return False

    while True:
        cap = input("Podaj poczatkowy rozmiar listy: ")
        try:
            cap = int(cap)
            lista = MLista(cap)
            break
        except ValueError:
            print("Bład - podana wartosc nie jest liczba")

    while True:
        operacja = input("Wybierz typ operacji: (pisz, dodaj_element, "
                         "znajdz, pobierz, rozmiar, pojemnosc, "
                         "usun_powtorzenia, odwroc, zwieksz_pojemnosc, "
                         "zmniejsz_pojemnosc, wyjscie)")
        operacja = operacja.lower()
        if operacja == "pisz":
            lista.pisz()
        elif operacja == "dodaj_element":
            x = argument()
            lista.dodaj_element(x)
        elif operacja == "znajdz":
            x = argument()
            lista.znajdz(x)
        elif operacja == "pobierz":
            x = argument()
            lista.pobierz(x)
        elif operacja == "rozmiar":
            lista.rozmiar
        elif operacja == "pojemnosc":
            lista.pojemnosc
        elif operacja == "usun_powtorzenia":
            x = argument()
            lista.usun_powtorzenia(x)
        elif operacja == "odwroc":
            lista.odwroc
        elif operacja == "zwieksz_pojemnosc":
            x = argument()
            lista.zwieksz_pojemnosc(x)
        elif operacja == "zmniejsz_pojemnosc":
            x = argument()
            lista.zmniejsz_pojemnosc(x)
        elif operacja == "wyjscie":
            sys.exit()
        else:
            print("Bledna operacja!")

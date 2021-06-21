 from mlist import MLista

lista = MLista(4)
lista.dodaj_element(2)


def argument():
    while True:
        x = input("Podaj liczbe: ")
        try:
            x = int(x)
            return x
        except ValueError:
            print("Bład - podana wartosc nie jest liczba")
            return False


def test_argument():
    assert argument("3") == 3
    assert argument("2.5") is False
    assert argument("a") is False
    assert argument("trzy") is False


def test_dodaj_element():
    assert lista.dodaj_element(0) is True
    assert lista.dodaj_element(2) is True
    assert lista.dodaj_element(8) is True
    assert lista.dodaj_element(3) is False


def test_znajdz():
    assert lista.znajdz(0) == 1
    assert lista.znajdz(7) == -1


def test_pobierz():
    assert lista.pobierz(0) == 2
    assert lista.pobierz(1) == 0
    assert lista.pobierz(5) == "Wystapil blad."


def test_rozmiar():
    assert lista.rozmiar() == 4


def test_pojemnosc():
    assert lista.pojemnosc() == 4


def test_usun_powtorzenia():
    assert lista.usun_powtorzenia(2) is True
    assert lista.usun_powtorzenia(0) is True
    assert lista.usun_powtorzenia(3) is False


def test_rozmiar_bez_powtorzen():
    assert lista.rozmiar() == 3


def test_pojemnosc_bez_powtorzen():
    assert lista.pojemnosc() == 4


def test_zwiększ_pojemnosc():
    assert lista.zwiększ_pojemnosc(4) is True
    assert lista.zwiększ_pojemnosc(-3) is False


def test_pojemnosc_po_zwiekszeniu():
    assert lista.pojemnosc() == 8


def test_zmniejsz_pojemnosc():
    assert lista.zmniejsz_pojemnosc(2) is True
    assert lista.zmniejsz_pojemnosc(6) is False
    assert lista.zmniejsz_pojemnosc(12) is False
    assert lista.zmniejsz_pojemnosc(-2) is False


def test_pojemnosc_po_zmniejszeniu():
    assert lista.pojemnosc() == 6

class MLista:

    def __init__(self, capacity):
        self.lista = []
        self.capacity = capacity

    def pisz(self):
        print("Informacje o liscie: ")
        print("Aktualny rozmiar: " + str(len(self.lista)))
        print("Pojemnosc listy: " + str(self.capacity))
        print("Elementy listy: ", self.lista)

    def dodaj_element(self, x):
        if self.capacity > len(self.lista):
            self.lista.append(x)
            return True
        else:
            return False

    def znajdz(self, x):
        if x in self.lista:
            return self.lista.index(x)
        else:
            return -1

    def pobierz(self, x):
        if x >= self.capacity:
            print(self.lista[x])
        else:
            print("W liscie nie ma elementu o indeksie ", x)

    def rozmiar(self):
        print(len(self.lista))

    def pojemnosc(self):
        print(self.capacity)

    def usun_powtorzenia(self, x):
        try:
            start = 0
            bez_powtorzen = self.lista[:start+1]
            for item in self.lista[start:]:
                if item == x:
                    continue
                else:
                    bez_powtorzen.append(item)
            return bez_powtorzen, True
        except ValueError:
            print("Brak liczby ", x, " na liscie")
            return False

    def odwroc(self):
        print(self.lista.reverse())

    def zwieksz_pojemnosc(self, x):
        if x < 0:
            return False
        else:
            self.capacity += x
            return True

    def zmniejsz_pojemnosc(self, x):
        if x < 0 or (len(self.lista)) >= (self.capacity - x):
            return False
        else:
            self.capacity -= x
            return True

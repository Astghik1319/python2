Anna Matyjewicz i projekt zaliczeniowy nr 1

Pliki dostępne w repozytorium na GitHub pod adresem: https://github.com/Astghik1319/python2

Opis programu:

Moduł mylist.py zawiera klasę MLista, w której znajdują się:
- konstruktor listy o pojemności capacity,
- funkcja pisz wypisująca informacje o liści: jej akutalny rozmiar, pojemność oraz wypisuje elementy tej listy,
- funkcja dodaj_element pozwalająca na dodanie elementu do listy (o ile ilość elementów w liście jest mniejsza niż jej pojemność)
- funkcja znajdz, która znajduje podany element i zwraca numer indeksu, pod którym znajduje się ten element,
- funkcja pobierz, która wypisuje element o podanym indeksie, o ile indeks jest mniejszy lub równy pojemności listy
- funkcja rozmiar zwracająca informację o aktualnym rozmiarze listy
- funkcja pojemnosc zwracająca informację o pojemnosci listy
- funckja usun_powtorzenia, która usuwa z listy powtórzenia wybranego elementu, zostawia ten element w miejscu, gdzie pojawił się pierwszy raz
- funkcja odwroc, która odwraca listę - odwraca kolejność występowania kolejnych elementów
- funkcja zwieksz_pojemnosc, która większa pojemność listy o podaną liczbę o ile podana liczba jest dodatnia
- funckja zmniejsz_pojemnosc, która zmniejsza pojemność listy o podaną liczbę o ile ta jest dodatnia oraz pojemność listy po zmniejszeniu będzie większa lub równa ilości elementów znajdujących się na liście

Moduł test_mlist.py, który importuje klasę MLista, tworzy listę o pojemności 4 i z jednym elementem o wartości 2, a następnie wykonuje testy na każdej funkcji zgodnie z kolejnością, z jaką zostały one zdefiniowane w module mylist.py, nazwy testów odpowiadają nazwom testowanych funckji

Program main.py:
Zawiera klasę main, która zawiera definicję funkcji argument umożliwiającej podanie argumentu w funkcjach klasy MLista, które wymagają podania argumentu (np. dodaj_element, usun_powtorzenia, zmniejsz_pojemnosc).
Po uruchomieniu programu rozpoczyna się pętla while i wyświetla się komunikat z prośbą o podanie początkowego rozmiaru listy. Po podaniu poprawnej wartości zostaje utworzona lista o podanej pojemności, podanie błędnej wartości sprawi, że wyświetli się komunikat o błędzie i pętla wywoła się kolejny raz.
Po poprawnym utowrzeniu listy rozpocznie się druga pętla while i wyświetli się informacja z możliwymi operacjami do wyboru. Kazda operacja do wyboru odpowiada kolejnej funkcji z pliku mlist.py.
Wybranie operacji wyjscie kończy działanie programu.
Podanie błędnej operacji sprawi, że na ekranie pojawi się komunikat "Bledna operacja!" i pętla wykona się jeszcze raz. Przy podawaniu błędnych operacji pętla działa w nieskończoność. 


Kod źródłowy został sprawdzony na zgodność z dokumentacją PEP8 przy pomocy programu flake8
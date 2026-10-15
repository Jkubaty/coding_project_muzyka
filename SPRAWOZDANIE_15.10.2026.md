# Sprawozdanie z Zadania Laboratoryjnego nr \[NUMER]

**Przedmiot:** Programowanie w języku Python (`IwIK-S1`)  
**Projekt:** MusicLab
**Zespół (Autorzy):**

1. Hubert Homa (nr albumu: D/164831) – login Git: `HubertHoma`
2. Julia Kubaty (nr albumu: D/165576) – login Git: `JKubaty`  
3. Jakub Potoniec (nr albumu: D/164869) - login Git: `jakpot6`
**Data oddania:** 15.10.2026

\---

## 1\. Cel i Zakres Inżynierski Zadania

*(Zwięzły opis – maksymalnie 2–3 zdania. Jaki problem rozwiązuje ten etap i jakie mechanizmy języka Python zostały zbadane/zaimplementowane).*

Celem naszego projektu było wywoływanie funkcji w menu. Wyświetlanie biblioteki utworów, formularz z dodawaniem nowego utworu oraz filtrem biblioteki. Zostały użyte funkcje Pythona: match(); try: except: ; funkcje while oraz definiowanie funkcji przez def()

\---

## 2\. Architektura Rozwiązania i Struktura Modułów

*(Wykaz zrealizowanych plików w katalogu `src/` wraz z przypisaniem ich odpowiedzialności).*

* `src/data.py` –  Trzymamy dane muzyk w systemie
* `src/validators.py` – sprawdza występujące błedy
* `src/services.py` – fukcja do wyświetlania biblioteki muzyk
* `src/main.py` – głowna pętla programu

\---

## 3\. Kluczowy Fragment Kodu i Uzasadnienie Inżynierskie

*(Wybrany, najważniejszy lub najciekawszy fragment kodu źródłowego zrealizowany w tym etapie – maksymalnie 15–25 linii).*

```python
# Wklej tutaj kluczowy fragment kodu źródłowego
def main():

&#x20;   running = True

&#x20;   while running:

&#x20;       print\_menu()

&#x20;       choice = input("Wybierz liczbę od 1 do 4: ")

&#x20;       running = handle\_menu\_choice(choice)

```

**Uzasadnienie wyboru:**  
*(Krótkie wyjaśnienie: dlaczego zaimplementowano to w taki sposób, jak obsłużono błędy lub jakie wzorce projektowe zastosowano).*

*Główna pętla rozpoczywająca wołanie funkcji. Prosi o wybranie liczby od 1 do 4 i wywołuję potrzebne funkcje do działania kodu.*

\---

## 4\. Scenariusze Weryfikacji i Wyniki Testów

*(Dowód działania programu w konsoli. Należy przedstawić przynajmniej dwa scenariusze).*

### Scenariusz A: Ścieżka poprawna (Happy Path)

* **Dane wejściowe:** \[Opis danych]
* **Oczekiwany i uzyskany wynik:**

```text

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;  MusicLib   

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

1\. Wyświetl biblioteke utworów audio

2\. Dodaj nowy utwór

3\. Filtruj biblioteke

4\. Opuszczenie programu

\------------------------------

Wybierz liczbę od 1 do 4: 1

ID    Tytuł      Czas trwania \[s] autor     

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

1()()(nirvana)

2()()(eminem)

3()()(aaaaaa)

4()()(dddddd)



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[Wklej listing z konsoli lub opis poprawnego zachowania]
```

### Scenariusz B: Obsługa błędów i wartości brzegowych

* **Dane wejściowe (błędne):** \[np. litery zamiast cyfr, puste wejście, wartość spoza zakresu]
* **Reakcja programu:**

```text

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;  MusicLib   

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

1\. Wyświetl biblioteke utworów audio

2\. Dodaj nowy utwór

3\. Filtruj biblioteke

4\. Opuszczenie programu

\------------------------------

Wybierz liczbę od 1 do 4: 2

podaj czas grania (MM:SS)10

czas trwania jest niepoprawny

podaj czas grania (MM:SS)
\[Wklej listing z konsoli pokazujący bezpieczną reakcję na błąd]
```

\---

## 5\. Podział Pracy w Zespole

*(Precyzyjne i uczciwe rozliczenie wkładu obu członków zespołu – weryfikowane z historią commitów `git log`).*

* **Hubert Homa:**

  * Odpowiedzialność za moduły: `src/validators.py i main.py`
  * Zaimplementowane funkcjonalności: walidacja menu, wygląd menu
  * Liczba wykonanych commitów: 4
* **Julia Kubaty:**

  * Odpowiedzialność za moduły: `src/main.py handle\_menu\_choice()`
  * Zaimplementowane funkcjonalności: walidacja formularza czasu
  * Liczba wykonanych commitów: 3
* **Jakub Potoniec:**

  * Odpowiedzialność za moduły: `src/services.py`
  * Zaimplementowane funkcjonalności: fukcja wyświetlania menu
  * Liczba wykonanych commitów: 1




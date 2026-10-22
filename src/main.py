from dataclasses import fields
from pdb import exit_with_permission_help_text
from unittest import result
import json
from services import display_items, add_item
from validators import get_int_input, get_non_empty_string
from data import filter_menu, Library_menu, Playlists
from pathlib import Path
from storage import export_to_csv, import_from_csv, fields




def print_menu():
    print("\n" + "*" * 30)
    print("   MusicLab   ")
    print("*" * 30)
    print(f"1. Wyświetl biblioteke utworów audio")
    print(f"2. Dodaj nowy utwór")
    print(f"3. Filtruj biblioteke")
    print(f"4. Pobierz biblioteke utworów")
    print(f"5. Importuj biblioteke")
    print(f"6. test")
    print(f"7. Opuszczenie programu")
    print("-" * 30)

def displayplaylists():
    for i in range(len(Playlists)):
        print(str(i + 1), '. ', Playlists[i])

def getfilename(playlistnum):
    playlistname = Playlists[int(playlistnum)-1]
    return playlistname


def display_list(filename,wanttoadd):
    with open(filename, "r", encoding="utf-8") as file:
        items = json.load(file)

    for item in items:
        print(item)
    if wanttoadd:
        songtoadd = input("Enter song to add: ")
        items.append(songtoadd)
        json.dump(items, file, indent=4)

def handle_menu_choice(choice: str) -> bool:
    match choice.strip():
        case "1":
            display_items(Library_menu)
        case "2":
            validduration = False
            while not validduration:
                duration = input('podaj czas grania (MM:SS)')
                parts = duration.split(':')
                try:
                    if len(parts[0]) == 2 and int(parts[0]) <= 59:
                        if len(parts[1]) == 2 and int(parts[1]) <= 59:
                            validduration = True
                    else:
                        print('czas trwania jest niepoprawny')
                except:
                    print('czas trwania jest niepoprawny')

            new_item_data = {
                "title": get_non_empty_string("Podaj tytuł: "),
                "duration": (duration),
                "author": get_non_empty_string("Podaj nazwisko: "),

            }
            add_item(Library_menu, new_item_data)
        case "3":
            query = input("Podaj tytul do wyszukania: ")
            results = filter_menu(Library_menu, query)

            if results:
                for item in results:
                    print(f"{item['title']} - {item['author']}")
            else:
                print(f"Niestety nie istnieje")
        case "4":
            try:
                export_to_csv(Path("data/tracks_library.csv"), Library_menu, fields)
                print(f"Biblioteka pobrana pomyślnie")
            except:
                print(f"Biblioteka nie została pobrana")
        case "5":
            try:
                Library_menu.extend(import_from_csv(Path("data/tracks_library.csv")))
                print(f"Import zakończony pomyślnie")
            except FileNotFoundError:
                print(f"Nie ma pliku do importu")

        case "6":
            displayplaylists()
            getfilename()

        case "7" | "end" | "exit":
            return False
        case _:
            print(f"Błąd, opcja jest nie znana. Wybierz wartość"
                  f"od 1 do 6")
    return True


def main():
    running = True
    while running:
        print_menu()
        choice = input("Wybierz liczbę od 1 do 6: ")
        running = handle_menu_choice(choice)

if __name__ == "__main__":
    main()

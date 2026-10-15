from unittest import result

from services import display_items, add_item
from validators import get_int_input, get_non_empty_string
from data import filter_menu, Library_menu





def print_menu():
    print("\n" + "*" * 30)
    print("   MusicLib   ")
    print("*" * 30)
    print(f"1. Wyświetl biblioteke utworów audio")
    print(f"2. Dodaj nowy utwór")
    print(f"3. Filtruj biblioteke")
    print(f"4. Opuszczenie programu")
    print("-" * 30)

def handle_menu_choice(choice: str) -> bool:
    match choice.strip():
        case "1":
            display_items(Library_menu)
        case "2":
            new_item_data={
                "title": get_non_empty_string("Podaj tytuł: "),
                "duration": get_non_empty_string("Podaj czas trwania [s]: "),
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
        case "4" | "end" | "exit":
            return False
        case _:
            print(f"Błąd, opcja jest nie znana. Wybierz wartość"
                  f"od 1 do 4")
    return True

def main():
    running = True
    while running:
        print_menu()
        choice = input("Wybierz liczbę od 1 do 4: ")
        running = handle_menu_choice(choice)

if __name__ == "__main__":
    main()
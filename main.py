from services import display_items, add_item
from validators import get_int_input, get_non_empty_string
from data import Library_menu
import math





def print_menu():
    print("\n" + "*" * 30)
    print("   MusicLib   ")
    print("*" * 30)
    print(f"1. Wyświetl biblioteke utworów audio")
    print(f"2. Dodaj nowy utwór")
    print(f"3. Symuluj odtwarzacz")
    print(f"4. Opuszczenie programu")
    print("-" * 30)

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
                    if parts[0] == 2 and int(parts[0]) <= 59:
                        if parts[1] == 2 and int(parts[1]) <= 59:
                            validduration = True
                    else:
                        print('czas trwania jest niepoprawny')
                except:
                    print('czas trwania jest niepoprawny')
            
            new_item_data={
                "title": get_non_empty_string("Podaj tytuł: "),
                "duration": duration),
                "author": get_non_empty_string("Podaj nazwisko: "),
            }
            add_item(Library_menu, new_item_data)
        case "3":
            return True
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

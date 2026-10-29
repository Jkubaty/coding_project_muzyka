
import json
from services import display_items, add_item
from validators import get_int_input, get_non_empty_string
from data import filter_menu, Library_menu, Playlists
from pathlib import Path
from storage import export_to_csv, import_from_csv, fields, save_catalog, load_catalog, safe_load_catalog
from backups import createbackup
NAMES_PATH = "data/playlist_names.json"



def print_menu():
    print("\n" + "*" * 30)
    print("   MusicLab   ")
    print("*" * 30)
    print(f"1. Wyświetl biblioteke utworów audio")
    print(f"2. Dodaj nowy utwór")
    print(f"3. Filtruj biblioteke")
    print(f"4. Pobierz biblioteke utworów")
    print(f"5. Importuj biblioteke")
    print(f"6. Playlisty")
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
            input("\nNaciśnij Enter, aby wrócić do menu")
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
            playlists_path = Path(__file__).resolve().parent / "data" / "playlists.json"
            save_catalog(playlists_path, Library_menu)
            print("Utwór został dodany i zapisany.")
            input("\nNaciśnij Enter, aby wrócić do menu...")
        case "3":
            query = input("Podaj tytul do wyszukania: ")
            results = filter_menu(Library_menu, query)

            if results:
                for item in results:
                    print(f"{item['title']} - {item['author']}")
                    input("\nNaciśnij Enter, aby wrócić do menu...")
            else:
                print(f"Niestety nie istnieje")
                input("\nNaciśnij Enter, aby wrócić do menu...")
        case "4":
            try:
                export_to_csv(Path("data/tracks_library.csv"), Library_menu, fields)
                print(f"Biblioteka pobrana pomyślnie")
                input("\nNaciśnij Enter, aby wrócić do menu...")
            except:
                print(f"Biblioteka nie została pobrana")
                input("\nNaciśnij Enter, aby wrócić do menu...")
        case "5":
            try:
                imported_items = import_from_csv(Path("data/tracks_library.csv"))
                added = 0
                for item in imported_items:
                    if not any(
                            existing["title"] == item["title"]
                            and existing["author"] == item["author"]
                            for existing in Library_menu
                    ):
                        add_item(Library_menu, {
                            "title": item["title"],
                            "duration": item["duration"],
                            "author": item["author"],
                        })
                        added += 1
                print(f"Import zostaw wykonany poprawnie")
                input("\nNaciśnij Enter, aby wrócić do menu...")
            except FileNotFoundError:
                print("Nie ma pliku do importu")
                input("\nNaciśnij Enter, aby wrócić do menu...")

        case "6":
            print("1. Wyświetl playlistę")
            print("2. Utwórz nową playlistę")
            sub = input("Wybierz opcję: ")

            if sub == "1":
                displayplaylists()
                num = input("Wybierz numer playlisty: ")
                name = getfilename(num)

                try:
                    with open(f"data/{name}.json", "r", encoding="utf-8") as file:
                        songs = json.load(file)
                except FileNotFoundError:
                    songs = []

                print(f"\n--- {name} ---")
                if not songs:
                    print("Playlista jest pusta.")
                for i, song in enumerate(songs, start=1):
                    if isinstance(song, dict):
                        print(f"{i}. {song['title']} - {song['author']} ({song['duration']})")
                    else:
                        print(f"{i}. {song}")

            elif sub == "2":
                name = get_non_empty_string("Podaj nazwę nowej playlisty: ")
                Playlists.append(name)

                with open(NAMES_PATH, "w", encoding="utf-8") as file:
                    json.dump(Playlists, file, indent=4, ensure_ascii=False)

                songs = []
                while True:
                    song = input("Dodaj utwór (Enter, aby zakończyć): ").strip()
                    if song == "":
                        break
                    songs.append(song)

                with open(f"data/{name}.json", "w", encoding="utf-8") as file:
                    json.dump(songs, file, indent=4, ensure_ascii=False)

                print("Playlista została utworzona.")
                print("piosenki dodane")

            input("\nNaciśnij Enter, aby wrócić do menu...")


        case "7" | "end" | "exit":
            return False
        case _:
            print(f"Błąd, opcja jest nie znana. Wybierz wartość"
                  f"od 1 do 7")
    return True


def main():
    global Library_menu
    try:
        with open(NAMES_PATH, "r", encoding="utf-8") as file:
            Playlists[:] = json.load(file)
    except FileNotFoundError:
        pass

    playlists_path = Path(__file__).resolve().parent / "data" / "playlists.json"
    createbackup(playlists_path, Path(__file__).resolve().parent / "data" / "backups")
    if playlists_path.exists():
        loaded_items = safe_load_catalog(playlists_path, Library_menu)

        if loaded_items:
            Library_menu = loaded_items
        else:
            save_catalog(playlists_path, Library_menu)
    else:
        save_catalog(playlists_path, Library_menu)

    running = True
    while running:
        print_menu()
        choice = input("Wybierz liczbę od 1 do 7: ")
        running = handle_menu_choice(choice)

if __name__ == "__main__":
    main()

def get_int_input(
        prompt: str,
        min_val: int = None,
        max_val: int = None
    ) -> int:

    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Błąd wartość jest pusta")
            continue
        try:
          val = int(raw)
          if min_val is not None and val < min_val:
             print(f"Błąd: wartość < {min_val}")
             continue
          if max_val is not None and val > max_val:
                print(f"Błąd: wartość > {max_val}")
                continue
          return val
        except ValueError:
            print(f"Błąd: '{raw}' to nie int ")
            continue

def get_non_empty_string(
        prompt: str
) ->str:
    while True:
        raw = input(prompt).strip()
        if raw:
            return raw
        print(f"Nie moze byc puste")

#get_non_empty_string(f"podaj dane: ")
#print(f"podales dane")
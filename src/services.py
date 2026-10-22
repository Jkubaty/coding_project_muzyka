from data import Library_menu


def display_items(items_list):
    print(f"{'ID':<5} {'Tytuł':<10} {'Czas trwania [s]':<10} {'autor':<10}")
    print("*" * 30)

    for item in items_list:
        print(
            f"{item['id']}"
            f"({item['title'].capitalize()})"
            f"({item['duration']})"
            f"({item['author']})"
        )






def add_item(items_list, new_item_data):
    exi_id = [ item["id"] for item in items_list]
    new_id = max(exi_id) + 1



    new_item = {
        **new_item_data,
        "id": new_id,

    }
    items_list.append(new_item)
Library_menu = [
    {
        "id": 1,
        "title": "",
        "duration": "",
        "author": "",
    },
    {
        "id": 2,
        "title": "",
        "duration": "",
        "author": "",
    },
    {
        "id": 3,
        "title": "",
        "duration": "",
        "author": "",
    },
    {
        "id": 4,
        "title": "",
        "duration": "",
        "author": "",
    }
]

def filter_menu(catalog: list[dict], query:str) -> list[dict]:
    results = []
    q = query.strip().casefold()
    for item in catalog:
        if q in item["title"].casefold():
            results.append(item)
    return results


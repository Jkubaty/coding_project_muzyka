import json

Library_menu = [
    {
        "id": 1,
        "title": "Smells Like Teen Spirit",
        "duration": "05:01",
        "author": "nirvana",
    },
    {
        "id": 2,
        "title": "Lose Yourself",
        "duration": "05:26",
        "author": "eminem",
    },
    {
        "id": 3,
        "title": "Come As You Are",
        "duration": "03:39",
        "author": "nirvana",
    },
    {
        "id": 4,
        "title": "Without Me",
        "duration": "04:50",
        "author": "eminem",
    }
]

def filter_menu(catalog: list[dict], query:str) -> list[dict]:
    results = []
    q = query.strip().casefold()
    for item in catalog:
        if q in item["title"].casefold():
            results.append(item)
    return results

Playlists = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',]



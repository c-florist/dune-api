import json

HOUSES = [
    (
        1,
        "House Atreides",
        json.dumps(["Caladan", "Arrakis"]),
        "House Major",
        json.dumps(["Red", "Green"]),
        "Red Hawk",
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
    (
        2,
        "House Harkonnen",
        json.dumps(["Giedi Prime"]),
        "House Major",
        json.dumps(["Blue", "Orange"]),
        "Griffin",
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
]

ORGANISATIONS = [
    (
        1,
        "Bene Gesserit",
        "c. 98 BG",
        None,
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
    (
        2,
        "Fremen",
        "c. 1300 BG",
        "c. 10219 AG",
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
]

CHARACTERS = [
    (
        json.dumps(["Duke"]),
        json.dumps(["The Red Duke", "Leto the Just"]),
        "Leto",
        "Atreides",
        "I",
        "10140 AG",
        "Caladan",
        "10191 AG",
        1,
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
    (
        json.dumps(["Warmaster", "Earl of Caladan"]),
        None,
        "Gurney",
        "Halleck",
        None,
        "10130s AG",
        "Unknown",
        None,
        1,
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
    (
        json.dumps(["Baron"]),
        None,
        "Vladimir",
        "Harkonnen",
        None,
        "10110 AG",
        "Giedi Prime",
        "10193 AG",
        2,
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
]

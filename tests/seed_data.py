import json

HOUSES = [
    (
        1,
        "House Atreides",
        "Caladan",
        "House Major",
        json.dumps(["Red", "Green"]),
        "Red Hawk",
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
    (
        2,
        "House Harkonnen",
        "Giedi Prime",
        "House Major",
        json.dumps(["Blue", "Orange"]),
        "Ram",
        "2024-01-16 06:15:49",
        "2024-01-16 06:15:49",
    ),
]

CHARACTERS = [
    (
        json.dumps(["Duke"]),
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

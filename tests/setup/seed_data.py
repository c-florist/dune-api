import json
from uuid import uuid4

HOUSES = [
    (
        1,
        str(uuid4()),
        "House Atreides",
        json.dumps(["Caladan", "Arrakis"]),
        "House Major",
        json.dumps(["Red", "Green"]),
        "Red Hawk"
    ),
    (
        2,
        str(uuid4()),
        "House Harkonnen",
        json.dumps(["Giedi Prime"]),
        "House Major",
        json.dumps(["Blue", "Orange"]),
        "Griffin"
    ),
]

ORGANISATIONS = [
    (
        1,
        str(uuid4()),
        "Bene Gesserit",
        "c. 98 BG",
        "Unknown",
        None
    ),
    (
        2,
        str(uuid4()),
        "Fremen",
        "c. 1300 BG",
        "c. 10219 AG",
        None
    ),
    (
        3,
        str(uuid4()),
        "Fedaykin",
        "Unknown",
        "10210 AG",
        "Originally a word used to describe the Fremen's guerilla fighters, later used in reference to Muad'Dib's personal guard, otherwise known as his death commandos."
    ),
]

CHARACTERS = [
    (
        1,
        str(uuid4()),
        json.dumps(["Duke"]),
        json.dumps(["The Red Duke", "Leto the Just"]),
        "Leto",
        "Atreides",
        "I",
        "10140 AG",
        "Caladan",
        "10191 AG",
        json.dumps(["Ruler", "Soldier"]),
        None,
        1
    ),
    (
        2,
        str(uuid4()),
        json.dumps(["Warmaster", "Earl of Caladan"]),
        None,
        "Gurney",
        "Halleck",
        None,
        "10130s AG",
        "Unknown",
        "Unknown",
        json.dumps(["Soldier"]),
        None,
        1
    ),
    (
        3,
        str(uuid4()),
        json.dumps(["Baron"]),
        None,
        "Vladimir",
        "Harkonnen",
        None,
        "10110 AG",
        "Giedi Prime",
        "10193 AG",
        json.dumps(["Ruler"]),
        None,
        2
    ),
    (
        4,
        str(uuid4()),
        json.dumps(["Duke", "Padishah Emperor", "Kwisatz Haderach", "Mahdi", "Lisan al Gaib"]),
        json.dumps(["MuadDib", "Usul", "The Preacher", "The Mentat Emperor"]),
        "Paul",
        "Atreides",
        None,
        "10176 AG",
        "Caladan",
        "10219 AG",
        json.dumps(["Ruler", "Soldier"]),
        None,
        1
    ),
    (
        5,
        str(uuid4()),
        json.dumps(["Captain"]),
        json.dumps(["The Leaper"]),
        "Chatt",
        None,
        None,
        "Unknown",
        "Unknown",
        "Unknown",
        json.dumps(["Fighter"]),
        "Leader of the Fedaykin.",
        None
    ),
]

CHARACTER_ORGS = [
    (4, 2),
    (5, 2),
    (5, 3),
]

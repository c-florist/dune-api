import json
from uuid import uuid4

HOUSES = [
    (
        1,
        "e6cef093-fad8-4448-8bbf-86bad9fc8d85",
        "House Atreides",
        json.dumps(["Caladan", "Arrakis"]),
        "House Major",
        json.dumps(["Red", "Green"]),
        "Red Hawk"
    ),
    (
        2,
        "a86de371-376d-47a7-8ad6-717c5f8e15c9",
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
        "ebe3fc90-e48e-43b4-b563-04dd3a54f526",
        "Bene Gesserit",
        "c. 98 BG",
        "Unknown",
        None
    ),
    (
        2,
        "71ba9ffa-8f2d-49f7-be74-82ec4a7f1f2b",
        "Fremen",
        "c. 1300 BG",
        "c. 10219 AG",
        None
    ),
    (
        3,
        "c70968f9-4110-4cf2-9033-de3d88dd6fe3",
        "Fedaykin",
        "Unknown",
        "10210 AG",
        "Originally a word used to describe the Fremen's guerilla fighters, later used in reference to Muad'Dib's personal guard, otherwise known as his death commandos."
    ),
]

CHARACTERS = [
    (
        1,
        "a370cbcd-d6e8-46bd-8a9f-bfd2fe5a8eef",
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
        "97e6f15c-c72b-4742-87c5-28e656450902",
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
        "14aee0b2-2517-4d6d-a4fb-b09008d67141",
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
        "540b8c10-8297-4710-833e-84ef51797ac0",
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
        "5c2ac4fa-f560-4840-9783-7188b071b85f",
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

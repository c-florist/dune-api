from app.v1.query import get_characters


def test_get_characters(db_connection):
    characters = get_characters(db_connection)

    assert characters == [
        {
            'titles': ['Duke'],
            'first_name': 'Leto',
            'last_name': 'Atreides',
            'suffix': 'I',
            'dob': '10140 AG',
            'birthplace': 'Caladan',
            'dod': '10191 AG',
            'organisation': 'House Atreides',
            'created_at': '2024-01-15T23:49:38.956496',
            'updated_at': '2024-01-15T23:49:38.956496'
        },
        {
            'titles': ['Warmaster', 'Earl of Caladan'],
            'first_name': 'Gurney',
            'last_name': 'Halleck',
            'suffix': None,
            'dob': '10130s AG',
            'birthplace': 'Unknown',
            'dod': None,
            'organisation': 'House Atreides',
            'created_at': '2024-01-16T00:00:38.889460',
            'updated_at': '2024-01-16T00:00:38.889460'
        }
    ]

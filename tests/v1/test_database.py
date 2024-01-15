def test_db_connection_success(db_connection):
    with db_connection as conn:
        result = conn.execute('SELECT "Bananas" AS test')
        row = result.fetchone()

    assert row[0] == "Bananas"

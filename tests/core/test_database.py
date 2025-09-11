def test_db_client_connection_success(db_client):
    with db_client.conn as conn:
        cursor = conn.cursor()
        assert cursor.connection == conn

        result = cursor.execute('SELECT "Bananas" as test')
        row = result.fetchone()

    assert row["test"] == "Bananas"

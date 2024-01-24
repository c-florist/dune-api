from sqlite3 import Connection
from contextlib import closing


def read_characters(
    db_conn: Connection, house: str | None = None, skip: int = 0, limit: int | None = 20
) -> list[dict[str, str | None]]:
    if house is not None:
        params = (house.capitalize(), limit, skip)
        where_clause = "WHERE house.name = 'House ' || ?"
    else:
        params = (limit, skip)
        where_clause = ""

    base_query = """
        SELECT 
            titles,
            first_name,
            last_name,
            suffix,
            dob,
            birthplace,
            dod,
            organisation.name as organisation,
            house.name as house,
            character.created_at,
            character.updated_at
        FROM character
        LEFT JOIN organisation
            ON character.org_id = organisation.id
        LEFT JOIN house
            ON character.house_id = house.id
    """
    limit_offset_clause = "LIMIT ? OFFSET ?"

    q = base_query + where_clause + limit_offset_clause

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results

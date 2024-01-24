from sqlite3 import Connection
from contextlib import closing


def read_characters(
    db_conn: Connection, skip: int = 0, limit: int | None = 20
) -> list[dict[str, str | None]]:
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(
            """
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
            LIMIT ?
            OFFSET ?
        """,
            (limit, skip),
        )

        results = cursor.fetchall()

    return results


def read_characters_by_house(
    db_conn: Connection, house: str, skip: int = 0, limit: int | None = 20
) -> list[dict[str, str | None]]:
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(
            """
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
            WHERE house.name = ?
            LIMIT ?
            OFFSET ?
        """,
            (house, limit, skip),
        )

        results = cursor.fetchall()

    return results

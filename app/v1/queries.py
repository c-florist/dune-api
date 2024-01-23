from sqlite3 import Connection
from contextlib import closing

from app.v1.response_models import Character


def get_characters(
    db_conn: Connection, skip: int = 0, limit: int | None = 20
) -> list[Character]:
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

        return [
            Character(**x) for x in cursor.fetchall()
        ]

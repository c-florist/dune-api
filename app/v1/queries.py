from sqlite3 import Connection
from contextlib import closing
from typing import Any


def read_characters(
    db_conn: Connection, house: str | None = None, limit: int = 20, offset: int = 0
) -> list[dict[str, str | None]]:
    params: tuple[Any, ...] = (limit, offset)

    if house is not None:
        params = (house.capitalize(),) + params
        where_clause = "WHERE house.name = 'House ' || ?"
    else:
        where_clause = ""

    base_query = """
        SELECT 
            titles,
            aliases,
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
    order_limit_clause = "ORDER BY character.id LIMIT ? OFFSET ?"

    q = base_query + where_clause + order_limit_clause

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results


def read_random_character(db_conn: Connection) -> dict[str, str | None]:
    q = """
        WITH random_character AS (
            SELECT *
            FROM character
            ORDER BY RANDOM()
            LIMIT 1
        )
        SELECT
            titles,
            aliases,
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
        FROM random_character AS character
        LEFT JOIN organisation
            ON character.org_id = organisation.id
        LEFT JOIN house
            ON character.house_id = house.id
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q)
        result: dict[str, str | None] = cursor.fetchone()

    return result


def read_houses(
    db_conn: Connection,
    status: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> list[dict[str, str]]:
    params: tuple[Any, ...] = (limit, offset)

    if status is not None:
        params = (status.capitalize(),) + params
        where_clause = "WHERE house.status = 'House ' || ?"
    else:
        where_clause = ""

    base_query = """
        SELECT 
            name,
            homeworld,
            status,
            colours,
            symbol,
            created_at,
            updated_at
        FROM house
    """
    order_limit_clause = "ORDER BY id LIMIT ? OFFSET ?"

    q = base_query + where_clause + order_limit_clause

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results


def read_organisations(
    db_conn: Connection, limit: int = 20, offset: int = 0
) -> list[dict[str, str]]:
    params = (limit, offset)
    q = """
        SELECT
            name,
            founded,
            dissolved,
            created_at,
            updated_at
        FROM organisation
        ORDER BY id
        LIMIT ? OFFSET ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results

from sqlite3 import Connection
from contextlib import closing
from typing import Any


def read_characters(
    db_conn: Connection, house: str | None = None, skip: int = 0, limit: int = 20
) -> list[dict[str, str | None]]:
    params: tuple[Any, ...] = (limit, skip)

    if house is not None:
        params = (house.capitalize(),) + params
        where_clause = "WHERE house.name = 'House ' || ?"
    else:
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


def read_houses(
    db_conn: Connection,
    status: str | None = None,
    skip: int = 0,
    limit: int = 20,
) -> list[dict[str, str]]:
    params: tuple[Any, ...] = (limit, skip)

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
    limit_offset_clause = "LIMIT ? OFFSET ?"

    q = base_query + where_clause + limit_offset_clause

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results


def read_organisations(
    db_conn: Connection,
    skip: int = 0,
    limit: int = 20
) -> list[dict[str, str]]:
    params = (limit, skip)
    q = """
        SELECT
            name,
            founded,
            dissolved
        FROM organisation
        LIMIT ? OFFSET ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results

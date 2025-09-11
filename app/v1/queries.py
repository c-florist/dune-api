from contextlib import closing
from sqlite3 import Connection
from typing import Any


def read_character(db_conn: Connection, character_uuid: str) -> dict[str, str | None]:
    q = """
        SELECT
            uuid,
            titles,
            aliases,
            first_name,
            last_name,
            suffix,
            dob,
            birthplace,
            dod,
            profession,
            misc,
            organisations,
            house
        FROM character_with_org
        WHERE uuid = ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (character_uuid,))
        result: dict[str, str | None] = cursor.fetchone()

    return result


def read_characters(
    db_conn: Connection, house: str | None = None, limit: int = 20, offset: int = 0
) -> list[dict[str, str | None]]:
    params: tuple[Any, ...] = (limit, offset)

    if house is not None:
        params = (house.capitalize(),) + params
        where_clause = "WHERE house = 'House ' || ?"
    else:
        where_clause = ""

    base_query = """
        SELECT
            uuid,
            titles,
            aliases,
            first_name,
            last_name,
            suffix,
            dob,
            birthplace,
            dod,
            profession,
            misc,
            organisations,
            house
        FROM character_with_org
    """
    order_limit_clause = "ORDER BY 1 LIMIT ? OFFSET ?"

    q = base_query + where_clause + order_limit_clause

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results


def read_random_character(db_conn: Connection) -> dict[str, str | None]:
    q = """
        SELECT
            uuid,
            titles,
            aliases,
            first_name,
            last_name,
            suffix,
            dob,
            birthplace,
            dod,
            profession,
            misc,
            organisations,
            house
        FROM character_with_org
        ORDER BY RANDOM()
        LIMIT 1
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
            uuid,
            name,
            homeworld,
            status,
            colours,
            symbol
        FROM house
    """
    order_limit_clause = "ORDER BY id LIMIT ? OFFSET ?"

    q = base_query + where_clause + order_limit_clause

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results


def read_organisations(db_conn: Connection, limit: int = 20, offset: int = 0) -> list[dict[str, str]]:
    params = (limit, offset)
    q = """
        SELECT
            uuid,
            name,
            founded,
            dissolved,
            misc
        FROM organisation
        ORDER BY id
        LIMIT ? OFFSET ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results


def read_planet(db_conn: Connection, planet_uuid: str) -> dict[str, str | None]:
    q = """
        SELECT
            uuid,
            name,
            environment,
            ruler
        FROM planet
        WHERE uuid = ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (planet_uuid,))
        result: dict[str, str | None] = cursor.fetchone()

    return result


def read_planets(db_conn: Connection, limit: int = 20, offset: int = 0) -> list[dict[str, str]]:
    params = (limit, offset)
    q = """
        SELECT
            uuid,
            name,
            environment,
            ruler
        FROM planet
        ORDER BY id
        LIMIT ? OFFSET ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        results = cursor.fetchall()

    return results


def read_planets_by_environment(db_conn: Connection, environment: str) -> list[dict[str, str | None]]:
    q = """
        SELECT
            uuid,
            name,
            environment,
            ruler
        FROM planet
        WHERE environment = ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (environment,))
        results = cursor.fetchall()

    return results

from contextlib import closing
from sqlite3 import Connection
from typing import Any


def read_character(db_conn: Connection, character_uuid: str) -> dict[str, Any]:
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
        result = cursor.fetchone()

    return result


def read_characters(
    db_conn: Connection, house: str | None = None, limit: int = 20, offset: int = 0
) -> tuple[list[dict[str, Any]], int]:
    params: tuple[Any, ...] = ()
    count_params: tuple[Any, ...] = ()

    if house is not None:
        where_clause = "WHERE house = 'House ' || ?"
        params = (house.capitalize(), limit, offset)
        count_params = (house.capitalize(),)
    else:
        where_clause = ""
        params = (limit, offset)

    count_query = "SELECT COUNT(*) as total FROM character_with_org " + where_clause
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(count_query, count_params)
        total = cursor.fetchone()["total"]

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

    return results, total


def read_random_character(db_conn: Connection) -> dict[str, Any]:
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
        result = cursor.fetchone()

    return result


def search_characters(
    db_conn: Connection, search_term: str, limit: int = 20, offset: int = 0
) -> tuple[list[dict[str, Any]], int]:
    count_q = """
        SELECT COUNT(*) as total
        FROM character
        INNER JOIN character_fts fts
            ON character.id = fts.rowid
        WHERE fts.character_fts MATCH ?
    """
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(count_q, (search_term,))
        total = cursor.fetchone()["total"]

    q = """
        SELECT
            character.uuid,
            character.titles,
            character.aliases,
            character.first_name,
            character.last_name,
            character.suffix,
            character.dob,
            character.birthplace,
            character.dod,
            character.profession,
            character.misc,
            (
                SELECT
                    json_group_array(organisation.name)
                FROM organisation
                INNER JOIN character_organisation
                    ON organisation.id = character_organisation.org_id
                WHERE character_organisation.character_id = character.id
            ) AS organisations,
            house.name as house
        FROM character
        LEFT JOIN house
            ON character.house_id = house.id
        INNER JOIN character_fts fts
            ON character.id = fts.rowid
        WHERE fts.character_fts MATCH ?
        ORDER BY fts.rank
        LIMIT ? OFFSET ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (search_term, limit, offset))
        results = cursor.fetchall()

    return results, total


def read_houses(
    db_conn: Connection,
    status: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> tuple[list[dict[str, Any]], int]:
    params: tuple[Any, ...] = ()
    count_params: tuple[Any, ...] = ()

    if status is not None:
        where_clause = "WHERE house.status = 'House ' || ?"
        params = (status.capitalize(), limit, offset)
        count_params = (status.capitalize(),)
    else:
        where_clause = ""
        params = (limit, offset)

    count_query = "SELECT COUNT(*) as total FROM house " + where_clause
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(count_query, count_params)
        total = cursor.fetchone()["total"]

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

    return results, total


def search_houses(
    db_conn: Connection, search_term: str, limit: int = 20, offset: int = 0
) -> tuple[list[dict[str, Any]], int]:
    count_q = """
        SELECT COUNT(*) as total
        FROM house
        INNER JOIN house_fts fts
            ON house.id = fts.rowid
        WHERE fts.house_fts MATCH ?
    """
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(count_q, (search_term,))
        total = cursor.fetchone()["total"]

    q = """
        SELECT
            house.uuid,
            house.name,
            house.homeworld,
            house.status,
            house.colours,
            house.symbol
        FROM house
        INNER JOIN house_fts fts
            ON house.id = fts.rowid
        WHERE fts.house_fts MATCH ?
        LIMIT ? OFFSET ?
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (search_term, limit, offset))
        results = cursor.fetchall()

    return results, total


def read_organisations(db_conn: Connection, limit: int = 20, offset: int = 0) -> tuple[list[dict[str, Any]], int]:
    count_q = "SELECT COUNT(*) as total FROM organisation"
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(count_q)
        total = cursor.fetchone()["total"]

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

    return results, total


def read_planet(db_conn: Connection, planet_uuid: str) -> dict[str, Any]:
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
        result = cursor.fetchone()

    return result


def read_planets(db_conn: Connection, limit: int = 20, offset: int = 0) -> tuple[list[dict[str, Any]], int]:
    count_q = "SELECT COUNT(*) as total FROM planet"
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(count_q)
        total = cursor.fetchone()["total"]

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

    return results, total


def read_planet_by_environment(db_conn: Connection, environment: str) -> dict[str, Any]:
    q = """
        SELECT
            uuid,
            name,
            environment,
            ruler
        FROM planet
        WHERE lower(environment) = ?
        LIMIT 1
    """

    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (environment.lower(),))
        result = cursor.fetchone()

    return result


def create_annotation(db_conn: Connection, annotation: dict[str, Any]) -> dict[str, Any]:
    q = """
        INSERT INTO annotations
            (uuid, user_id, target_type, target_uuid, annotation_text, is_public)
        VALUES
            (:uuid, :user_id, :target_type, :target_uuid, :annotation_text, :is_public)
    """
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, annotation)
        db_conn.commit()

    read_q = """
        SELECT
            uuid,
            user_id,
            target_type,
            target_uuid,
            annotation_text,
            is_public
        FROM annotations
        WHERE uuid = ?
    """
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(read_q, (annotation["uuid"],))
        return cursor.fetchone()


def read_annotations_for_user(db_conn: Connection, user_id: str) -> tuple[list[dict[str, Any]], int]:
    count_q = "SELECT COUNT(*) as total FROM annotations WHERE user_id = ?"
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(count_q, (user_id,))
        total = cursor.fetchone()["total"]

    q = """
        SELECT
            uuid,
            user_id,
            target_type,
            target_uuid,
            annotation_text,
            is_public
        FROM annotations
        WHERE
            user_id = ?
    """
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (user_id,))
        results = cursor.fetchall()
    return results, total


def update_annotation(db_conn: Connection, annotation_uuid: str, user_id: str, annotation: dict[str, Any]) -> bool:
    q = """
        UPDATE annotations
        SET
            annotation_text = :annotation_text,
            is_public = :is_public
        WHERE
            uuid = :uuid
            AND user_id = :user_id
    """
    params = {
        "uuid": annotation_uuid,
        "user_id": user_id,
        "annotation_text": annotation["annotation_text"],
        "is_public": annotation["is_public"],
    }
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, params)
        db_conn.commit()
        return cursor.rowcount > 0


def delete_annotation(db_conn: Connection, annotation_uuid: str, user_id: str) -> bool:
    q = """
        DELETE FROM annotations
        WHERE
            uuid = ?
            AND user_id = ?
    """
    with closing(db_conn.cursor()) as cursor:
        cursor.execute(q, (annotation_uuid, user_id))
        db_conn.commit()
        return cursor.rowcount > 0

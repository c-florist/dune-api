from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import Organisation


class OrganisationService:
    db_conn: Connection

    def __init__(self, db_conn: Connection) -> None:
        self.db_conn = db_conn

    def get_organisations(self, limit: int, offset: int) -> tuple[list[Organisation], int]:
        organisations_data, total = queries.read_organisations(self.db_conn, limit, offset)
        organisations = [Organisation(**org_data) for org_data in organisations_data]
        return organisations, total

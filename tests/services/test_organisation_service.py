
from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import Organisation
from app.services.organisation_service import OrganisationService


def test_get_organisations_returns_domain_model(monkeypatch):
    organisation_data = [
        {
            "uuid": "e6cef093-fad8-4448-8bbf-86bad9fc8d85",
            "name": "Bene Gesserit",
            "founded": "c. 12,000 BG",
            "dissolved": "Ongoing",
            "misc": None,
        }
    ]

    def mock_read_organisations(db_conn: Connection, limit: int, offset: int):
        return organisation_data

    monkeypatch.setattr(queries, "read_organisations", mock_read_organisations)

    service = OrganisationService(db_conn=None)
    result = service.get_organisations(limit=20, offset=0)

    assert isinstance(result[0], Organisation)
    assert result[0].name == "Bene Gesserit"

import pytest

from app.v1.response_models import Character, House


@pytest.mark.parametrize(
    "model, db_response",
    [
        pytest.param(Character, "character_db_response", id="character"),
        pytest.param(House, "house_db_response", id="house"),
    ],
)
def test_model_validation(request, model, db_response):
    db_response = request.getfixturevalue(db_response)

    serialised_models = [model(**x) for x in db_response]

    assert True

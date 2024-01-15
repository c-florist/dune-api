import pytest

from app.v1.response_models import Character


@pytest.fixture
def character_model():
    yield Character(
        title='Duke',
        first_name='Foo',
        last_name='Bar',
        relation='Father of Baz',
        organisation='Atreides',
        created_at='2024-01-15T12:10:07.770187',
        updated_at='2024-01-15T12:10:07.770187'
    )


@pytest.mark.parametrize(
    'model, attributes', [
        pytest.param('character_model', {'title', 'first_name', 'last_name', 'relation', 'organisation', 'created_at', 'updated_at'}, id='character')
    ]
)
def test_model_attributes_match_schema(request, model, attributes):
    model = request.getfixturevalue(model)
    assert set(model.model_dump().keys()) == attributes

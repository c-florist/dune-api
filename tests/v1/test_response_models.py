import pytest

from app.v1.response_models import Character


@pytest.fixture
def character_model():
    yield Character(
        titles=['Mr'],
        first_name='Foo',
        last_name='Bar',
        suffix=None,
        dob='10000 AD',
        birthplace='Planet of the Apes',
        dod=None,
        house='Monkeys',
        organisation=None,
        created_at='2024-01-15T12:10:07.770187',
        updated_at='2024-01-15T12:10:07.770187'
    )


@pytest.mark.parametrize(
    'model, attributes', [
        pytest.param('character_model', {'titles', 'first_name', 'last_name', 'suffix', 'dob', 'birthplace', 'dod', 'house', 'organisation', 'created_at', 'updated_at'}, id='character'),
    ]
)
def test_model_attributes_match_schema(request, model, attributes):
    model = request.getfixturevalue(model)
    assert set(model.model_dump().keys()) == attributes

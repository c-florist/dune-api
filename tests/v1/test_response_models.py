import pytest

from app.v1.response_models import Character, Organisation


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
        organisation='Monkeys',
        created_at='2024-01-15T12:10:07.770187',
        updated_at='2024-01-15T12:10:07.770187'
    )


@pytest.fixture
def organisation_model():
    yield Organisation(
        name='Order of Foo',
        year_founded='110000 AG',
        created_at='2024-01-15T12:27:53.898594',
        updated_at='2024-01-15T12:27:53.898594'
    )


@pytest.mark.parametrize(
    'model, attributes', [
        pytest.param('character_model', {'titles', 'first_name', 'last_name', 'suffix', 'dob', 'birthplace', 'dod', 'organisation', 'created_at', 'updated_at'}, id='character'),
        pytest.param('organisation_model', {'name', 'year_founded', 'created_at', 'updated_at'}, id='organisation')
    ]
)
def test_model_attributes_match_schema(request, model, attributes):
    model = request.getfixturevalue(model)
    assert set(model.model_dump().keys()) == attributes

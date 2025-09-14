import pytest
from app.services.annotation_service import AnnotationService
from app.v1.request_models import AnnotationCreate, AnnotationUpdate
from tests.setup.teardown import teardown_annotations


@pytest.fixture(autouse=True)
def run_around_tests(db_client):
    yield
    teardown_annotations(db_client.conn)


def test_create_annotation(db_client):
    annotation_service = AnnotationService(db_client.conn)
    annotation_data = AnnotationCreate(
        user_id="test_user",
        annotation_text="This is a test annotation.",
        is_public=True,
    )
    annotation = annotation_service.create_annotation(
        "character", "540b8c10-8297-4710-833e-84ef51797ac0", annotation_data
    )
    assert annotation.user_id == "test_user"
    assert annotation.annotation_text == "This is a test annotation."
    assert annotation.is_public is True


def test_get_annotations_for_user(db_client):
    annotation_service = AnnotationService(db_client.conn)
    annotation_data = AnnotationCreate(
        user_id="test_user",
        annotation_text="This is a test annotation.",
        is_public=True,
    )
    annotation_service.create_annotation("character", "540b8c10-8297-4710-833e-84ef51797ac0", annotation_data)

    annotations = annotation_service.get_annotations_for_user("test_user")
    assert len(annotations) == 1
    assert annotations[0].user_id == "test_user"
    assert annotations[0].annotation_text == "This is a test annotation."


def test_update_annotation_success(db_client):
    annotation_service = AnnotationService(db_client.conn)
    annotation_data = AnnotationCreate(
        user_id="test_user",
        annotation_text="This is a test annotation.",
        is_public=True,
    )
    annotation = annotation_service.create_annotation(
        "character", "540b8c10-8297-4710-833e-84ef51797ac0", annotation_data
    )

    update_data = AnnotationUpdate(
        text="This is an updated annotation.",
        is_public=False,
    )
    result = annotation_service.update_annotation(annotation.uuid, "test_user", update_data)
    assert result is True


def test_update_annotation_wrong_user(db_client):
    annotation_service = AnnotationService(db_client.conn)
    annotation_data = AnnotationCreate(
        user_id="test_user",
        annotation_text="This is a test annotation.",
        is_public=True,
    )
    annotation = annotation_service.create_annotation(
        "character", "540b8c10-8297-4710-833e-84ef51797ac0", annotation_data
    )

    update_data = AnnotationUpdate(
        text="This is an updated annotation.",
        is_public=False,
    )
    result = annotation_service.update_annotation(annotation.uuid, "wrong_user", update_data)
    assert result is False

from app.services.annotation_service import AnnotationService
from app.v1.request_models import AnnotationCreate


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

import uuid
from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import Annotation
from app.v1.request_models import AnnotationCreate, AnnotationUpdate


class AnnotationService:
    db_conn: Connection

    def __init__(self, db_conn: Connection) -> None:
        self.db_conn = db_conn

    def create_annotation(self, target_type: str, target_uuid: str, annotation_data: AnnotationCreate) -> Annotation:
        annotation_uuid = str(uuid.uuid4())
        created_annotation = queries.create_annotation(
            self.db_conn,
            {
                "uuid": annotation_uuid,
                "user_id": annotation_data.user_id,
                "target_type": target_type,
                "target_uuid": target_uuid,
                "annotation_text": annotation_data.annotation_text,
                "is_public": annotation_data.is_public,
            },
        )
        return Annotation(**created_annotation)

    def get_public_annotations_for_target(self, target_type: str, target_uuid: str) -> list[Annotation]:
        raise NotImplementedError

    def get_annotations_for_user(self, user_id: str) -> list[Annotation]:
        annotations_data = queries.read_annotations_for_user(self.db_conn, user_id)
        return [Annotation(**annotation_data) for annotation_data in annotations_data]

    def update_annotation(self, annotation_uuid: str, user_id: str, update_data: AnnotationUpdate) -> Annotation | None:
        raise NotImplementedError

    def delete_annotation(self, annotation_uuid: str, user_id: str) -> bool:
        raise NotImplementedError

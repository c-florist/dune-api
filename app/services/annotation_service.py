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

    def get_annotations_for_user(self, user_id: str) -> tuple[list[Annotation], int]:
        annotations_data, total = queries.read_annotations_for_user(self.db_conn, user_id)
        annotations = [Annotation(**annotation_data) for annotation_data in annotations_data]
        return annotations, total

    def update_annotation(self, annotation_uuid: str, user_id: str, update_data: AnnotationUpdate) -> bool:
        return queries.update_annotation(
            self.db_conn,
            str(annotation_uuid),
            user_id,
            {
                "annotation_text": update_data.text,
                "is_public": update_data.is_public,
            },
        )

    def delete_annotation(self, annotation_uuid: str, user_id: str) -> bool:
        return queries.delete_annotation(self.db_conn, str(annotation_uuid), user_id)

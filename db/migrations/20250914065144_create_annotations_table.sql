-- migrate:up
CREATE TABLE IF NOT EXISTS annotations (
    id INTEGER PRIMARY KEY,
    uuid TEXT NOT NULL,
    user_id TEXT NOT NULL,
    target_type TEXT NOT NULL,
    target_uuid TEXT NOT NULL,
    TEXT TEXT NOT NULL,
    is_public BOOLEAN NOT NULL DEFAULT FALSE,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX annotations_uuid_unique_idx ON annotations(uuid);

CREATE TRIGGER annotations_updated_at AFTER UPDATE ON annotations
BEGIN
    UPDATE annotations
    SET
        updated_at = CURRENT_TIMESTAMP
    WHERE
        id = NEW.id;
END;

-- migrate:down
DROP TABLE IF EXISTS annotations;

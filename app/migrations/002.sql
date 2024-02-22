PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS organisation (
    id INTEGER NOT NULL PRIMARY KEY,
    uuid TEXT NOT NULL,
    name TEXT NOT NULL,
    founded TEXT NOT NULL,
    dissolved TEXT NOT NULL,
    misc TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX organisation_uuid_unique_idx ON organisation(uuid);

CREATE TRIGGER IF NOT EXISTS organisation_updated_at
AFTER UPDATE ON organisation
BEGIN
    UPDATE organisation
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

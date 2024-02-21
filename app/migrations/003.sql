PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS character (
    id INTEGER NOT NULL PRIMARY KEY,
    uuid TEXT NOT NULL,
    titles TEXT,
    aliases TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    suffix TEXT,
    dob TEXT NOT NULL,
    birthplace TEXT NOT NULL,
    dod TEXT,
    house_id INTEGER,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (house_id) REFERENCES house(id) ON DELETE SET NULL
);

CREATE UNIQUE INDEX character_uuid_unique_idx ON character(uuid);

CREATE TRIGGER IF NOT EXISTS character_updated_at
AFTER UPDATE ON character
BEGIN
    UPDATE character
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

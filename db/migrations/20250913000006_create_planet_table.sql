-- migrate:up
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS planet (
    id INTEGER NOT NULL PRIMARY KEY,
    uuid TEXT NOT NULL,
    name TEXT NOT NULL,
    environment TEXT NOT NULL,
    ruler TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX planet_uuid_unique_idx ON planet(uuid);

CREATE TRIGGER IF NOT EXISTS planet_updated_at
AFTER UPDATE ON planet
BEGIN
    UPDATE planet
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

-- migrate:down
DROP TABLE IF EXISTS planet;

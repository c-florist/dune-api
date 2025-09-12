-- migrate:up
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS house (
    id INTEGER NOT NULL PRIMARY KEY,
    uuid TEXT NOT NULL,
    name TEXT NOT NULL,
    homeworld TEXT NOT NULL,
    status TEXT NOT NULL,
    colours TEXT NOT NULL,
    symbol TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX house_uuid_unique_idx ON house(uuid);

CREATE TRIGGER IF NOT EXISTS house_updated_at
AFTER UPDATE ON house
BEGIN
    UPDATE house
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

-- migrate:down
DROP TABLE IF EXISTS house;

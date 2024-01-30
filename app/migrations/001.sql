BEGIN;

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS character (
    id INTEGER NOT NULL PRIMARY KEY,
    titles TEXT,
    aliases TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    suffix TEXT,
    dob TEXT NOT NULL,
    birthplace TEXT NOT NULL,
    dod TEXT,
    org_id INTEGER,
    house_id INTEGER,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (org_id) REFERENCES organisation(id) ON DELETE SET NULL,
    FOREIGN KEY (house_id) REFERENCES house(id) ON DELETE SET NULL
);

CREATE TRIGGER IF NOT EXISTS character_updated_at
AFTER UPDATE ON character
BEGIN
    UPDATE character
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

CREATE TABLE IF NOT EXISTS organisation (
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    founded TEXT NOT NULL,
    dissolved TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS organisation_updated_at
AFTER UPDATE ON organisation
BEGIN
    UPDATE organisation
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

CREATE TABLE IF NOT EXISTS house (
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    homeworld TEXT NOT NULL,
    status TEXT NOT NULL,
    colours TEXT NOT NULL,
    symbol TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS house_updated_at
AFTER UPDATE ON house
BEGIN
    UPDATE house
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

COMMIT;

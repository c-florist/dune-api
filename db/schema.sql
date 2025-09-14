CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE house (
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
CREATE TRIGGER house_updated_at
AFTER UPDATE ON house
BEGIN
    UPDATE house
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;
CREATE TABLE organisation (
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
CREATE TRIGGER organisation_updated_at
AFTER UPDATE ON organisation
BEGIN
    UPDATE organisation
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;
CREATE TABLE character (
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
    profession TEXT,
    misc TEXT,
    house_id INTEGER,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (house_id) REFERENCES house(id) ON DELETE SET NULL
);
CREATE UNIQUE INDEX character_uuid_unique_idx ON character(uuid);
CREATE TRIGGER character_updated_at
AFTER UPDATE ON character
BEGIN
    UPDATE character
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;
CREATE TABLE character_organisation (
    character_id INTEGER NOT NULL,
    org_id INTEGER NOT NULL,
    PRIMARY KEY (character_id, org_id),
    FOREIGN KEY (character_id) REFERENCES character(id) ON DELETE CASCADE,
    FOREIGN KEY (org_id) REFERENCES organisation(id) ON DELETE CASCADE
);
CREATE VIEW character_with_org AS
    SELECT
        character.uuid,
        character.titles,
        character.aliases,
        character.first_name,
        character.last_name,
        character.suffix,
        character.dob,
        character.birthplace,
        character.dod,
        character.profession,
        character.misc,
        (
            SELECT
                json_group_array(organisation.name)
            FROM organisation
            INNER JOIN character_organisation char_org
                ON organisation.id = char_org.org_id
            WHERE char_org.character_id = character.id
        ) AS organisations,
        house.name as house,
        character.created_at,
        character.updated_at
    FROM character
    LEFT JOIN house
        ON character.house_id = house.id
/* character_with_org(uuid,titles,aliases,first_name,last_name,suffix,dob,birthplace,dod,profession,misc,organisations,house,created_at,updated_at) */;
CREATE TABLE planet (
    id INTEGER NOT NULL PRIMARY KEY,
    uuid TEXT NOT NULL,
    name TEXT NOT NULL,
    environment TEXT NOT NULL,
    ruler TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE UNIQUE INDEX planet_uuid_unique_idx ON planet(uuid);
CREATE TRIGGER planet_updated_at
AFTER UPDATE ON planet
BEGIN
    UPDATE planet
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;
CREATE VIRTUAL TABLE character_fts USING fts5(
    first_name,
    last_name,
    aliases,
    titles,
    profession,
    misc,
    content='character',
    content_rowid='id'
)
/* character_fts(first_name,last_name,aliases,titles,profession,misc) */;
CREATE TABLE IF NOT EXISTS 'character_fts_data'(id INTEGER PRIMARY KEY, block BLOB);
CREATE TABLE IF NOT EXISTS 'character_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS 'character_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);
CREATE TABLE IF NOT EXISTS 'character_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;
CREATE TRIGGER character_ai AFTER INSERT ON character BEGIN
    INSERT INTO character_fts(rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES (new.id, new.first_name, new.last_name, new.aliases, new.titles, new.profession, new.misc);
END;
CREATE TRIGGER character_ad AFTER DELETE ON character BEGIN
    INSERT INTO character_fts(character_fts, rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES ('delete', old.id, old.first_name, old.last_name, old.aliases, old.titles, old.profession, old.misc);
END;
CREATE TRIGGER character_au AFTER UPDATE ON character BEGIN
    INSERT INTO character_fts(character_fts, rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES ('delete', old.id, old.first_name, old.last_name, old.aliases, old.titles, old.profession, old.misc);
    INSERT INTO character_fts(rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES (new.id, new.first_name, new.last_name, new.aliases, new.titles, new.profession, new.misc);
END;
CREATE VIRTUAL TABLE house_fts USING fts5(
    name,
    homeworld,
    status,
    colours,
    symbol,
    content='house',
    content_rowid='id'
)
/* house_fts(name,homeworld,status,colours,symbol) */;
CREATE TABLE IF NOT EXISTS 'house_fts_data'(id INTEGER PRIMARY KEY, block BLOB);
CREATE TABLE IF NOT EXISTS 'house_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS 'house_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);
CREATE TABLE IF NOT EXISTS 'house_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;
CREATE TRIGGER house_ai AFTER INSERT ON house BEGIN
    INSERT INTO house_fts(rowid, name, homeworld, status, colours, symbol)
    VALUES (new.id, new.name, new.homeworld, new.status, new.colours, new.symbol);
END;
CREATE TRIGGER house_ad AFTER DELETE ON house BEGIN
    INSERT INTO house_fts(house_fts, rowid, name, homeworld, status, colours, symbol)
    VALUES ('delete', old.id, old.name, old.homeworld, old.status, old.colours, old.symbol);
END;
CREATE TRIGGER house_au AFTER UPDATE ON house BEGIN
    INSERT INTO house_fts(house_fts, rowid, name, homeworld, status, colours, symbol)
    VALUES ('delete', old.id, old.name, old.homeworld, old.status, old.colours, old.symbol);
    INSERT INTO house_fts(rowid, name, homeworld, status, colours, symbol)
    VALUES (new.id, new.name, new.homeworld, new.status, new.colours, new.symbol);
END;
CREATE TABLE annotations (
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
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20250913000001'),
  ('20250913000002'),
  ('20250913000003'),
  ('20250913000004'),
  ('20250913000005'),
  ('20250913000006'),
  ('20250913000007'),
  ('20250914065144');

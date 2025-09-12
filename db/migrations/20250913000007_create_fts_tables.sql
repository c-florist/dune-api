-- migrate:up
PRAGMA foreign_keys = ON;

CREATE VIRTUAL TABLE IF NOT EXISTS character_fts USING fts5(
    first_name,
    last_name,
    aliases,
    titles,
    profession,
    misc,
    content='character',
    content_rowid='id'
);

CREATE TRIGGER IF NOT EXISTS character_ai AFTER INSERT ON character BEGIN
    INSERT INTO character_fts(rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES (new.id, new.first_name, new.last_name, new.aliases, new.titles, new.profession, new.misc);
END;

CREATE TRIGGER IF NOT EXISTS character_ad AFTER DELETE ON character BEGIN
    INSERT INTO character_fts(character_fts, rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES ('delete', old.id, old.first_name, old.last_name, old.aliases, old.titles, old.profession, old.misc);
END;

CREATE TRIGGER IF NOT EXISTS character_au AFTER UPDATE ON character BEGIN
    INSERT INTO character_fts(character_fts, rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES ('delete', old.id, old.first_name, old.last_name, old.aliases, old.titles, old.profession, old.misc);
    INSERT INTO character_fts(rowid, first_name, last_name, aliases, titles, profession, misc)
    VALUES (new.id, new.first_name, new.last_name, new.aliases, new.titles, new.profession, new.misc);
END;

CREATE VIRTUAL TABLE IF NOT EXISTS house_fts USING fts5(
    name,
    homeworld,
    status,
    colours,
    symbol,
    content='house',
    content_rowid='id'
);

CREATE TRIGGER IF NOT EXISTS house_ai AFTER INSERT ON house BEGIN
    INSERT INTO house_fts(rowid, name, homeworld, status, colours, symbol)
    VALUES (new.id, new.name, new.homeworld, new.status, new.colours, new.symbol);
END;

CREATE TRIGGER IF NOT EXISTS house_ad AFTER DELETE ON house BEGIN
    INSERT INTO house_fts(house_fts, rowid, name, homeworld, status, colours, symbol)
    VALUES ('delete', old.id, old.name, old.homeworld, old.status, old.colours, old.symbol);
END;

CREATE TRIGGER IF NOT EXISTS house_au AFTER UPDATE ON house BEGIN
    INSERT INTO house_fts(house_fts, rowid, name, homeworld, status, colours, symbol)
    VALUES ('delete', old.id, old.name, old.homeworld, old.status, old.colours, old.symbol);
    INSERT INTO house_fts(rowid, name, homeworld, status, colours, symbol)
    VALUES (new.id, new.name, new.homeworld, new.status, new.colours, new.symbol);
END;

-- migrate:down
DROP TABLE IF EXISTS house_fts;
DROP TRIGGER IF EXISTS house_au;
DROP TRIGGER IF EXISTS house_ad;
DROP TRIGGER IF EXISTS house_ai;
DROP TABLE IF EXISTS character_fts;
DROP TRIGGER IF EXISTS character_au;
DROP TRIGGER IF EXISTS character_ad;
DROP TRIGGER IF EXISTS character_ai;

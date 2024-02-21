PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS character_organisation (
    character_id INTEGER NOT NULL,
    org_id INTEGER NOT NULL,
    PRIMARY KEY (character_id, org_id),
    FOREIGN KEY (character_id) REFERENCES character(id) ON DELETE CASCADE,
    FOREIGN KEY (org_id) REFERENCES organisation(id) ON DELETE CASCADE
);

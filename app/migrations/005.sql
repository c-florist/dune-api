PRAGMA foreign_keys = ON;

CREATE VIEW IF NOT EXISTS character_with_org AS
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
;

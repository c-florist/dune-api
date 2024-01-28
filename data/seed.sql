BEGIN;

------------------------ ALL HOUSES ------------------------
------------------------------------------------------------
INSERT INTO house (id, name, homeworld, status, colours, symbol)
VALUES
    (1, 'House Atreides', 'Caladan', 'House Major', '["Red", "Green"]', 'Red hawk'),
    (2, 'House Harkonnen', 'Giedi Prime', 'House Major', '["Blue", "Orange"]', 'Griffin'),
    (3, 'House Corrino', '["Kaitain", "Salusa Secundus"]', 'House Major', '["Black", "Grey", "Bronze", "Gold"]', 'Golden lion'),
    (4, 'House Fenring', '["Kaitain", "Caladan"]', 'House Major', '["Black", "Silver", "Red"]', 'Two lions split by a chain'),
    (5, 'House Ginaz', '["Ginaz"]', 'House Major', '["White", "Khaki"]', 'Crossed swords'),
    (6, 'House Halleck', '["Caladan"]', 'House Major', '["Unknown"]', 'Unknown'),
    (7, 'House Metulli', '["Novebruns"]', 'House Major', '["Unknown"]', 'Unknown'),
    (8, 'House Moritani', '["Grumman"]', 'House Major', '["Unknown"]', 'Unknown'),
    (9, 'House Nebiro', '["Unknown"]', 'House Minor', '["Unknown"]', 'Unknown')
;

--------------------- ALL ORGANISATIONS ---------------------
-------------------------------------------------------------
INSERT INTO organisation (id, name, founded, dissolved)
VALUES
    (1, 'Bene Gesserit', 'c. 98 BG', null),
    (2, 'Fremen', 'c. 1300 BG', 'c. 10219 AG'),
    (3, 'Ixian Confederacy', '10196 AG', null),
    (4, 'Fish Speakers', 'c. 10500 AG', null),
    (5, 'Bene Tleilax', 'After 1381 BG', '15229 AG'),
    (6, 'Rakian Preisthood', 'c. 15228 AG', null),
    (7, 'Sardaukar', 'Before 10163 AG', 'After 10219 AG'),
    (8, 'Honored Matres', 'c. 15728 AG', 'After 15240 AG'),
    (9, 'Combine Honnete Ober Advancer Mercantiles (CHOAM)', 'c. 1000 AG', 'After 15212 AG'),
    (10, 'Landsraad', 'c. 2100 BG', 'After 10219 AG'),
    (11, 'Spacing Guild', 'c. 1 AG', null),
    (12, 'Suk Medical School', '88 BG', null)
;

-------------------- ATREIDES CHARACTERS --------------------
-------------------------------------------------------------
INSERT INTO character (titles, first_name, last_name, suffix, dob, birthplace, dod, org_id, house_id)
VALUES
    ('["The Old Duke"]', 'Unknown', 'Atreides', null, 'Unknown', 'Unknown', '10154 AG', null, 1),
    ('["Duke"]', 'Leto', 'Atreides', 'I', '10140 AG', 'Caladan', '10191 AG', null, 1),
    ('["Lady", "Honorable Atreides"]', 'Jessica', 'Atreides', null, '10154 AG', 'Wallach IX', '10256 AG', 1, 1),
    ('["Duke", "Padishah Emperor", "Kwisatz Haderach", "Mahdi", "Lisan al Gaib"]', 'Paul', 'Atreides', null, '10176 AG', 'Caladan', '10219 AG', 2, 1),
    ('["Regent", "Mahdinate"]', 'Alia', 'Atreides', null, '10191 AG', 'Arrakis', '10219 AG', 2, 1),
    (null, 'Leto', 'Atreides', 'II (Elder)', 'Unknown', 'Arrakis', '10193 AG', null, 1),
    ('["Padishah Emperor"]', 'Leto', 'Atreides', 'II', '10210 AG', 'Arrakis', '13728 AG', null, 1),
    ('["Empress"]', 'Ghanima', 'Atreides', null, '10210 AG', 'Arrakis', null, null, 1),
    ('["Majordomo"]', 'Moneo', 'Atreides', null, '13610 AG', 'Unknown', '13728 AG', null, 1),
    ('["Governor of Arrakis"]', 'Siona Ibn Fuad al-Seyefa', 'Atreides', null, '13600s AG', 'Arrakis', null, null, 1)
;

COMMIT;

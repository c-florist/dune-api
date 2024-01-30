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
INSERT INTO character (titles, aliases, first_name, last_name, suffix, dob, birthplace, dod, org_id, house_id)
VALUES
    ('["Duke"]', '["The Old Duke"]', 'Unknown', 'Atreides', null, 'Unknown', 'Unknown', '10154 AG', null, 1),
    ('["Duke"]', '["The Red Duke", "Leto the Just"]', 'Leto', 'Atreides', 'I', '10140 AG', 'Caladan', '10191 AG', null, 1),
    ('["Lady", "Honorable Atreides"]', null, 'Jessica', 'Atreides', null, '10154 AG', 'Wallach IX', '10256 AG', 1, 1),
    ('["Duke", "Padishah Emperor", "Kwisatz Haderach", "Mahdi", "Lisan al Gaib"]', '["Muad''Dib", "Usul", "The Preacher", "The Mentat Emperor"]', 'Paul', 'Atreides', null, '10176 AG', 'Caladan', '10219 AG', 2, 1),
    ('["Regent", "Mahdinate"]', '["St. Alia of the Knife", "Abomination", "Coan-Teen", "Hawt the Fish Monster", "Womb of Heaven"]', 'Alia', 'Atreides', null, '10191 AG', 'Arrakis', '10219 AG', 2, 1),
    (null, null, 'Leto', 'Atreides', 'II (Elder)', 'Unknown', 'Arrakis', '10193 AG', null, 1),
    ('["Padishah Emperor"]', '["God-Emperor", "Divided God", "Golden Ruler", "The Tyrant", "Guldur", "Great God Dur", "Worm", "Worm God", "Old Worm", "Prophet", "Desert Demon", "Ari", "Lion of the Atreides", "Batigh"]', 'Leto', 'Atreides', 'II', '10210 AG', 'Arrakis', '13728 AG', null, 1),
    ('["Empress"]', '["Aryeh", "Atreides Lioness"]', 'Ghanima', 'Atreides', null, '10210 AG', 'Arrakis', null, null, 1),
    ('["Majordomo"]', null, 'Moneo', 'Atreides', null, '13610 AG', 'Unknown', '13728 AG', null, 1),
    ('["Governor of Arrakis"]', null, 'Siona Ibn Fuad al-Seyefa', 'Atreides', null, '13600s AG', 'Arrakis', null, null, 1),
    ('["Warmaster", "Earl of Caladan"]', null, 'Gurney', 'Halleck', null, 'c. 10130 AG', 'Unknown', null, null, 1)
;

------------------- HARKONNEN CHARACTERS --------------------
-------------------------------------------------------------
INSERT INTO character (titles, aliases, first_name, last_name, suffix, dob, birthplace, dod, org_id, house_id)
VALUES
    (null, null, 'Abulurd', 'Harkonnen', null, 'Unknown', 'Unknown', 'Unknown', null, 2),
    (null, '["Abulurd Harkonnen II"]', 'Abulurd', 'Rabban', null, 'Unknown', 'Unknown', 'Unknown', null, 2),
    ('["Baron"]', null, 'Vladimir', 'Harkonnen', null, '10110 AG', 'Giedi Prime', '10193 AG', null, 2),
    ('["Count of Lankiveil", "Governor of Arrakis"]', '["Beast Rabban", "Mudir Nahya", "Demon Ruler", "King Cobra"]', 'Glossu', 'Rabban', null, '10132 AG', 'Lankiveil', '10193 AG', null, 2),
    ('["Baron"]', null, 'Feyd-Rautha', 'Harkonnen', null, '10174 AG', 'Lankiveil', '10193 AG', null, 2)
;

--------------------- CORRINO CHARACTERS --------------------
-------------------------------------------------------------
INSERT INTO character (titles, aliases, first_name, last_name, suffix, dob, birthplace, dod, org_id, house_id)
VALUES
    ('["Padishah Emperor"]', null, 'Shaddam', 'Corrino', 'IV', '10119 AG', 'Kaitain', '10202 AG', null, 3),
    ('["Princess"]', null, 'Irulan', 'Corrino', null, '10176 AG', 'Kaitain', null, 1, 3),
    ('["Princess"]', null, 'Wensicia', 'Corrino', null, 'Unknown', 'Unknown', null, null, 3),
    ('["Prince"]', '["Harq al-Ada"]', 'Farad''n', 'Corrino', null, 'Unknown', 'Unknown', null, null, 3)
;

--------------------- FENRING CHARACTERS --------------------
-------------------------------------------------------------
INSERT INTO character (titles, aliases, first_name, last_name, suffix, dob, birthplace, dod, org_id, house_id)
VALUES
    ('["Count"]', '["Imperial Agent on Arrakis", "Interim Governor of Arrakis", "Siridar-Absentia of Caladan"]', null, 'Hasimir', 'Fenring', null, '10133 AG', 'Unknown', '10225 AG', null, 4),
    ('["Lady"]', null, 'Margot', 'Fenring', null, 'Unknown', 'Unknown', null, 1, 4),
    (null, null, 'Dalak', 'Fenring', null, 'Unknown', 'Unknown', 'Before 10219 AG', null, 4)
;

---------------------- NEBIRO CHARACTERS --------------------
-------------------------------------------------------------
INSERT INTO character (titles, aliases, first_name, last_name, suffix, dob, birthplace, dod, org_id, house_id)
VALUES
    (null, null, 'Essas', 'Paymon', null, 'Unknown', 'Unknown', 'After 10210 AG', null, 9)
;

COMMIT;

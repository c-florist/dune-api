begin;

--------------------- TABLES ---------------------
--------------------------------------------------
create table if not exists character (
    id integer not null primary key,
    titles text,
    first_name text not null,
    last_name text not null,
    suffix text,
    dob text not null,
    birthplace text not null,
    dod text,
    org_id int,
    house_id int,
    created_at datetime not null default current_timestamp,
    updated_at datetime not null default current_timestamp,
    foreign key (org_id) references organisation(id),
    foreign key (house_id) references house(id)
);

create trigger if not exists character_updated_at
after update on character
begin
    update character
    set updated_at = current_timestamp
    where old.id = new.id;
end;

create table if not exists organisation (
    id integer not null primary key,
    name text not null,
    founded text not null,
    dissolved text,
    created_at datetime not null default current_timestamp,
    updated_at datetime not null default current_timestamp
);

create trigger if not exists organisation_updated_at
after update on organisation
begin
    update organisation
    set updated_at = current_timestamp
    where old.id = new.id;
end;

create table if not exists house (
    id integer not null primary key,
    name text not null,
    homeworld text not null,
    status text not null,
    colours text not null,
    symbol text not null,
    created_at datetime not null default current_timestamp,
    updated_at datetime not null default current_timestamp
);

create trigger if not exists house_updated_at
after update on house
begin
    update house
    set updated_at = current_timestamp
    where old.id = new.id;
end;

commit;

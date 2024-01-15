begin;

create table character (
    id int not null primary key,
    title text,
    first_name text not null,
    last_name text not null,
    suffix text,
    relation text,
    org_id int,
    created_at datetime not null default current_timestamp,
    updated_at datetime not null default current_timestamp,
    foreign key (org_id) references organisation(id)
);

create trigger character_updated_at
after update on character
begin
    update character
    set updated_at = current_timestamp
    where old.id = new.id;
end;

create table organisation (
    id int not null primary key,
    name text not null,
    year_founded text,
    created_at datetime not null default current_timestamp,
    updated_at datetime not null default current_timestamp
);

create trigger organisation_updated_at
after update on organisation
begin
    update organisation
    set updated_at = current_timestamp
    where old.id = new.id;
end;

commit;

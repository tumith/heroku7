create database 0412012660_verk7;

create table 0412012660_verk7.users(
	user varchar(32) not null,
    pass varchar(32) not null,
    nafn varchar(32) not null,
    primary key(user)
);

insert into 0412012660_verk7.users (user, pass, nafn) values('TTJ', '123456','Tumi')
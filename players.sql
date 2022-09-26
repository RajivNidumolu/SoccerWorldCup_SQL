create table players(player_id int primary key, name varchar(40),fname varchar(40),lname varchar(35),dob varchar(20), country varchar(30),foreign key(country) references country(country_name),height int,club varchar(30), position varchar(20),caps_for_country int, is_captain char(20));


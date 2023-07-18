
--Task-1
--create  table if not exists Movies(
--	id Integer primary key,
--	name varchar (50),
--	release_year date not null
--);

--Task-2
--insert  into Movies (id,name,release_year) values (1,'pokimon','2000-10-23'),
--(2,'Black love','2005-02-20'),
--(3,'Baron','2016-09-17');


--task-3
--select * from Movies where  name = 'Baron';


--task-4

--alter table Movies add column category text,
--add column runtime time,
--add column rating integer,
--add column box_office bigint,
--add column created_at timestamp

--task-5

--Update Movies set category='comedy',runtime='10:06:20',rating=9,box_office =876,created_at ='2002-10-01 14:42:12' where name ='pokimon';
--Update  Movies set category='Dorama',runtime='21:43:12',rating=3,box_office=9573,created_at='2005-01-12  15:23:54' where name ='Black love'; 
--update Movies set category= 'Melodrama',runtime ='18:54:11',rating=7,box_office = 483947,created_at = '2001-09-08 22:11:55' where  name = 'Baron';

--delete from Movies where id =4;
--delete from movies where id = 5;

--6 task

--alter table Movies add constraint name  unique (name);

insert  into Movies (id,name,release_year,category,runtime,rating,box_office,created_at) 
values (5,'pokimon','2000-10-23','comedy','21:43:12',9,6546,'2005-01-12  15:23:54');

--select * from Movies;

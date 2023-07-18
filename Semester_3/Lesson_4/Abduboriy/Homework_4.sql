--Дз
--1. Movies DB:
--1. Создать таблицу movies с столбцами name и release_year
--2. Добавить в таблицу 3 фильма
--3. Выбрать один из фильмов
--4. Добавить в таблицу новые столбцы:
--    - runtime
--    - category
--    - rating
--    - box_office - поле для хранения прибыли от фильма. Типа bigint
--    - created_at - дата создания. используйте тип datetime
--5. Сейчас данные поля созданы пустыми в каждой строке, поэтому ваша задача добавить туда новые значения.
--6. В будущем могут быть фильмы с одинаковыми названиями, поэтому нужно добавить в столбец name Constraint Unique
--
--
--2. Написать следующий запросы на базе данных world:

--CREATE TABLE if not exists Movies_DB (	
--    name TEXT,
--    release_year date NOT NULL
-- );	


-- INSERT INTO Movies_DB (name, release_year)
-- VALUES ('The Flash', '2023-06-15');

-- INSERT INTO Movies_DB (name, release_year)
-- VALUES ('Spider-Man: Across the Spider-Verse', '2023-06-02');	

-- INSERT INTO Movies_DB (name, release_year)
-- VALUES ('Transformers: Rise of the Beasts', '2023-06-09');	


--ALTER TABLE movies_db ADD COLUMN runtime varchar(50);
--ALTER TABLE movies_db ADD COLUMN category varchar(50);
--ALTER TABLE movies_db ADD COLUMN rating varchar(50);
--ALTER TABLE movies_db ADD COLUMN box_office bigint;
--ALTER TABLE movies_db ADD COLUMN created_at date;


--UPDATE movies_db SET runtime = '02:24:15' WHERE name = 'The Flash';
--UPDATE movies_db SET category = 'Action, Adventure, Fantasy' WHERE name = 'The Flash';
--UPDATE movies_db SET rating = '7.1' WHERE name = 'The Flash';
--UPDATE movies_db SET box_office = '267200000' WHERE name = 'The Flash';
--UPDATE movies_db SET created_at = '2021-01-19' WHERE name = 'The Flash';

--UPDATE movies_db SET runtime = '02:16:00' WHERE name = 'Spider-Man: Across the Spider-Verse';
--UPDATE movies_db SET category = 'Action, Adventure, Fantasy' WHERE name = 'Spider-Man: Across the Spider-Verse';
--UPDATE movies_db SET rating = '8.9' WHERE name = 'Spider-Man: Across the Spider-Verse';
--UPDATE movies_db SET box_office = '663500000' WHERE name = 'Spider-Man: Across the Spider-Verse';
--UPDATE movies_db SET created_at = '2022-10-07' WHERE name = 'Spider-Man: Across the Spider-Verse';

--UPDATE movies_db SET runtime = '02:07:34' WHERE name = 'Transformers: Rise of the Beasts';
--UPDATE movies_db SET category = 'Action, Fantasy' WHERE name = 'Transformers: Rise of the Beasts';
--UPDATE movies_db SET rating = '6.2' WHERE name = 'Transformers: Rise of the Beasts';
--UPDATE movies_db SET box_office = '421000000' WHERE name = 'Transformers: Rise of the Beasts';
--UPDATE movies_db SET created_at = '2018-11-07' WHERE name = 'Transformers: Rise of the Beasts';


--ALTER TABLE movies_db
--ADD CONSTRAINT constraint_name UNIQUE (name);


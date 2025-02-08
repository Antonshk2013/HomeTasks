/*
 Подключиться к базе данных world (которая находится на удаленном сервере). 

Посмотреть на таблицы city, country из базы world. В каждой таблице есть поле 
название (Name) и население (Population). Поле Name в одной таблице означает 
название города, а в другой - название страны. 

Написать запрос с помощью UNION, который выводит список названий всех городов 
и стран с их населением. 
Итоговая выборка должна содержать два столбца: Name, Population. 
  */

SELECT 
c.name as Name, 
c.population as Population  
from city c 
UNION
SELECT 
cou.name, 
cou.population  
from country cou;
/*Посмотреть на таблицы в базе world 
 * и объяснить ограничения нескольких столбцов - ответить 1 предложением.*/
/*Определены ограничения для примари кей, нот нул, заданы дефолтные значения*/
/*Далее работаем на локальном сервере. 
 * Создать новую таблицу citizen, которая содержит следующие поля: 
 * уникальное автоинкрементное, 
 * номер соц страхования, 
 * имя, 
 * фамилию 
 * емейл. */
create table if not exists citizen
	(
	id integer not null auto_increment primary key,
	ssn integer,
	first_name varchar(255),
	surname_name varchar(255),
	email varchar(255)
	);
/*
 На вашем локальном сервере в любой базе 
 создать таблицу без ограничений (любую, можно взять с урока). 
 */
create table if not exists simple_table
	(
	first_name integer
	);

/*
 Добавить в таблицу 5 значений. 
 Добавить 3 человека с одинаковыми именами и 2 человека без lastname 
 */

INSERT INTO citizen
(ssn, first_name, email)
VALUES(18146, 'Anton', 'antonshk2013"gmail.com');

/*Использовать оператор alter table … modify
 *  , чтобы добавить ограничение not null на поле firstname и lastname. */

describe citizen;
ALTER TABLE citizen
MODIFY first_name VARCHAR(255) NOT NULL;

ALTER TABLE citizen
MODIFY surname_name VARCHAR(255) NOT NULL;
/*Тут получаем ошибку так как есть с значением НУЛ записи
SQL Error [1138] [22001]: Data truncation: Invalid use of NULL value*/

/*Добавить ограничение unique для пары firstname\lastname. */
ALTER TABLE citizen 
ADD CONSTRAINT unique_full_name UNIQUE (first_name, surname_name);
/*Ошибка есть неуникальные записи
 * SQL Error [1062] [23000]: Duplicate entry 'Anton-Shkarupa' for key 'citizen.unique_full_name'*/

/*Удалить таблицу из базы и пересоздать ее, 
модифицировав запрос add table так, 
чтобы он учитывал ограничения (см примеры из класса).*/
drop table citizen;
describe citizen;
TRUNCATE citizen;
SELECT * from citizen ;

SELECT 
c.first_name
,c.surname_name
,COUNT(*) 
FROM citizen c
GROUP BY first_name, surname_name 
HAVING COUNT(*) > 1;


create table if not exists citizen
	(
	id integer not null auto_increment primary key,
	ssn integer,
	first_name varchar(255) not null,
	surname_name varchar(255) not null,
	email varchar(255),
	CONSTRAINT unique_full_name UNIQUE (first_name, surname_name)
	);

/*Добавить правильные и неправильные данные (нарушающие и не нарушающие ограничения). */
/*не правильные данные*/
INSERT INTO citizen
(ssn, first_name, email)
VALUES(18146, 'Anton', 'antonshk2013"gmail.com');
/*SQL Error [1364] [HY000]: Field 'surname_name' doesn't have a default value*/

/*не правильные данные*/
INSERT INTO citizen
(ssn, surname_name, email)
VALUES(18146, 'Shkarupa', 'antonshk2013"gmail.com');
/*SQL Error [1364] [HY000]: Field 'first_name' doesn't have a default value*/

/*правильные данные*/
INSERT INTO citizen
(ssn, first_name, surname_name, email)
VALUES(18146, 'Anton','Shkarupa', 'antonshk2013"gmail.com');

/*не правильные данные*/
INSERT INTO citizen
(ssn, first_name, surname_name, email)
VALUES(18147, 'Anton','Shkarupa', 'antonshk2014"gmail.com');
/*SQL Error [1062] [23000]: Duplicate entry 'Anton-Shkarupa' for key 'citizen.unique_full_name'*/


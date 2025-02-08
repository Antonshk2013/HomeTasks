/*1. Создать таблицу Students с полями:
id - целое число первичный ключ автоинкремент
name - строка 128 не null
age - целое число*/
DROP table Students;
DROP table Teachers;

create table if not exists Students
	(
	id integer not null auto_increment primary key,
	name varchar(128) not null,
	age integer
	);

/*2. Создать таблицу Teachers с полями:
 id - целое число первичный ключ автоинкремент
 name - строка 128 не null
 age - целое число*/

create table if not exists Teachers
	(
	id integer not null auto_increment primary key,
	name varchar(128) not null,
	age integer
	);
/*3. Создать таблицу Competencies с полями:
id - целое число первичный ключ автоинкремент
 title - строка 128 не null*/

create table if not exists Competencies
	(
	id integer not null auto_increment primary key,
	title varchar(128) not null
	);

/*4. Создать таблицу Teachers2Competencies с полями:
● id - целое число первичный ключ автоинкремент
● teacher_id - целое число
● competencies_id - целое число*/

create table if not exists Teachers2Competencies
	(
	id integer not null auto_increment primary key,
	teacher_id integer,
	competencies_id integer
	);
/*5. Создать таблицу Courses
● id - целое число первичный ключ автоинкремент
● teacher_id - целое число
● title строка - 128 не null
● headman_id - целое число*/

create table if not exists Courses
	(
	id integer not null auto_increment primary key,
	teacher_id integer,
	title varchar(128)
	headman_id integer
	);

/*6. Создать таблицу Students2Courses
● id - целое число первичный ключ автоинкремент
● student_id - целое число
●  course_id- целое число*/

create table if not exists Students2Courses
	(
	id integer not null auto_increment primary key,
	student_id integer,
	course_id integer
	);

use HR;
/*Выведите количество сотрудников в базе*/
select count(*) from employees e ;

/*Выведите количество департаментов (отделов) в базе*/

select count(*) from departments d ;

/*Подключитесь к базе данных World (которая находится на удаленном сервере).*/

use world;

/*Выведите среднее население в городах Индии (таблица City, код Индии - IND)*/
/*Выведите минимальное население в индийском городе и максимальное.*/
select
round(avg(c.Population), 0) as 'avg'
,min(c.Population) as 'min'
,max(c.Population) as 'max'
from city c
where c.CountryCode = 'IND';



/*Выведите самую большую площадь территории.*/
select max(SurfaceArea) from country c;

/*Выведите среднюю продолжительность жизни по странам.*/
SELECT round(avg(c.LifeExpectancy),0) from country c

/*Найдите самый населенный город (подсказка: использовать подзапросы)*/
/*Самый населенный город в рамках всех стран*/
SELECT c2.name from city c2 where c2.Population=(SELECT max(Population) from city c);

/*Самый населенный город в рамках каждой страны*/
SELECT
c.CountryCode
,(SELECT c3.name FROM city c3 where c3.CountryCode=c.Countrycode and c3.Population=(SELECT max(c2.Population) from city c2 where c2.CountryCode=c3.CountryCode))
FROM city c
group by c.CountryCode

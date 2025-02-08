
/*Подключитесь к базе данных world (которая находится на удаленном сервере).*/ 

/*+*/

/*Выведите список стран с языками, на которых в них говорят. */
SELECT 
c.Name,
cl.`Language` 
FROM country c 
INNER JOIN countrylanguage cl 
on c.code = cl.CountryCode;

/*Выведите список городов с их населением и названием стран*/
SELECT 
c.Name
,c.Population 
,co.Name 
FROM city c
left Join country co
on c.CountryCode =co.Code;

/*Выведите список городов в South Africa*/
SELECT 
c.name
FROM city c
left join country co
on c.CountryCode = co.Code
where co.Name = "South Africa";

/*Выведите список стран с названиями столиц. 
 Подсказка: в таблице country есть поле Capital, 
 которое содержит номер города из таблицы City.*/ 
SELECT 
co.name,
c.Name 
FROM country co 
INNER join city c
on co.Capital = c.ID ;

/*Измените запрос 4 таким образом, чтобы выводилось население в столице.*/ 
SELECT 
co.name,
c.Population  
FROM country co 
INNER join city c
on co.Capital = c.ID ;
/*Напишите запрос, который возвращает название столицы United States*/
SELECT 
co.name,
c.Name 
FROM country co 
INNER join city c
on co.Capital = c.ID 
where co.Name = "United States";

/*Используя базу hr_data.sql, вывести имя, фамилию и город сотрудника.*/
SELECT 
e.first_name 
,e.last_name 
,l.city 
FROM employees e 
left join departments d 
on e.department_id = d.department_id 
left join locations l 
on d.location_id = l.location_id ;
/*Используя базу hr_data.sql, вывести города и соответствующие городам страны.*/
SELECT 
l.city 
,c.country_name 
FROM locations l
left join countries c 
on l.country_id  = c.country_id ;

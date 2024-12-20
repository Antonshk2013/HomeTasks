/*1. Выведите 5 самых населенных городов. Подсказка: вывести все, отсортировать по
Population в порядке убывания по населению и с помощью limit 5 оставить только 5
самых больших.*/
SELECT
Name
,Population
from city c
order by Population DESC
limit 5;

/*2. На скольки языках говорят в Индии?*/
SELECT
count(*)
from countrylanguage c
where c.CountryCode = (select Code  from country c
where c.Name ='India');

/*3. Какой язык в Индии самый популярный?*/
SELECT
*
from countrylanguage c
where c.CountryCode = (select Code  from country c
where c.Name ='India')
order by Percentage DESC
limit 1;

/*4. Какой официальный язык в Индии?*/
SELECT
*
from countrylanguage c
where c.CountryCode = (select Code  from country c
where c.Name ='India')
and IsOfficial='T';

/*5. Выведите список официальных языков всех стран с процентом их использования.
Объясните результат.*/
SELECT
`Language`
,Percentage
from countrylanguage c
WHERE IsOfficial='T';
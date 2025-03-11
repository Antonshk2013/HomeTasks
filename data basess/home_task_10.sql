/*Подключиться к базе данных world*/
use world;
/*Вывести население в каждой стране.
 Результат содержит два поля: CountryCode, sum(Population). Запрос по таблице city.*/
SELECT
c.CountryCode
,SUM(c.Population)
FROM city c
GROUP BY c.CountryCode;
/*Изменить запрос выше так,
чтобы выводились только страны с населением более 3 млн человек.
Сколько всего записей в результате?*/
SELECT
c.CountryCode
,SUM(c.Population) as CumPop
FROM city c
GROUP BY c.CountryCode
HAVING CumPop > 3000000;
/*Поменять запрос выше так, чтобы в результате вместо кода страны выводилось ее название.
 Подсказка: нужен join таблиц city и country по полю CountryCode.*/
SELECT
c2.Name
,SUM(c.Population) as CumPop
FROM city c
JOIN country c2
on c.CountryCode =c2.Code
GROUP BY c2.Name
HAVING CumPop > 3000000;
/*Вывести количество городов в каждой стране (CountryCode, amount of cities).
 Подсказка: запрос по таблице city и группировка по CountryCode.*/
SELECT
c.CountryCode
,count(c.Name)
FROM city c
GROUP BY c.CountryCode ;
/*Поменять запрос так, чтобы вместо кодов стран, было названия стран.*/
SELECT
c2.Name
,count(c.Name)
FROM city c
JOIN country c2
on c.CountryCode =c2.Code
GROUP BY c.CountryCode ;
/*Поменять запрос так, чтобы выводилось среднее количество городов в стране.
Подсказка: разделите задачу на несколько подзадач.
Например, сначала вывести код страны и количество городов в каждой стране.
Затем сделать join получившегося результата с запросом, где высчитывается
среднее от количества городов. Потом добавить join, который добавит имена стран,
вместо кода.

Разобьем запросы на части:

1. Вывести код страны и количество городов в каждой стране.

2. Получить среднее количество городов в стране.

3. Объединить результаты с именами стран.*/
SELECT
c2.Name
,count(c.Name)
,((SELECT count(*) FROM city)/(SELECT count(*) FROM country)) as avg_city
FROM city c
JOIN country c2
on c.CountryCode =c2.Code
GROUP BY c.CountryCode ;

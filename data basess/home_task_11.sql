/*Подключиться к базе данных hr*/
use hr;

/*Вывести список
 region_id,
 total_countries,
 где total_countries - количество стран в таблице.
 Подсказка: работаем с таблицей countries, использовать оконную функцию over() и
 суммировать count(country_id).*/
select
region_id ,
count(country_id) as 'total_countries'
from countries
group by region_id
order by region_id ;

select DISTINCT
c.region_id,
count(c.country_id) over() as 'total_countries'
from countries c;

/*Изменить запрос 2 таким образом, чтобы для каждого region_id выводилось
 * количество стран в этом регионе. Подсказка: добавить partition by region_id в over().*/
select DISTINCT
c.region_id,
count(c.country_id) over(PARTITION by c.region_id) as 'total_countries'
from countries c;
/*Работа с таблицей departments.
Написать запрос, который выводит location_id, department_name,
dept_total, где dept_total - количество департаментов в location_id. */
SELECT DISTINCT
d.location_id ,
count(d.department_name) over(PARTITION by d.location_id) as 'dept_total'
FROM departments d;


/*Изменить запрос 3 таким образом, чтобы выводились названия городов соответствующих
 location_id.
 */
SELECT DISTINCT
l.city ,
count(d.department_name) over(PARTITION by d.location_id) as 'dept_total'
FROM departments d
join locations l
on d.location_id = l.location_id ;
/*Работа с таблицей employees. Вывести manager_id, last_name,
total_manager_salary, где total_manager_salary - общая зарплата подчиненных
каждого менеджера (manager_id).*/

select * from employees e ;

SELECT DISTINCT
e2.last_name ,
sum(e.salary) over(PARTITION by e.manager_id) as total_manager_salary
FROM employees e
join employees e2
on e.manager_id = e2.employee_id

/*1. Написать запрос, возвращающий всех сотрудников, c job_id = IT_PROG. */
SELECT 
* 
from hr.employees e 
where e.job_id = 'IT_PROG';

/*2. Изменить запрос так, чтобы вывести всех сотрудников с job_id равной AD_VP*/
SELECT 
* 
from hr.employees e 
where e.job_id = 'AD_VP';

/*3. Выполнил*/
/*4.1. Найдите сотрудников, с зп от 10 000 до 20 000 (включая концы)*/
SELECT 
* 
from hr.employees e 
where e.salary >= 10000
and e.salary <= 20000;
/*или битвин*/

/*4.2. Найдите сотрудников не из 60, 30 и 100 департамента*/
SELECT 
* 
from hr.employees e 
where e.department_id in (30, 60, 100);

/*4.3. Найдите сотрудников у которых есть две буквы ll подряд в середине имени*/
SELECT 
* 
from hr.employees e 
where e.first_name like '_%ll%_';

/*4.4. Найдите сотрудников, у которых фамилия кончается на a*/
SELECT 
* 
from hr.employees e 
where e.last_name like '%a';

/*4.5. Найдите сотрудников, у которых фамилия кончается на a*/
SELECT 
* 
from hr.employees e 
where e.last_name like '%a';

/*5. Найти всех сотрудников с зарплатой выше 10000*/
SELECT 
* 
from hr.employees e 
where e.salary > 10000;

/*6. Найти всех сотрудников, с зарплатой выше 10000 и чья фамилия начинается на букву L*/
SELECT 
* 
from hr.employees e 
where e.salary > 10000
and e.last_name like 'L%';

/*7. Не выполняя запрос к базе данных, предсказать его результат: select *  from employees where salary > 10000 or salary <= 10000;*/
/*Будут выведены все сотрудники/

/*8.Ответить в 1 предложении: чем он будет отличаться от результата этого запроса? select *  from employees where salary > 10000 or salary < 10000;*/
/*Будут выполнены сотрудники с зп кроме сотрудников где зп 10000 */

/*9. Не выполняя запрос к базе, 
 * предсказать результат. select *  from employees where salary > 10000 and salary < 5000;*/
/*0 результатов, условия перекрывают диапозоны друг друга по salary*/

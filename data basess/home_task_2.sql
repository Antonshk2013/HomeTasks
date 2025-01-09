/*Используя
https://github.com/it-career-hub/MySQL_databases/blob/main/hr_data.sql,*/
/*вывести список всех сотрудников.*/
SELECT
*
FROM employees e;

/*Найти поле с зарплатой сотрудника.*/

SELECT
e.salary
FROM employees e;

/*Используя операторы case/when/end,
изменить запрос так,
чтобы результатом был только один столбец,
назовите его SALARY_GROUP и оно будет принимать значение
1 если зп сотрудника больше 10000 и значение 0, если меньше.*/

SELECT
CASE
	WHEN salary > 10000 THEN 1
	else 0
END as `SALARY_GROUP`
FROM employees e;

/*Ответить одним предложением: почему выводится только один столбец?*/
 Так была поставлена задача, соответственно в запросе указан вывод
/*Изменить запрос,так, чтобы вывелось два столбца:
имя сотрудника и новое поле SALARY_GROUP.*/
SELECT
e.first_name
,CASE
	WHEN salary > 10000 THEN 1
	else 0
END as `SALARY_GROUP`
FROM employees e;

/*Вывести среднюю зарплату для департаментов с
номерами 60, 90 и 100 используя составное условие.*/

SELECT
avg(
CASE
	WHEN department_id = 60 or department_id = 90 or department_id = 100 THEN salary
	ELSE null END) as avg_dp60_90_100
FROM employees;

/*
Разделить уровни (level) сотрудников на
junior < 10000,10000<mid<15000,
senior>15000 в зависимости от их зарплаты.
Вывести список сотрудников (first_name, last_name, level).*/
SELECT
e.first_name
,e.last_name
,CASE
	WHEN e.salary>15000 THEN 'senior'
	WHEN e.salary>10000 THEN 'mid'
	WHEN e.salary>0 THEN 'junior'
END
FROM employees e;


/*Посмотреть содержимое таблицы jobs.
Написать запрос c использованием оператора case/when/end,
который возвращает 2 столбца:
job_id, payer_rank,
где столбец payer_rank формируется по правилу:
если максимальная зарплата больше 10000,
то “high_payer”, если меньше, то “low payer”. */

SELECT
j.job_id
,CASE
	WHEN j.max_salary>10000 THEN 'high_payer'
	ELSE 'low payer'
END as `payer_rank`
FROM jobs j;

/*Переписать этот запрос с использованием оператора IF.*/
SELECT
j.job_id
,IF(j.max_salary>10000, 'high_payer', 'low payer') as `payer_rank`
FROM jobs j;

/* Поменять предыдущий запрос так,
 чтобы выводилось 3 столбца,
 к двум существующим добавьте max_salary
 и отсортировать результат по убыванию. */

SELECT
j.job_id
,IF(j.max_salary>10000, 'high_payer', 'low payer') as `payer_rank`
,j.max_salary
FROM jobs j
ORDER BY j.max_salary DESC;
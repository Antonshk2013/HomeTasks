create table if not exists customers
	(
	id integer not null auto_increment primary key,
	name varchar(255),
	last_name varchar(255),
	post_code integer,
	country varchar(255),
	city varchar(255),
	street varchar(255),
	email varchar(255),
	registration_date date
	);

/*Идентификатор заказчика, который создал
этот заказ,
дата создания заказа,
наименование товара (номер айтема),
описание товара, ссылка на фотографию,
стоимость заказа.*/
create table if not exists orders
	(
	id integer not null auto_increment primary key,
	customer_id integer,
	order_date date,
	good_id integer,
	good_description text,
	good_link varchar(255),
	good_price decimal(10, 2)
)

INSERT INTO customers
(name, last_name, post_code, country, city, street, email, registration_date)
VALUES('Shkarupa', 'Anton', 18146, 'Deutschland', 'Rostock',
'Kurt-Schumacher-Ring 141', 'antonshk2013"gmail.com', '2025-01-22');

INSERT INTO customers
(name, last_name, post_code, country, city, street, email, registration_date)
VALUES('Tkach', 'Julia', 27755, 'Deutschland', 'Delmenhorst',
'Steler Straße 15', 'Julia`Tkach@gmail.com', '2025-01-22');

INSERT INTO customers
(name, last_name, post_code, country, city, street, email, registration_date)
VALUES('Scholz', 'Olaf', 10115, 'Deutschland', 'Berlin',
'Keizer Straße 1', 'OlavSpaß18@gmail.com', '2025-01-22');

INSERT INTO customers
(name, last_name, post_code, country, city, street, email, registration_date)
VALUES('Kruger', 'Diane', 10127, 'Deutschland', 'Berlin',
'Kruger Straße 1', 'Krugersüß@gmail.com', '2025-01-22');

INSERT INTO goods
(title, quantity)
VALUES
('Картошка 1 кг', 100),
('Арбуз 1 кг', 10000),
('Хлеб', 100),
('Вода минеральная 1,5 л', 100);


INSERT INTO orders
(customer_id, order_date, good_id, good_description, good_link, good_price)
VALUES
(1, '2025-01-22', 4, 'Вода из артезианских скважин', 'https://geizer.com/facts/poleznaya-informaciya/artezianskaja-voda/', 1.5),
(3, '2025-01-22', 2, 'Вкусный мамой клянусь', 'https://www.championat.com/lifestyle/article-5594208-arbuz-polza-i-vred-dlya-organizma-cheloveka-protivopokazaniya.html', 3.99),
(4, '2025-01-22', 1, 'Картошка всему голова', 'https://president.gov.by/ru', 0.86),
(2, '2025-01-22', 3, 'Из лучших сортов пшеницы', 'https://www.edimdoma.ru/retsepty/79104-frantsuzskiy-baget-s-hrustyaschey-korochkoy', 0.99),
(1, '2025-01-22', 4, 'Вода из артезианских скважин', 'https://geizer.com/facts/poleznaya-informaciya/artezianskaja-voda/', 1.5),
(2, '2025-01-22', 3, 'Из лучших сортов пшеницы', 'https://www.edimdoma.ru/retsepty/79104-frantsuzskiy-baget-s-hrustyaschey-korochkoy', 0.99),
(3, '2025-01-22', 2, 'Вкусный мамой клянусь', 'https://www.championat.com/lifestyle/article-5594208-arbuz-polza-i-vred-dlya-organizma-cheloveka-protivopokazaniya.html', 3.99),
(4, '2025-01-22', 1, 'Картошка всему голова', 'https://president.gov.by/ru', 0.86),
(3, '2025-01-22', 4, 'Вода из артезианских скважин', 'https://geizer.com/facts/poleznaya-informaciya/artezianskaja-voda/', 1.5),
(4, '2025-01-22', 3, 'Из лучших сортов пшеницы', 'https://www.edimdoma.ru/retsepty/79104-frantsuzskiy-baget-s-hrustyaschey-korochkoy', 0.99);


ALTER TABLE customers ADD COLUMN last_modified date default (CURDATE());
ALTER TABLE customers ADD COLUMN last_modified_time_stamp datetime default (CURRENT_TIMESTAMP());
SELECT CURRENT_TIMESTAMP() ;
SELECT (CURRENT_DATE);

/*Добавить к таблице Order поле discounter_price, которое содержит скидочную
стоимость заказа. Выставить значение этого поля для всех заказов на 10% меньше,
чем оригинальная стоимость заказа.---*/

SELECT * FROM orders o ;
ALTER TABLE orders ADD COLUMN discounter_price decimal(10,2) default (orders.good_price*0.9);

/*Добавить в таблицы тестовые данные: как минимум 3 заказчика по 2-3 заказа у
каждого.*/
INSERT INTO customers
(name, last_name, post_code, country, city, street, email, registration_date)
VALUES('Waldemar', 'Weber', 10115, 'Deutschland', 'Berlin',
'Alexandr Platz 69', 'Waldemarius@gmail.com', '2025-01-22'),
('Dominik', 'Hollmann', 10138, 'Deutschland', 'Berlin',
'Tot Cadets 8', 'Hollman@gmail.com', '2025-01-22'),
('Friedrich', 'Hölderlin', 18146, 'Deutschland', 'Rostock',
'Warnemunde', 'Hölderlin@gmail.com', '2025-01-22');

select * from customers c;

INSERT INTO orders
(customer_id, order_date, good_id, good_description, good_link, good_price)
VALUES
(5, '2025-01-22', 4, 'Вода из артезианских скважин', 'https://geizer.com/facts/poleznaya-informaciya/artezianskaja-voda/', 1.5),
(6, '2025-01-22', 2, 'Вкусный мамой клянусь', 'https://www.championat.com/lifestyle/article-5594208-arbuz-polza-i-vred-dlya-organizma-cheloveka-protivopokazaniya.html', 3.99),
(7, '2025-01-22', 1, 'Картошка всему голова', 'https://president.gov.by/ru', 0.86),
(5, '2025-01-22', 3, 'Из лучших сортов пшеницы', 'https://www.edimdoma.ru/retsepty/79104-frantsuzskiy-baget-s-hrustyaschey-korochkoy', 0.99),
(6, '2025-01-22', 4, 'Вода из артезианских скважин', 'https://geizer.com/facts/poleznaya-informaciya/artezianskaja-voda/', 1.5),
(7, '2025-01-22', 3, 'Из лучших сортов пшеницы', 'https://www.edimdoma.ru/retsepty/79104-frantsuzskiy-baget-s-hrustyaschey-korochkoy', 0.99),
(5, '2025-01-22', 2, 'Вкусный мамой клянусь', 'https://www.championat.com/lifestyle/article-5594208-arbuz-polza-i-vred-dlya-organizma-cheloveka-protivopokazaniya.html', 3.99),
(6, '2025-01-22', 1, 'Картошка всему голова', 'https://president.gov.by/ru', 0.86),
(7, '2025-01-22', 4, 'Вода из артезианских скважин', 'https://geizer.com/facts/poleznaya-informaciya/artezianskaja-voda/', 1.5),
(5, '2025-01-22', 3, 'Из лучших сортов пшеницы', 'https://www.edimdoma.ru/retsepty/79104-frantsuzskiy-baget-s-hrustyaschey-korochkoy', 0.99);

commit;
/*Вывести все заказы, отсортированные по убыванию по стоимости*/
select
*
from orders o
order by o.good_price DESC;

/*Вывести всех заказчиков, у которых почта зарегистриварована на gmail.com*/
SELECT
*
from customers c
where c.email like '%gmail.com'

/*Вывести заказы, добавив дополнительный вычисляемый столбец status,
 * который вычисляется по стоимости заказа и имеет три значения: low, middle, high. */
SELECT
*,
CASE
	WHEN o.good_price < 1 THEN 'low'
	WHEN o.good_price > 3 THEN 'hight'
	ELSE 'middle'
END as "STATUS"
from orders o ;
/*Вывести заказчиков по убыванию рейтинга.*/
SELECT
*
FROM customers c order by c.id desc;

/*Вывести всех заказчиков из города на ваш выбор.*/
SELECT * from customers c where c.city = 'Berlin';

/*Написать запрос, который вернет самый часто продаваемый товар. */
SELECT
o.good_description ,
COUNT(o.good_description)
FROM orders o
GROUP BY o.good_description

/*Вывести список заказов с максимальной скидкой.*/
SELECT
*
FROM orders o
where (o.good_price - o.discounter_price) = (SELECT
max(o.good_price - o.discounter_price) as 'discount'
FROM orders o );

/*Ответьте в 1 предложении: как вы определите скидку? */
/*Разностью двух значений*/

/*Ответьте в 1 предложении: может ли это быть разница между нормальной ценой и скидочной ценой?*/
/*может*/

/*Написать запрос, который выведет все заказы с дополнительным
 столбцом процент_скидки, который содержит разницу в процентах
 между нормальной и скидочной ценой?*/
 select
 *
 , round((o.discounter_price/o.good_price)*100,2) as "discountPersent"
 from orders o







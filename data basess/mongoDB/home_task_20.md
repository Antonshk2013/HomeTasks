# Домашнее задание №20

## 1. Dывести названия фильмов с расшифровкой рейтинга для каждого 
```
select 
title,
rating,
case 
	when rating = 'G' then 'General Audiences' 
	when rating = 'PG' then 'Parental Guidance Suggested' 
	when rating = 'PG-13' then 'Parents Strongly Cautioned' 
	when rating = 'R' then 'Restricted' 
	when rating = 'NC-17' then 'Adults Only'  
end as rating_description
from film;

```
## 2. Выведите количество фильмов в каждой категории рейтинга. Используем group by
```
select 
rating ,
count(film_id)
from film
group by rating;

```

## 3. Используя оконные функции и partition by, выведите список названий фильмов, рейтинг и количество фильмов в каждом рейтинге. Объясните, чем отличаются результаты предыдущего запроса и запроса в этой задаче.*/

```
select
title,
rating,
COUNT(*) OVER (PARTITION BY rating) AS ratings_count
from film;
```
## 3.Изучите таблицы payment и customer. Выведите список всех платежей с указанием имени и фамилии каждого заказчика, датой платежа и суммой.
```
select
c.first_name ,
c.last_name ,
p.payment_date ,
p.amount 
from payment p 
left join customer c 
on p.customer_id = c.customer_id ;
```
## 4.Поменяйте предыдущий запрос так, чтобы дата выводилась в формате “число, название месяца, год” (без времени).*/
```
select
c.first_name ,
c.last_name ,
DATE_FORMAT(p.payment_date, '%d-%m-%Y'),
p.amount 
from payment p 
left join customer c 
on p.customer_id = c.customer_id ;
```
## 5. Найти рестораны на 'Staten Island' в названии которых есть слово pizza (Pizza и PIZZA тоже считаются))
```
db.restaurants.aggregate([{$match:{
  borough: "Staten Island",
  name: { $regex: "pizza", $options: "i" }
}}])
```
## 6. Выведите названия 5 лучших по среднему значению отзывов ( $avg: "$grades.score")
```
[
  {
    $addFields:
      {
        avgGrade: {
          $avg: "$grades.score"
        }
      }
  },
  {
    $sort:
      {
        avgGrade: -1
      }
  },
  {
    $limit:
      5
  }
]
```
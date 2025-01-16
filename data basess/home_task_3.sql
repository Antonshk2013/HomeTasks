/*Не подглядывая в решение в классе, создать таблицу weather с тремя полями:
название города (city)
дата (forecast_date)
температура в эту даты (temperature)*/

CREATE TABLE IF NOT EXISTS weather(
	city varchar(100),
	forecast_date date,
	temperature integer
	);

/*Вывести содержимое таблицы*/
SELECT * FROM weather w ;

/*Добавить данные в таблицу, используя запрос INSERT
“29 августа 2023 года в Берлине было 30 градусов”*/

INSERT INTO weather
(city, forecast_date, temperature)
VALUES('Berlin', '2023-08-29', 30);
COMMIT;


/*Добавить еще 3 записи в таблицу
 * (произвольную погоду в разных городах в разные дни).*/
INSERT INTO weather
(city, forecast_date, temperature)
VALUES
('Rostock', '2023-08-30', 28),
('Lübeck', '2023-08-31', 29),
('Hamburg', '2023-09-01', 29);
COMMIT;

/*Написать запрос, который возвращает содержимое таблицы.*/
SELECT * FROM weather w;

/*Изменить данные в таблице о температуре в Берлине с 30 на 26 градусов.*/
UPDATE weather SET temperature =26 WHERE city ="Berlin";
COMMIT;

/*Поменяйте во всей таблице название города на Paris для записей,
 * где температура выше 25 градусов. */
UPDATE weather SET city ="Paris" WHERE temperature > 25;
COMMIT;

/*Добавить к таблице weather дополнительный столбец min_temp типа integer.*/
ALTER TABLE weather ADD COLUMN min_temp int;

/*Используя команду update,
 *установить значение поля min_temp в 0 для всех записей в таблице*/
UPDATE weather set min_temp = 0;
COMMIT;

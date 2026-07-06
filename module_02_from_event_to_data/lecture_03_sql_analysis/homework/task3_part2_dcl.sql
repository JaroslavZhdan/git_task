-- 1. Создать новую роль (пользователя) PostgreSQL с именем data_engineer_trainee (стажер) и простым паролем.
CREATE USER
	data_engineer_trainee
WITH PASSWORD '123456';

-- 2. Предоставить data_engineer_trainee право SELECT на таблицу Sales.
GRANT SELECT
	ON Sales
	TO data_engineer_trainee;

-- 3. (В новой сессии) подключитесь как data_engineer_trainee и выполните SELECT * FROM Sales;.
SELECT * FROM sales;

-- 4. Как data_engineer_trainee, попытаться выполнить INSERT новой продажи в Sales. (Должно завершиться неудачей).
INSERT INTO
	sales (sales_id, employee_id, customer_id, product_id, quantity, discount, total_price, sales_timestamp, transaction_number)
VALUES
	(2000001, 84, 90121, 1, 3, 0.21, 83, now(), 'T0002000001')

-- 5. Как пользователь-администратор, предоставить data_engineer_trainee права INSERT и UPDATE на таблицу Sales.
GRANT
	INSERT
	ON sales
	TO data_engineer_trainee;

GRANT
	UPDATE
	ON sales
	TO data_engineer_trainee;

-- 6. Как data_engineer_trainee, попробовать выполнить INSERT и UPDATE. (Теперь должно сработать).
INSERT INTO
	sales (sales_id, employee_id, customer_id, product_id, quantity, discount, total_price, sales_timestamp, transaction_number)
VALUES
	(2000001, 84, 90121, 1, 3, 0.21, 83, now(), 'T0002000001')
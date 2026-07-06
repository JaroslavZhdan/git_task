-- 1. Увеличить цену всех продуктов категории 'Fruits' на 10%.
UPDATE
	products
SET
	price = price + (price * 10 / 100)
FROM
	categories
WHERE products.category_id = categories.category_id AND categories.category_name = 'Fruits';

-- 2. Удалить всех сотрудников без продаж.
DELETE
FROM
	employees
WHERE (
	SELECT
		COUNT(*)
	FROM
		sales
	WHERE
		employees.employee_id = sales.employee_id
	) = 0

-- 3. Вставить нового сотрудника и первую продажу в одной транзакции.
BEGIN;
	INSERT INTO
		employees
	VALUES
		(321, 'Carl', 'T', 'Loonacy', '1978-05-09', 'M', 3, 22, '2018-08-16');

	INSERT INTO
		sales (sales_id, employee_id, customer_id, product_id, quantity, discount, total_price, sales_timestamp, transaction_number)
	VALUES
		(2000002, 321, 90121, 1, 3, 0.21, 83, now(), 'T0002000002');
COMMIT;
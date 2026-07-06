-- 1. Найти сотрудников с продажами > 1000.
WITH employee_better_than_1000 AS (
	SELECT
		employee_id,
		COUNT(*)
	FROM
		sales
	GROUP BY
		employee_id
)
SELECT
	employees.*
FROM
	employee_better_than_1000
JOIN
	employees ON employee_better_than_1000.employee_id = employees.employee_id
WHERE
	employee_better_than_1000.count > 1000;

-- 2. Обновить класс продуктов на 'A' для категорий с общей выручкой > 5000.
WITH revenue AS (
	SELECT
		product_id,
		SUM(total_price) as revenue_amount
	FROM
		sales
	GROUP BY
		product_id
)
UPDATE
	products
SET
	class = 'A'
FROM
	revenue
WHERE
	revenue.product_id = products.product_id AND revenue.revenue_amount > 5000

-- 3. Установить modify_timestamp (функция NOW()) для продуктов без даты.
UPDATE
	products
SET
	modify_timestamp = now()
WHERE
	modify_timestamp IS NULL;

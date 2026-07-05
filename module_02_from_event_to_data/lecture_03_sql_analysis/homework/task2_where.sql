-- Задание 1
SELECT
	shop_id, address, cities.city_name, countries.country_name
FROM
	shops as s
JOIN
	cities ON s.city_id = cities.city_id
JOIN
	countries ON cities.country_id = countries.country_id
WHERE
	country_name = 'Poland';

-- Задание 2
SELECT
	transaction_number, products.product_name, total_price, customer_id, sales_timestamp
FROM
	sales as s
JOIN
	products ON s.product_id = products.product_id
WHERE
	total_price > 1500 AND class = 'A'
ORDER BY
	transaction_number;

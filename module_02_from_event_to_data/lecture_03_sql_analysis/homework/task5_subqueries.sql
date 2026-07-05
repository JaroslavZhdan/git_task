SELECT
	e.first_name, e.last_name, shops.address, s.total_price
FROM
	sales as s
JOIN
	employees as e ON s.employee_id = e.employee_id
JOIN
	shops ON e.shop_id = shops.shop_id
WHERE
	s.total_price = (SELECT MAX(total_price)
	FROM sales)
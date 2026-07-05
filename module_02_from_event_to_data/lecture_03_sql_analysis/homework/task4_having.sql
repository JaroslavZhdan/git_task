SELECT
	products.product_name, SUM(total_price) as total_revenue, AVG(total_price) as avg_sale
FROM
	sales as s
JOIN
	products ON s.product_id = products.product_id
GROUP BY
	products.product_name
HAVING
	SUM(total_price) > 400000
ORDER BY
	SUM(total_price) DESC;

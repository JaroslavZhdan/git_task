SELECT
    DATE_TRUNC('month', sales_timestamp) AS month_start,
    SUM(total_price) AS monthly_sum,
    LAG(SUM(total_price), 1) OVER (ORDER BY DATE_TRUNC('month', sales_timestamp)) AS prev_month_sum,
	SUM(total_price) - COALESCE(LAG(SUM(total_price), 1) OVER (ORDER BY DATE_TRUNC('month', sales_timestamp)), 0) as revenue_diff_vs_previous
FROM
	sales
JOIN
	employees ON sales.employee_id = employees.employee_id
JOIN
	shops ON employees.shop_id = shops.shop_id
JOIN
	cities ON shops.city_id = cities.city_id
JOIN
	countries ON cities.country_id = countries.country_id
WHERE
	countries.country_name = 'Germany'
GROUP BY
	DATE_TRUNC('month', sales_timestamp)
ORDER BY
	month_start;
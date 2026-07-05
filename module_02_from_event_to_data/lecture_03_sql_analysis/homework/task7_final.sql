WITH shops AS (
    SELECT
        countries.country_name AS country,
        shops.shop_id,
        shops.address AS shop_address,
        COUNT(sales_id) AS total_sales_count,
        SUM(total_price) AS total_sales_amount
    FROM sales
    JOIN employees ON sales.employee_id = employees.employee_id
    JOIN shops ON employees.shop_id = shops.shop_id
    JOIN cities ON shops.city_id = cities.city_id
    JOIN countries ON cities.country_id = countries.country_id
    WHERE (
        SELECT COUNT(*)
        FROM sales s2
        JOIN employees e2 ON s2.employee_id = e2.employee_id
        WHERE e2.shop_id = shops.shop_id
    ) >= 2
    GROUP BY countries.country_name, shops.shop_id, shops.address
)
SELECT
    country,
    shop_id,
    shop_address,
    total_sales_count,
    total_sales_amount,
    SUM(total_sales_amount) OVER (PARTITION BY country) AS country_total_amount,
	total_sales_amount / NULLIF(SUM(total_sales_amount) OVER (PARTITION BY country), 0) AS share_percent,
	RANK() OVER (PARTITION BY country ORDER BY total_sales_amount DESC) as rank_of_country,
	SUM(total_sales_amount) OVER (PARTITION BY country ORDER BY total_sales_amount DESC) as country_running_total
FROM shops
ORDER BY country, rank_of_country;
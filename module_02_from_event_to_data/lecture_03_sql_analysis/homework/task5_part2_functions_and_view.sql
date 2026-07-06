-- 1. Функция: Создать функцию AvgSalesPerEmployee (PL/pgSQL), для вычисления средней суммы продаж для сотрудника.
CREATE OR REPLACE FUNCTION AvgSalesPerEmployee(IN employee_id_search INT)
RETURNS employees AS $$
DECLARE
    result employees;
BEGIN
    SELECT * INTO result
    FROM employees
    WHERE employee_id = employee_id_search;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- 2. Представление (View): Создать представление FullStatShops для суммарной статистики по магазинам с колонками (shop_id, shop_address, country, total_sales_count, total_sales_amount).
CREATE OR REPLACE VIEW FullStatShops AS
	WITH shops AS (
	    SELECT
	        countries.country_name AS country,
	        shops.shop_id as shop_id,
	        shops.shop_address AS shop_address,
	        COUNT(sales_id) AS total_sales_count,
	        SUM(total_price) AS total_sales_amount
	    FROM sales
	    JOIN employees ON sales.employee_id = employees.employee_id
	    JOIN shops ON employees.shop_id = shops.shop_id
	    JOIN cities ON shops.city_id = cities.city_id
	    JOIN countries ON cities.country_id = countries.country_id
	    GROUP BY countries.country_name, shops.shop_id, shops.shop_address
	)
	SELECT
		shop_id,
	    shop_address,
		country,
	    total_sales_count,
	    total_sales_amount
	FROM
		shops;
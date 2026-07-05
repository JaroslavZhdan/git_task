SELECT
	countries.country_name, COUNT(*) as shops_count
FROM
	shops as s
JOIN cities ON s.city_id = cities.city_id
JOIN
	countries ON cities.country_id = countries.country_id
GROUP BY
	countries.country_name
ORDER BY
	shops_count DESC;

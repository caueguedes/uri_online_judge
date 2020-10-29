SELECT COUNT(cities.city)
FROM
(
	SELECT
		customers.city
	FROM customers
	GROUP BY customers.city
) as cities

-- OR

SELECT COUNT(distinct(customers.city)) FROM customers
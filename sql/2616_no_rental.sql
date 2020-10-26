SELECT
	customers.id,
	customers.name
FROM customers WHERE NOT EXISTS (
	SELECT  locations.id_customers
	FROM locations
	where locations.id_customers = customers.id
)
ORDER BY
customers.id


-- OR
SELECT
	customers.id,
	customers.name
FROM
	customers left join locations ON customers.id = locations.id_customers
GROUP BY
    customers.id,
    customers.name
WHERE locations.id is NULL
SELECT
	customers.name,
	rentals.rentals_date
FROM
	rentals JOIN customers ON rentals.id_customers = customers.id
WHERE
	rentals.rentals_date BETWEEN '2016-09-01' AND '2016-09-30'
SELECT
	products.name,
	CASE
		WHEN products.type = 'A' THEN 20.0
		WHEN products.type = 'B' THEN 70.0
		WHEN products.type = 'C' THEN 530.5
	END as price
FROM products
ORDER BY price, products.id DESC
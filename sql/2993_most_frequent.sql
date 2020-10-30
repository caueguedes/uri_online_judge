SELECT
	amount as most_frequent_value
FROM (
	SELECT
		amount,
		count(amount) as appearances
	FROM value_table
	GROUP BY value_table.amount
	ORDER BY appearances DESC
	LIMIT 1
) as appearances
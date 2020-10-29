SELECT
	loan.name,
	EXTRACT(DAY FROM loan.payday)::INTEGER
FROM loan
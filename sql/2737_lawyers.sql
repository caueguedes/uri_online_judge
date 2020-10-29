SELECT * FROM (
	SELECT lawyers.name, lawyers.customers_number
	FROM lawyers WHERE lawyers.customers_number in (
		SELECT MAX(lawyers.customers_number) FROM lawyers
			UNION SELECT MIN(lawyers.customers_number) FROM lawyers
	) ORDE R BY customers_number DESC
) min_max

UNION all SELECT 'Average', aver FROM (
	SELECT FLOOR(AVG(val)) as aver
	from (SELECT MAX(lawyers.customers_number) as val FROM lawyers
		UNION SELECT MIN(lawyers.customers_number) as val FROM lawyers ) as max_min)
as average
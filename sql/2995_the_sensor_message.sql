SELECT
	records.temperature,
	count(records.mark) as number_of_records
FROM records
GROUP BY records.mark, records.temperature
ORDER BY records.mark
SELECT
	cumulative_profit.name,
	cumulative_profit.investment,
	cumulative_profit.month as month_of_payback,
	cumulative_profit.cumulative - cumulative_profit.investment as return
FROM (
	SELECT
		clients.name,
		clients.investment,
		operations.month,
		operations.profit,
		(
			SELECT
				SUM(op2.profit)
			FROM operations as op2
			WHERE op2.month <= operations.month and op2.client_id = clients.id
		) as cumulative
	FROM
		clients JOIN operations ON clients.id = operations.client_id
) as cumulative_profit
WHERE cumulative >= investment and (cumulative - profit) <= investment
ORDER BY return DESC
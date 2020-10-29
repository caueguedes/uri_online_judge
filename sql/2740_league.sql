SELECT name FROM (
	SELECT * FROM (
		SELECT
			league.position,
			format('Podium: %1$s', league.team) as name
		FROM
			league
		LIMIT 3
	) as top
	UNION all
	SELECT * FROM (
		SELECT
			league.position,
			format('Demoted: %1$s', league.team) as name
		FROM
			league
		ORDER BY league.position DESC
		LIMIT 2
	) as bottom
) as final order by position
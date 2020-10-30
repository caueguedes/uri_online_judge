SELECT
	name,
	COUNT(*) as matches,
	SUM(victories) as victories,
	SUM(defeats) as defeats,
	SUM(draws) as draws,
	(SUM(victories)*3 + SUM(draws)) as score
FROM(
	SELECT
		teams.name,
		CASE
			WHEN matches.team_1_goals > matches.team_2_goals THEN 1 ELSE 0
		END as victories,
		CASE
			WHEN matches.team_1_goals < matches.team_2_goals THEN 1 ELSE 0
		END as defeats,
		CASE
			WHEN matches.team_1_goals = matches.team_2_goals THEN 1 ELSE 0
		END as draws
	FROM matches LEFT JOIN teams as teams ON matches.team_1 = teams.id
	UNION ALL
	SELECT
		teams.name,
		CASE
			WHEN matches.team_2_goals > matches.team_1_goals THEN 1 ELSE 0
		END as victories,
		CASE
			WHEN matches.team_2_goals < matches.team_1_goals THEN 1 ELSE 0
		END as defeats,
		CASE
			WHEN matches.team_2_goals = matches.team_1_goals THEN 1 ELSE 0
		END as draws
	FROM matches LEFT JOIN teams as teams ON matches.team_2 = teams.id
) as score_table
GROUP BY score_table.name
ORDER BY score DESC, name ASC


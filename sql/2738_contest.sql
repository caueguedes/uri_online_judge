SELECT
    candidate.name,
    ((score.math * 2 + score.specific * 3 + score.project_plan *5)/10)::numeric(10, 2) as score
FROM candidate JOIN score ON candidate.id = score.candidate_id
ORDER BY score DESC

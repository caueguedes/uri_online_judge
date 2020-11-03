WITH
salary AS(
    SELECT matr, nome, lotacao, lotacao_div, SUM(valor)::NUMERIC(10,2) as salario
    FROM
    (
        SELECT empregado.matr, empregado.lotacao, empregado.lotacao_div, empregado.nome,  COALESCE(vencimento.valor, 0) as valor
        FROM empregado
            LEFT JOIN emp_venc ON empregado.matr = emp_venc.matr
            LEFT JOIN vencimento ON emp_venc.cod_venc = vencimento.cod_venc
        UNION ALL
        SELECT empregado.matr, empregado.lotacao, empregado.lotacao_div, empregado.nome, -desconto.valor
        FROM empregado
            JOIN emp_desc ON empregado.matr = emp_desc.matr
            JOIN desconto ON emp_desc.cod_desc = desconto.cod_desc
    ) as salary_values
    GROUP BY lotacao, lotacao_div, matr, nome
), average as (
	SELECT
		lotacao_div,
		lotacao,
		AVG(salario)::NUMERIC(10,2) as media_salarial
	FROM salary
	GROUP BY lotacao_div, lotacao
)

SELECT
	departamento.nome as departamento,
	divisao.nome as divisao,
	media_salarial as media
FROM average
JOIN  (
	SELECT
		lotacao,
		MAX(media_salarial)
	FROM average
	GROUP by lotacao
) max_depart ON average.lotacao = max_depart.lotacao AND average.media_salarial = max_depart.max
JOIN divisao ON average.lotacao_div = divisao.cod_divisao
JOIN departamento ON average.lotacao = departamento.cod_dep
ORDER BY media DESC
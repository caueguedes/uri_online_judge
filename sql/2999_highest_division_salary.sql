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
),
average AS(
	Select
		lotacao_div, lotacao,
		AVG(salario)::NUMERIC(10,2) media_salarial
	FROM salary GROUP BY lotacao_div, lotacao
)

SELECT nome, salario
 FROM salary LEFT JOIN average ON salary.lotacao_div = average.lotacao_div
 WHERE salary.salario > average.media_salarial
 ORDER BY salario DESC
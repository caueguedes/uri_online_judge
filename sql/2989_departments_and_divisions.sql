SELECT
	salario.departamento,
	salario.divisao,
	AVG(salario.salario - coalesce(descontos.descontos, 0))::NUMERIC(10,2) as media,
	MAX(salario.salario - coalesce(descontos.descontos, 0)) as maior
FROM (
	SELECT
		departamento.nome as departamento,
		divisao.nome as divisao,
		empregado.matr,
 		COALESCE(SUM(vencimento.valor), 0) as salario
	FROM departamento
		JOIN divisao ON divisao.cod_dep = departamento.cod_dep
	 	JOIN empregado ON empregado.lotacao_div = divisao.cod_divisao
		LEFT JOIN emp_venc ON emp_venc.matr = empregado.matr
		LEFT JOIN vencimento ON vencimento.cod_venc = emp_venc.cod_venc
	GROUP BY departamento.nome, divisao.nome, empregado.matr
) as salario
LEFT JOIN (
	SELECT
		empregado.matr,
		SUM(desconto.valor) as descontos
	FROM empregado
		JOIN emp_desc ON emp_desc.matr = empregado.matr
		JOIN desconto ON desconto.cod_desc = emp_desc.cod_desc
	GROUP BY empregado.matr
) as descontos ON descontos.matr = salario.matr
GROUP BY departamento, divisao
ORDER BY media DESC, maior DESC
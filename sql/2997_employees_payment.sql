SELECT
	departamento as "Departamento",
	nome as "Empregado",
	salario as "Salario Bruto",
	COALESCE(descontos, 0) as "Total Descontos",
	(salario - COALESCE(descontos,0)) as "Salario Liquidoaws"
FROM(
	SELECT
		empregado.nome,
		departamento.nome as departamento,
		empregado.matr,
		COALESCE(SUM(vencimento.valor), 0) as salario
	FROM departamento
		JOIN divisao ON divisao.cod_dep = departamento.cod_dep
		JOIN empregado ON empregado.lotacao_div = divisao.cod_divisao
		LEFT JOIN emp_venc ON emp_venc.matr = empregado.matr
		LEFT JOIN vencimento ON vencimento.cod_venc = emp_venc.cod_venc
	GROUP BY departamento.nome, empregado.matr, empregado.nome
) as salarios LEFT JOIN (
	SELECT
		empregado.matr,
		SUM(desconto.valor) as descontos
	FROM empregado
		JOIN emp_desc ON emp_desc.matr = empregado.matr
		JOIN desconto ON desconto.cod_desc = emp_desc.cod_desc
	GROUP BY empregado.matr
) as descontos
ON salarios.matr = descontos.matr
ORDER BY "Salario Liquidoaws" DESC, salarios."matr"
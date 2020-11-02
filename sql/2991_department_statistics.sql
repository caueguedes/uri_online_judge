SELECT
	departamento as "Nome Departamento",
	COUNT(nome) as "Numero de Empregados",
	AVG(salario - COALESCE(descontos,0))::NUMERIC(10,2) as "Media Salarial",
	MAX(salario - COALESCE(descontos,0))::NUMERIC(10,2) as "Maior Salario",
	CASE
		WHEN MIN(salario - COALESCE(descontos,0)) = 0 THEN 0
		ELSE MIN(salario - COALESCE(descontos,0))::NUMERIC(10,2)
  	END as "Menor Salario"
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
GROUP BY departamento
ORDER BY "Media Salarial" DESC
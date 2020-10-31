SELECT
	empregados.cpf,
	empregados.enome,
	departamentos.dnome
FROM empregados
	JOIN departamentos ON empregados.dnumero = departamentos.dnumero
WHERE NOT EXISTS (
	SELECT *
	FROM trabalha
	WHERE empregados.cpf like trabalha.cpf_emp
)
ORDER BY empregados.cpf

SELECT
    people.name,
    (people.salary*0.1)::numeric(10, 2) as tax
FROM people
WHERE people.salary > 3000
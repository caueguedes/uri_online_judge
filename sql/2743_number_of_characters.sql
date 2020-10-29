SELECT
    people.name,
    char_length(people.name) as length
FROM people
ORDER BY LENGTH
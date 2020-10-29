SELECT
    products.name,
    categories.name
FROM
    products JOIN categories ON products.id_categories = categories.id
WHERE categories.id in (1,2,3,6,9) AND products.amount > 100
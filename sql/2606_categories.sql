SELECT id, name FROM products where id_categories in (select id from categories where name like 'super%');

-- or
select products.id, products.name from products join categories on products.id_categories = categories.id where categories.name like 'super%'

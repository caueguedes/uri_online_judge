SELECT
    life_registry.name,
    (life_registry.omega*1.618)::numeric(10, 3) as 	"The N Factor"
FROM life_registry JOIN dimensions
	ON life_registry.dimensions_id = dimensions.id
WHERE life_registry.name like 'Richard%'
    AND dimensions.name in  ('C875', 'C774')
ORDER BY life_registry.omega
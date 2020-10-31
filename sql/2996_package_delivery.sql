SELECT
    packages.year,
	sender.name as sender,
	receiver.name as receiver
FROM packages
JOIN users as sender on packages.id_user_sender = sender.id 
JOIN users as receiver on packages.id_user_receiver = receiver.id 
WHERE (packages.color = 'blue' OR packages.year = 2015) AND sender.address != 'Taiwan' AND receiver.address != 'Taiwan' 
ORDER BY packages.year DESC
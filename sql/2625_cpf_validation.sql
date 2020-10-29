SELECT  format('%1$s.%2$s.%3$s-%4$s', 
			   substring(natural_person.cpf from 1 for 3),
			   substring(natural_person.cpf from 4 for 3),
			   substring(natural_person.cpf from 7 for 3),
			   substring(natural_person.cpf from 10 for 2)) FROM natural_person 

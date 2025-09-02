course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information['description'])




course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information.get('description'))





# course_information = {
# 	'title': 'Introduction to DBs',
# 	'description': 'Here we review the basics of SQL Databases',
# 	'length_in_minutes': 600,
# }

# print(course_information['episodes'])



course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information.get('episodes'))



#Iterando el keys
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country in europe_capitals_by_country.keys():
  print(country)



# Iterando el values
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for capital in europe_capitals_by_country.values():
  print(capital)


user_data = {
	'full_name': 'John Snow',
	'email': 'j.snow@gmail.com',
}

user_data['password'] = 'WinterIsComing2023'
print(user_data)



student_information = {
	'first_name': 'Harry',
	'last_name': 'Potter',
	'age': 17,
}

deleted_item = student_information.pop('last_name')
print(student_information)
print(f'Deleted item: {deleted_item}')







empresa = {
    "nombre": "Tech Solutions Inc.",
    "rubro": "Tecnología y Software",
    "departamentos": [
        {
            "funcion": "Desarrollo de software",
            "numero_personal": 75,
            "nombre_presidente": "Dr. Elena García"
        },
        {
            "funcion": "Marketing digital",
            "numero_personal": 30,
            "nombre_presidente": "Lic. Pablo Ruiz"
        },
        {
            "funcion": "Recursos humanos",
            "numero_personal": 15,
            "nombre_presidente": "Mtra. Sofía López"
        }
    ]
}

print(empresa)
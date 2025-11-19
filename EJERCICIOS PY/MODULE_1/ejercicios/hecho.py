my_string = "Este es un string"
my_multiline_string = """
	Este
	es
	un
	string
	de
	multiples
	lineas
"""

print(my_string)
print('Este tambien es un string')
print(my_multiline_string)

other_string = 'Bond'
concatenated_string = 'my name is' + other_string
print(concatenated_string)

other_string= 'bond'
f_string= f'my name is {other_string}'
print (f_string)

my_first_list= [2,5,7,8]
print(my_first_list[1])
print(my_first_list[0])
print(my_first_list[0+1])

list_of_integers=[4,7,3,5+4,3]
list_of_strings=["hello","i am","a","string","list"]
list_of_booleans=['true','true','false']
print(list_of_integers[3])
print (list_of_strings[2])
print(list_of_booleans[2])
print (list_of_strings[3])

my_first_tuple=(2,5,7,8)
print(my_first_tuple[2])

my_first_dictionary={"key":5,
                     "other_key":"hello again",
                     "final_key":98,
}
print(my_first_dictionary["other_key"])

horas_trabajadas=0
tarifa_por_hora=0
salario=horas_trabajadas*tarifa_por_hora

# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print

print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema

print(len(my_int_to_str_variable))  # Es una abreviatura de length, lo que hace
# es contar los caracteres, contando los espacios

# Variables en una sola línea

name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, ". Mi edad es:", age, "Y mi alias es:", alias)

# Inputs
"""
name = input('¿Cuál es tu nombre?')
age = input('¿Cuántos años tienes?')

print(name)
print(age)
#Las variables se están reasignando, se han sobreescrito
"""

# Cambiamos su tipo

name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
print(type(address))  # Ha imprimido 32 y el programa funciona. El tipo es int. En
# realidad nosotros podemos especificar este tipado para ayudarnos de alguna forma a
# entender que queremos que sea un string. Nosotros incluso podríamos configurar el id
# para indicarle que de un error, si le pasaramos un linter o algo que fuera capaz
# de analizar la sintaxis que estamos usando. Se podría ir cambiando y se quedaría con
# el último. Aunque lo hayamos tipado de una forma, no es tipado.

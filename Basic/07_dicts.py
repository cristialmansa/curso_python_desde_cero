### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))  # <class 'dict'>
print(type(my_other_dict))  # <class 'dict'>

my_other_dict = {"Nombre": "Brais",
    "Apellido": "Moure", "Edad": 35, 1: "Python"}
# Aquí lo que tendremos será relación clave/valor

my_dict = {
	"Nombre": "Brais",
	"Apellido": "Moure",
	"Edad": 35,
	"Lenguajes": {"Python", "Swift", "Kotlin"},
	1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))  # 4 elementos
print(len(my_dict))  # 5 elementos

# Brais. La facilidad que nosotros tenemos para acceder
print(my_dict["Nombre"])
# a un elemento

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])  # Pedro

print(my_dict[1])  # 1'77. Se accede así porque es un entero. Si pusiéramos
# print(my_dict["1"]) nos daría un error

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)  # Esta es una manera de agregar elementos al diccionario

del my_dict["Calle"]
print(my_dict)  # Esta sería la manera de eliminar un elemento concreto de nuestro
# diccionario.

# False. Nos dice False porque de esta manera estamos buscando
print("Moure" in my_dict)
# por clave, no por valor
# True, porque si que hay una clave que sea Apellido
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())  # Lo que tenemos es un listado con cada uno de los items
print(my_dict.keys())  # Solo nos retorna un listado de las keys
print(my_dict.values())  # Nos retorna todos los valores

# my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso"))
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)  # De esta forma lo que hacemos es crear un diccionario nuevo que
# no tiene valores. En realidad es algo que no nos vale para nada. Lo suyo sería
# hacerlo con dict, que es una palabra reservada ya que es absurdo usar my_other_dict
# cuando no podemos utilizar ninguno de los valores.

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Brais", "Moure"))
# De esta manera, a todos los elementos se le meten los valores de
print(my_new_dict)
# Brais y Moure.

my_new_dict = dict.fromkeys(my_dict, ["Brais", "Moure"])
print(my_new_dict)  # De esta manera, ocurre lo mismo que en la anterior

my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))

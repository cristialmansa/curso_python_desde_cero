### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))  # Ahora sería un set

print(len(my_other_set))  # 3, porque tiene 3 elementos

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada, de
# ahí que no podamos acceder al elemento 0

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Búsquedas:
print("Moure" in my_other_set)  # True
print("Mouri" in my_other_set)  # False

# Operaciones como eliminar:
my_other_set.remove("Moure")
print(my_other_set)

# Operaciones como clear, el clear borra todos los elementos que tiene nuestro set
my_other_set.clear()
print(len(my_other_set))  # 0

# del, palabra reservada del sistema, no quiere decir que esté relacionado con el set
# Las que son propias del set son las que están después del .
del my_other_set
print(my_other_set)  # NameError: name 'my_other_set' is not defined

my_set = {"Brais", "Moure", 35}
# Hacer este tipo de transformaciones es muy arriesgado porque
my_list = list(my_set)
# no vamos a saber el orden de los elementos
print(my_list)
print(my_list[0])

my_other_set = {"Kotli", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set)  # En este caso no aparecen 12 elementos porque
# no se duplican, no se pueden repetir los elementos

print(my_new_set.union(my_new_set).union(my_set).union({"Javascript", "C#"}))

# Tenemos un set que tiene solo {"Kotli", "Swift",
print(my_new_set.difference(my_set))
# "Python"}, no aparecen {"Javascript", "C#"} porque hemos hecho un union en un print
# es decir, solo para ese print pero no está almacenado en la variable

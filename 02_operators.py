### Operadores Aritméticos ###

print(3 + 4)  # 7
print(3 - 4)  # -1
print(3 * 4)  # 12
print(3 / 4)  # 0.75
print(10 % 4)  # 0 es el resto que tenemos de una división, el operador de módulo
print(10 % 3)  # 1
# 3 Operación de división de dos barras, es un floor division. Esto nos va
print(10 // 3)
# a dar siempre un número entero aunque la división nos diera un decimal, la va a
# intentar siempre aproximar.
print(2 ** 3)  # 8 Calcular un exponente. 2 elevado a 3 = 8, lo hacemos como el
# multiplicar pero con dos.
print(2 ** 3 + 3 - 7 / 1 // 4)  # 10.0

print("Hola" + "Python")  # HolaPython
# print("Hola" * "Python")  # Error
# Con cadenas de texto si podemos realizar sumas y se suman esas cadenas de caracteres
# print("Hola" + 5)  # Error
# No podemos mezclar un entero con un string, sin embargo, tenemos algunas funciones
# del sistema para poder realizarlo
print("Hola" + str(5))  # Hola 5
print("Hola " * 5)  # Hola Hola Hola Hola Hola
print("Hola " * (2 ** 3))  # Hola Hola Hola Hola Hola Hola Hola Hola

my_float = 2.5 * 2
print("Hola " * int(my_float))  # Hola Hola Hola Hola Hola

## Operadores Comparativos ##

print(3 > 4)  # False
print(3 < 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True
print(3 == 4)  # False
print(3 != 4)  # True

print("Hola" > "Python")  # False
print("Hola" < "Python")  # True
print("Hola" >= "Python")  # False
print("Hola" <= "Python")  # True
print("Hola" == "Python")  # False
print("Hola" != "Python")  # True
print("Hola" >= "Zola")  # False Ordenación alfabética
print("aaaa" >= "abaa")  # False
# Lo que hace es hacer una comparación entre ordenación alfabética
# Ordenación alfabética por ASCII
# Si quisiéramos hacerlo contando caracteres:
print(len("aaaa") >= len("abaa"))  # True


## Operadores Lógicos ##

# La lógica booleana rige toda la programación
print(3 > 4 and "Hola" > "Python")  # False
print(3 > 4 or "Hola" > "Python")  # False
print(3 < 4 and "Hola" < "Python")  # True
print(3 < 4 or "Hola" < "Python")  # True
print(3 < 4 or "Hola" < "Python" and 4 == 4)  # True
print(not (3 > 4))

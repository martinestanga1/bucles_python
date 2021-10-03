# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
numero_1 = int(input("Número 1:\n"))
numero_2 = int(input("Número 2:\n"))
operador = str(input("Operador:\n"))

operadores = ("+", "-", "*", "/", "**", "FIN")

# Prueba con condicional

'''if operador == operadores[0]:
        print("La suma es:", numero_1 + numero_2)
elif operador == operadores[1]:
        print("La resta es:", numero_1 - numero_2)
elif operador == operadores[2]:
        print("La multiplicación es:", numero_1 * numero_2)
elif operador == operadores[3]:
        print("La división es:", numero_1 / numero_2)
elif operador == operadores[4]:
        print("El exponente es:", numero_1 ** numero_2)
elif operador == operadores[5]:
        print("Fin de la operación.")
else:
        print("ERROR! Ingrese un dato válido.")'''

# Bucle
while operador == operadores[0]:
        print("La suma es:", numero_1 + numero_2)
        break
while operador == operadores[1]:
        print("La resta es:", numero_1 - numero_2) 
        break
while operador == operadores[2]:
        print("La multiplicación es:", numero_1 * numero_2)
        break
while operador == operadores[3]:
        print("La división es:", numero_1 / numero_2)
        break
while operador == operadores[4]:
        print("El exponente es:", numero_1 ** numero_2)
        break
fin = str(input("Ingresar la finalización de la operación:\n"))
while fin == operadores[5]:
        print("Fin de la operación.")
        break
if operador != operadores[0:5]:
        print("ERROR! Ingrese un operador válido.")
        



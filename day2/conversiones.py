"""""
edad = input("Dime tu edad")
print(type(edad))
ead = int (edad)
print(type(edad))
nueeva_edad = 1 + edad
print("tu nueva edad es"+nueeva_edad)

Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
num1 = 7.5
resul = int(num1)
print(type(resul))
Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
num2 = 10
result = float(num2)
print(type(result))

Práctica Formatear Cadenas 1
Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")


puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores + puntos_nuevos
print (f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

x=6
y=2
z=7

print(f"{x}mas {y} es igual a{x+y}")
print(f"{x}menos {y} es igual a{x-y}")
print(f"{x}por {y} es igual a{x*y}")
print(f"{x} dividido {y} es igual a{x/y}")


print(f"{x} dividido al piso de {y} es igual a {z//y}")
print(f"{x} modulo de  {y} es igual a {z%y}")
print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")
print(f"{x} la raiz cuadrada de {x} es igual a {x**0.5}")


redondeo con valor tipo int
valor = round(95.666666)
print(valor)
print(type(valor))


Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.

divicion = (10/3)
redondeo =  round(divicion,2)
print(redondeo)

valor = round(5**0.5,4)
print(valor)

"""""

'''''

usuario=input("Cual es tu nombre")
ventas=input("Cual es tu ventas")
ingreso = float(ventas)
porcerntaje =  (0.13)
print(f"el nombre seria{usuario} y su ventas serian {ventas} que tendria una ganancia  de:{porcerntaje*ingreso}")

'''








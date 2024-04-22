# VER LAS CONSIGNAS DE LOS EJERCICIOS EN EL ARCHIVO P2_2022.PDF

""" Ejercicio 3
num = int(input("ingrese un número: "))
print("el triple del número es: ", 3*num)
"""

""" Ejercicio 4
num = int(input("ingrese un número: "))
print("la mitad de ese número es: ", num/2)
"""

""" Ejercicio 5 
nota = int(input("ingrese una nota: "))
nota2 = int(input("ingrese una nota: "))
nota3 = int(input("ingrese una nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print("El promedio de las notas es: ", promedio)
"""

""" Ejercicio 6 
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = base*altura/2
print("El área del triángulo es: ", area)
"""

""" Ejercicio 7 
diametro = float(input("Ingrese el diámetro del círculo: "))
perimetro = diametro * 3.1416
area = 3.1416 * (diametro / 2)**2
print("El perímetro del círculo es ", perimetro, " y su área es ", area)
"""

""" Ejercicio 8 
primer_num = int(input("Ingrese un número: "))
segundo_num = int(input("Ingrese otro número: "))
division_entera = primer_num // segundo_num
resto_division = primer_num % segundo_num
print("La división entera es", division_entera, "y su resto es", resto_division)
"""

""" Ejercicio 9 
ancho = float(input("Ingrese el ancho de la pileta en metros: "))
alto = float(input("Ingrese el alto de la pileta en metros: "))
largo = float(input("Ingrese el largo de la pileta en metros: "))
volumen_pileta = ancho * alto * largo
cantidad_litros = volumen_pileta * 1000
print("La pileta tiene un volumen de", volumen_pileta, 
        "metros cúbicos y su cantidad de litros es", cantidad_litros)
"""

""" Ejercicio 10
ancho = float(input("Ingrese el ancho del terreno en metros: "))
largo = float(input("Ingrese el largo del terreno en metros: "))
area_terreno = ancho * largo
# Se usa 2.77 en la siguiente línea porque, haciendo regla de 3 simples, por 
# cada metro cuadrado se necesitan 2,7777 paneles ((100x100) x 1 : (60x60))
cantidad_paneles = area_terreno * 2.7777
print("La cantidad de paneles de pasto que se deben comprar para el terreno son", cantidad_paneles)
"""

""" Ejercicio 11 
producto1_nombre = input("Ingrese el nombre del primer producto: ")
producto1_precio_unitario = float(input("Ingrese el precio unitario del primer producto: "))
producto1_cantidad_comprada = int(input("Ingrese la cantidad comprada del primer producto: "))
subtotal_producto1 = producto1_precio_unitario * producto1_cantidad_comprada

producto2_nombre = input("Ingrese el nombre del segundo producto: ")
producto2_precio_unitario = float(input("Ingrese el precio unitario del segundo producto: "))
producto2_cantidad_comprada = int(input("Ingrese la cantidad comprada del segundo producto: "))
subtotal_producto2 = producto2_precio_unitario * producto2_cantidad_comprada

producto3_nombre = input("Ingrese el nombre del tercer producto: ")
producto3_precio_unitario = float(input("Ingrese el precio unitario del tercer producto: "))
producto3_cantidad_comprada = int(input("Ingrese la cantidad comprada del tercer producto: "))
subtotal_producto3 = producto3_precio_unitario * producto3_cantidad_comprada

total = subtotal_producto1 + subtotal_producto2 + subtotal_producto3

print("Nombre, subtotal")
print(producto1_nombre, ",", subtotal_producto1)
print(producto2_nombre, ",", subtotal_producto2)
print(producto3_nombre, ",", subtotal_producto3)
print("Total:", total)
"""

""" Ejercicio 12 
lado = float(input("Ingrese el lado del cuadrado en metros: "))
perimetro_cuadrado = lado*4
area_cuadrado = lado ** 2
print("El perímetro del cuadrado es ", perimetro_cuadrado, "metros",
      "y su área es", area_cuadrado, "metros cuadrados.")
"""

""" Ejercicio 14 
palabra1 = input('Ingrese una palabra: ')
palabra2 = input('Ingrese una palabra: ')
palabra3 = input('Ingrese una palabra: ')
print("Las iniciales de su palabras son", palabra1[0], palabra2[0], palabra3[0])
"""

""" Ejercicio 14 alternativa 
palabras = input("Ingrese un texto de 3 palabras: ")
palabras_separadas = palabras.split()
print("Las iniciales de su palabras son", palabras_separadas[0][0], palabras_separadas[1][0], palabras_separadas[2][0])
"""


""" Ejercicio 29 """
n1 = 124.25
n2 = "33.40"
n2 = float(n2)
division_entera = int( n1 // n2)
print("Division entera:", division_entera)


""" Ejercicio 5 
def cuantos_dias(mes):
    meses = [["Enero", 31],["Febrero", 28], ["Marzo", 31]]
    return meses[mes][1]

print(cuantos_dias(2))
"""

""" Ejercicio 7
def area_circulo(radio):
    return 3.1416*(radio**2)

def area_rectangulo(base, altura):
    return base*altura

def area_cuadrado(lado):
    return lado**2
"""
""" Ejercicio 8
def calculo_rebaja(precio_anterior, precio_rebajado):
    return 100 - (precio_anterior / precio_rebajado)*100

print(calculo_rebaja(90, 100))
"""

""" Ejercicio 9 
def calculo_nuevo_precio(precio_anterior, porcentaje_a_aumentar):
    return precio_anterior + (precio_anterior*porcentaje_a_aumentar)/100

print(calculo_nuevo_precio(80,10))
"""
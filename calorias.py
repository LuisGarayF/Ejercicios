# Ejercicio de Cálculo de calorías

import math

proteina = float(input("Ingrese la cantidad de proteinas : \n>"))
carbohidratos = float(input("Ingrese la cantidad de carbohidratos : \n>"))
grasa = float(input("Ingrese la cantidad de grasas : \n>"))

calorias = (proteina*4)+(carbohidratos*4)+(grasa*9)

print(f"La cantidad de calorías en el alimento es : {math.ceil(calorias)} kcal")



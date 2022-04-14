# Cálculo de velocidad de escape con unidades específicas

import math

print("---------------------------------------------\n>")
print("--------- Velocidad de escape ---------------\n>")
print("---------------------------------------------\n>")
print("\n>")

radio = float(input("Ingrese el valor de la medida del radio en km: \n>"))

print(f"r = {radio} Km")

g = float(input("Ingrese el valor de la constante g: \n>"))

print(f"g = {g} m/s2")

r = (radio*1000)

v = math.sqrt(r * g * 2) # Se realiza el cambio de unidad de km a mt

print(f"La velocidad de escape, según fórmula sería :\n> V = √rxgx2 = {v:.2f} m/s")
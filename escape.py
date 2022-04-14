# Cálculo de velocidad de escape

import math

print("---------------------------------------------\n>")
print("--------- Velocidad de escape ---------------\n>")
print("---------------------------------------------\n>")
print("\n>")

radio = float(input("Ingrese el valor de la medida del radio: \n>"))

g = float(input("Ingrese el valor de la constante g: \n>"))

v = math.sqrt(radio * g * 2)

print(f"La velocidad de escape es :\n> {v:.2f} m/s")

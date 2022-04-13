# Cálculo de rentabilidad y comparación de utilidades según año anterior

print("---------------------------------------------\n>")
print("--------- Comparación de rentabilidad -------\n>")
print("---------------------------------------------\n>")
print("------------ Instrucciones ------------------\n>")
print("---------------------------------------------\n>")
print("\n>")
print("Ingrese solamente números enteros o reales\n>")
print("\n>")

precio_suscripcion = float(input("Ingrese el precio de la suscripción actual: \n>"))

numero_usuarios = float(input("Ingrese el número de usuarios actuales: \n>"))

gastos_totales = float(input("Ingrese los gastos totales durante este periodo: \n>"))

utilidades = (precio_suscripcion * numero_usuarios) - gastos_totales

print(f"Las utilidades de este año son:\n> $ {utilidades:.0f}")

utilidades_anterior = float(input("Ingrese las utilidades del año anterior: \n>"))

print(f"Las utilidades del año anterior son:\n> $ {utilidades_anterior:.0f}")


if utilidades_anterior > utilidades:
    
    utilidades1 = utilidades_anterior-utilidades
    print(f"El año anterior fue más rentable con una diferencia de  : \n> $ {utilidades1} ")
    
elif utilidades_anterior < utilidades: 
     
    utilidades2 = utilidades-utilidades_anterior
    print(f"Actualmente es más rentable que el año anterior con una diferencia de  : \n> $ {utilidades2} ")
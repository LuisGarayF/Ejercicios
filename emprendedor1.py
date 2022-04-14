# Cálculo de rentabilidad según utilidades

print("-----------------------------------------\n>")
print("--------- Cálculo de rentabilidad -------\n>")
print("-----------------------------------------\n>")
print("------------ Instrucciones --------------\n>")
print("-----------------------------------------\n>")
print("\n>")
print("Ingrese solamente números enteros o reales\n>")
print("\n>")

precio_suscripcion = float(input("Ingrese el precio de la suscripción : \n>"))

numero_usuarios = int(input("Ingrese el número de usuarios : \n>"))

gastos_totales = float(input("Ingrese los gastos totales : \n>"))

utilidades = (precio_suscripcion * numero_usuarios) - gastos_totales

print(f"Las utilidades del negocio son : \n> $ {utilidades:.0f} ")
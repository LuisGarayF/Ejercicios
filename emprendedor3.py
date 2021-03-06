# Cálculo de rentabilidad y comparación de utilidades según año anterior

print("-----------------------------------------------------------------\n")
print("------------------- Comparación de rentabilidad -----------------\n")
print("-----------------------------------------------------------------\n")
print("------------------------- Instrucciones -------------------------\n")
print("-----------------------------------------------------------------\n")
print("\n")
print("Ingrese solamente números enteros o decimales separados por punto\n")
print("\n")

precio_suscripcion = float(input("Ingrese el precio de la suscripción actual: \n>"))

numero_usuarios = int(input("Ingrese el número de usuarios actuales: \n>"))

gastos_totales = float(input("Ingrese los gastos totales durante este periodo: \n>"))

utilidades = (precio_suscripcion * numero_usuarios) - gastos_totales

print(f"Las utilidades de este año son:\n> $ {utilidades:.0f}")

utilidades_anterior = float(input("Ingrese las utilidades del año anterior: \n>"))

print(f"Las utilidades del año anterior son:\n> $ {utilidades_anterior:.0f}")

print(f"La razón entre el año anterior con un valor de {utilidades_anterior} y el año actual {utilidades} es : {utilidades/utilidades_anterior}")
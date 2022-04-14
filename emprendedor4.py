# Cálculo de rentabilidad según utilidades para usuarios diferenciados

print("-----------------------------------------\n>")
print("--------- Cálculo de rentabilidad -------\n>")
print("-----------------------------------------\n>")
print("------------ Instrucciones --------------\n>")
print("-----------------------------------------\n>")
print("\n>")
print("Ingrese solamente números enteros o reales\n>")
print("\n>")

tipo_usuario = int(input(" Seleccione 1 o 2 dependiendo de la opción: \n> 1. Usuario Premium \n> 2. Usuario normal \n>"))

precio_suscripcion = float(input("Ingrese el precio de la suscripción : \n>"))

usuarios = int(input("Ingrese el número de usuarios : \n>"))

gastos_totales = float(input("Ingrese los gastos totales : \n>"))

utilidades = (precio_suscripcion * usuarios) - gastos_totales

utilidades_premium = (utilidades/2) + utilidades

# Decisiones 

if tipo_usuario == 1 :

    print(f"Las utilidades del negocio con usuarios premium son : \n> $ {utilidades_premium:.0f} ")


elif tipo_usuario == 2 :
    
   print(f"Las utilidades del negocio con usuarios normales son : \n> $ {utilidades:.0f} ") 
# Cálculo de rentabilidad según utilidades para usuarios diferenciados

print("-----------------------------------------\n>")
print("--------- Cálculo de rentabilidad -------\n>")
print("-----------------------------------------\n>")
print("------------ Instrucciones --------------\n>")
print("-----------------------------------------\n>")
print("\n>")
print("Ingrese solamente números enteros o reales\n>")

p = float(input("Ingrese el precio de la suscripción base : \n>"))

u_n = int(input("Ingrese el número de usuarios normales: \n>"))

u_p = int(input("Ingrese el número de usuarios premium: \n>"))

g_t = float(input("Ingrese los gastos totales : \n>"))

utilidades = ((p *( u_n + (u_p * 1.5)))- g_t)

print(f"Las utilidades del negocio serian : \n> $ {utilidades:.0f} ")
    



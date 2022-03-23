# Numeros

# Enteros

diez = 10

flotante = 12.4

print("La clase del numero", (diez) ," es :" ,(type(diez)))
print("La clase del numero", (flotante) ," es :" ,(type(flotante)))

# Potencias

print("La potencia de 2 elevado en 3 es : " , (2**3))


# Division

print(" 3 / 2 =" , (3/2))


print(" 3 / 2 su módulo entero es : " , (3//2))# Módulo solo muestra el resto entero de la division

#El resto de la division

print(" 3 / 2  su resto es : " , (3%2))

# Toma lo que el usuario inserta en la consola

edad = input("Ingrese su edad  : ") # imprime el mensaje y guarda lo que el usuario ingresa en edad

print("Su edad actual es : " + edad)

nueva_edad = int(edad) + 5 # Se transforma a entero por que el numero ingresado es un string

print("Su edad en 5 años será : " , nueva_edad)
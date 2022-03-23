n = int(input("Ingrese un número entero"))
m = int(input("Ingrese otro número entero"))
division = int(n/m)
coeficiente = n//m
resto = n%m
print("El resultado de la división entre "+ str(n) + " y "+ str(m) +" es : "+ str(division))
print("El coeficiente de la división entre "+ str(n)+" y "+ str(m) +" es : "+ str(coeficiente))
print("El resto de la división entre "+ str(n)+" y "+str(m) +" es : "+ str(resto))
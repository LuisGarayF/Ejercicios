print("------- CALCULO IMC --------------")
peso = int(input ("Ingrese su peso : "))
estatura = float(input ("Ingrese su estatura : "))
IMC = round(float(peso)/float(estatura)**2,2)
print ("Su IMC es : "+ str(IMC))
print("----------------------------------")
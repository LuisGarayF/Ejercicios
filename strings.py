# String o cadenas

myStr = "Hola mundo"

# print(dir(myStr))

# Funcion upper transforma todo en mayúsculas

print(myStr.upper())

# Funcion upper transforma todo en minúsculas

print(myStr.lower())

# Funcion transforma intercalando mayúsculas por minusculas y al contrario

print(myStr.swapcase())

# Funcion transforma la primera letra a mayúsculas

MyStr = "la primera letra cambia a mayúscula, pero la letra estaba en minúscula."

print(MyStr.capitalize())

# Funcion cambia un texto

print(MyStr.replace('primera', "segunda"))

# Métodos encadenados

print(MyStr.replace('primera', "segunda").upper())

# Contar carácter

print("La cantidad de veces que se repite la palabra letra es : ", (MyStr.count('letra')))
print("La oración tiene ", (MyStr.count(' ')), " espacios.")

# Empieza con?

print("La oración dentro del string comienza con la palabra primera? : ",(MyStr.startswith('primera')))
print("La oración dentro del string comienza con la palabra la? : ",(MyStr.startswith('la')))

# Termina con?

print("La oración dentro del string termina con punto? : ",(MyStr.endswith('.')))


# Dividir el string con split, separa por defecto con espacio

print(myStr.split())

# Separar con otro carácter como una coma

myStr2 = "Auto,Avión,Barco"

print("El nuevo string es : ",(myStr2))


print(myStr2.split(","))

# Separar a  partir de la letra o es sencible a las mayusculas y los acentos

print(myStr2.split("o"))

# Buscar un caracter especifico del string y arroja su posicion contando desde 0 es decir su indice

print("La posición de la primera letra o en la cadena [",myStr2,"] es : ",(myStr2.find("o")))

# Muestra el largo del string

print("El largo de la cadena [",myStr2,"] es : ",(len(myStr2)))

# Mostrar el indice de la letra especifica

print("El indice de la letra o de la cadena [",myStr,"] es : ",(myStr.index("o")))

# Mostrar si es un numero o si es alfanumerico

print("La cadena [",myStr,"] es un número? ",(myStr.isnumeric()))
print("La cadena [",myStr,"] es un alfanumérica? ",(myStr.isalpha()))

# Mostrar un caracter de un indice específico

print("En la cadena [",myStr,"] El indice selecionado es el N° 6 y es el caracter : "+(myStr[6]))

# Mostrar en sentido inverso

print("En la cadena [",myStr,"] El indice selecionado es el N° -5 y es el caracter : "+(myStr[-4]))

# Concatenacion se utiliza +

name = "Luis"

print("Mi nombre es " + name)

# Una variable dentro de un texto

print(f"Mi primer nombre es {name}")

print("Mi primer nombre con la funcion format es {0}". format(name))
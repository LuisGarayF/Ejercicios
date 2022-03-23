# Listas

lista1 = ["hola", 1, 1.18, True, [1,2,3]]
colors = ["red", "green", "blue"]

 #Se crea una tupla para crear la lista con doble (()) para pasar mas de 1 argumento
lista2 = list((1,2,3,4))

#print(lista2)

# Crear una lista por rango

r = list(range(1,111)) # Del 1 al 110

#print(r)

# el metodo dir te dice que se puede hacer con un dato especifico

#print(dir(colors))

# print(colors[1]) #Imprime el elemento en la posición 1 que es green

# Si string esta en una lista por rango

print("El valor greeen esta dentro de la lista colors? ",('green' in colors))

# reasignacion 

print(colors)

colors[1] = 'yellow'

print(colors)

# metodos

colors.append('violet')
print(colors)
 # Se agregan nuevos elementos al final de la lista
colors.extend(['orange','yellow']) # Solo se pueden pasar tuplas por eso llevan corchetes

print(colors)

# Inserta un elemento en la posición 1 con valor black sin sobreescribir el anterior
colors.insert(1, 'black')

print(colors)

# Inserta un elemento en la última posición de la lista con valor pink sin sobreescribir el anterior

colors.insert(len(colors), 'pink') # se utiliza la longitud

print(colors)

# min 1.53.47
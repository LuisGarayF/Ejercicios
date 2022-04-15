# Lista puede contener distintos tipos de datos

varios = [False, True, 5.5, 'hola', 1]

animales = ["perro", "gato", "mono"]

print(f"La lista varios es : {varios}")
print(f"La lista animales es : {animales}")
print(f"muestra los datos del indice 0 al 3 sin iuncluir el indice 3 {varios[0:3]}") 
print("================================================================================= \n")


# Diccionario, se puede buscar en vez de indice con key directamente

cliente ={'nombre':'Urzula', 'apellido': 'Vergara', 'rut' : '16.116.116-6'}

diccionario = {"key1": 1, "key2": 2, "key3": 3}

print(f"El diccionario es : {diccionario}")
print(f"Los datos del cliente son : {cliente}")

print(cliente.items())
print(cliente.values())
print(cliente.keys())
print(f"El rut del cliente es : {cliente.get('rut')}")

print("================================================================================= \n")

# Set no tiene indice y entrega los datos desordenados, además no permite datos iguales

frutas ={'banana','platano','plátano','manzana', 'platano', 'durazno'} 

print(f"Las frutas son : {frutas}")

frutas_corregidas = frutas.remove('platano')

print(f"Eliminando las frutas repetidas quedaría : {frutas_corregidas}")#elimina todo al ser un set y un remove

print("================================================================================= \n")

# Tupla tambien considera indices y sus respectivas propiedades de los indices negativos decir ir en reversa

ciudades = ('Santiago', 'Valparaiso', 'Rancagua')

print(f"Algunas cuidades de Chile son : {ciudades}")

ciudades_corregidas = ciudades.remove('Rancagua') # aqui se demuestra que los datos son inmutables en una tupla

print(f"Corrijo Rancagua no existe : {ciudades_corregidas}")

print("================================================================================= \n")
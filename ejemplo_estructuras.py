# Almacenados a varios clientes en una tabla
# Ordenenes de compra relacionadas a cada cliente
# Obtener un cliente y todas sus ordenes de compra que a efectuado a lo largo de un mensaje

cliente = {
    'rut' : '76.233.638.4',
    'nombre': 'Leonor',
    'apellido': 'Lloyd',
    'direccion': {
        'Calle':'Radomiro Tomic',
        'Numero': '232',
        'Depto': '301',
        'Comuna': 'Maipú'
        },
    'ordenes': [
        {
            'código': '123456',
            'producto': '7645498',
            'precio': '500'
        },
        {
            'código': '456789',
            'producto': '978544645',
            'precio': '1000'
        },
        {
            'código': '123456',
            'producto': '7645498',
            'precio': '500'
        }
    ]
}


print(cliente)

print("=========================================================================================================================================================\n")
print(cliente.get('direccion'))
print("=========================================================================================================================================================\n")
print(cliente.get('ordenes')[2].get('producto')) # Obtiene el producto de una orden especifica
print("=========================================================================================================================================================\n")
print(f" $ {cliente.get('ordenes')[1].get('precio')}") # Obtiene el producto de una orden especifica
print("=========================================================================================================================================================\n")

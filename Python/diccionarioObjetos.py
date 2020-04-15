#A los OBEJTOS se los llama DICCIONARIO

carritoCompras = {
    'name': 'book',
    'cantidad': 3,
    'precio': 4.99
}

persona = {
    'first_name': 'Matias',
    'last_name': 'Martinez',
    'age': 25
}

#print(type(persona))
#print(dir(persona))

print(persona.keys())
print(persona.items())

productos = [
    {
        'nombre': 'libro',
        'precio': 'mucho'
    },
    {
        'nombre': 'librote',
        'precio': 'menor'
    }
]

print(productos)
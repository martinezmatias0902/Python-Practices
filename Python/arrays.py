
#Esto es una CLASE
class cat(): 
    name = 'Jason'
    hobbies = ['music', 'programming', 'games']
    job = 'Software Developer'

gatosObjeto = cat() 
print ('Tu nombre es ', gatosObjeto.name)
print ('Tu Hobbie favorito es ', gatosObjeto.hobbies[1])

# Esto son ARRAYS, que en Python son llamados Listas/List

lista = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']
r = list(range(1,21))
print(r)

#Estos son TUPLES, parecido a las listas pero no se pueden cambiar, inmutables

tupla = (1, 2, 3)
print(tupla)
y = tuple((1,2,3))
print(y)

#Estos son SET, es una colección desordenada sin indices.

mira = {'Red', 'Green', 'Blue'}
print(type(mira))
print(mira)
print('Red' in mira)
mira.add('Violet')
print(mira)

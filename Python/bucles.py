
comidas = ['apples', 'bread', 'cheese', 'milk', 'bananas']

for comida in comidas:
    print(comida)

print('-------------------1')

for comida in comidas:
    if comida == 'cheese':
        print('No te olvides del queso')
    print(comida)

print('-------------------2')

for comida in comidas:
    if comida == 'cheese':
        break
    print(comida)


print('-------------------3')

for comida in comidas:
    if comida == 'cheese':
        continue
    print(comida)

print('-------------------4')

for number in range(1, 11):
    print(number)

print('-------------------5')

for letra in 'Hello':
    print(letra)

print('-------------------6    WHILE')

count = 4

while count <= 10:
    print(count)
    count = count + 1                       #No olvidar sumar "count" porque sino será un bucle infinito

#Ejercicio 1
print('--------------------------EJERCICIO 1-----------------------------------')
print('Sacar IVA')
precioA = int(input('Ingrese un número: '))
precioB = int(input('Ingrese otro número: '))
IVA = 1.21
print('El precio final es: ', (precioA + precioB) * IVA)

#Ejercicio 2
print('--------------------------EJERCICIO 2-----------------------------------')
print('Sacar promedio de números')
n1 = int(input('1) Ingrese un numero: '))
n2 = int(input('2) Ingrese un numero: '))
n3 = int(input('3) Ingrese un numero: '))
prom = (n1 + n2 + n3) / 3
print('El promedio de sus numeros es: ', prom)

#Ejercicio 3
print('--------------------------EJERCICIO 3-----------------------------------')
print('Imprimir el número más alto')
N1 = int(input('Ingrese un número RANDOM: '))
N2 = int(input('Ingrese otro número CUSTOM: '))
if N1 > N2:
    print('El número mayor es: RANDOM ', N1)
elif N1 == N2:
    print('Los números son iguales')
else:
    print('El número mayor es: CUSTOM ', N2)

#Ejercicio 4
print('--------------------------EJERCICIO 4-----------------------------------')
print('Será par o impar??')
nParOimpar = int(input('Ingrese un número y le diremos si es PAR o IMPAR: '))
if nParOimpar % 2 == 0:
    print('El número ingresado es par! ', nParOimpar)
if nParOimpar % 2 != 0:
    print('El número ingresado es impar!', nParOimpar)

#Ejercicio 5
print('--------------------------EJERCICIO 5-----------------------------------')
num = int(input('Ingrese un número negativo: '))
while num >= 0:
    print('El numero ingresado es positivo')
    num = int(input('Ingrese otro número: '))
    if num < 0:
        print('El número ingresado es negativo, ahora puede dejar el programa..... Be Happy')
    




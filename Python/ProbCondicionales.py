print('--------------------------EJERCICIO 1-----------------------------------')
from random import randint, uniform,random                  #importo para crear numeros random
total = int(input('Ingrese el total de su Compra: '))
numero = randint(0,100)                                  #imprime número random
print('Su número aleatorio es: ', numero)

if numero < 74:
    descuento15 = (15 * total) / 100
    print('Su descuento del 15% es: .... ', descuento15)
elif numero >= 74:
    descuento20 = (20 * total) / 100
    print('Su descuento del 20% es: .... ', descuento20)

print('--------------------------EJERCICIO 2-----------------------------------')
def pulsacionesF():
    pulsa = (220 - edad) / 10
    print('Por cada 10 segundos de ejercicio aeróbico sus pulsaciones femeninas deben ser de: ', pulsa)
def pulsacionesM():
    pulsa = (210 - edad) / 10
    print('Por cada 10 segundos de ejercicio aeróbico sus pulsaciones masculinas deben ser de: ', pulsa)
   

sexo = input('Ingrese su sexo, Masculino o Femenino?: ')
edad = int(input('Indique su edad: '))

if sexo == 'Masculino':
    pulsacionesM()
else:
    pulsacionesF()

print('--------------------------EJERCICIO 3-----------------------------------')
cliente = int(input('Bienvenido a nuestra aseguradora! Ingrese su monto de seguro: '))
print('Si el monto ingresado es menor a $50.000 la cuota será del 3%, sino del 2%')
print('Calculando su cuota ... ... ...')

if cliente < 50000:
    cuotaMayor = (3 * cliente) / 100
    print('El valor de su cuota 3% es de: $', cuotaMayor)
elif cliente >= 50000:
    cuotaMenor = (2 * cliente) / 100
    print('El valor de su cuota 2% es de: $', cuotaMenor)

print('--------------------------EJERCICIO 4-----------------------------------')
print('El costo de las materias es de $1000 cada una')
materias = int(input('A cuántas materias desea anotarse?: '))
matricula = (materias * 1000) * 1.21
print('El valor total de su matricula es de (IVA incluido): $', matricula)
promedio = int(input('Ingrese su promedio (0 - 10) final para calcular descuentos o becas sobre la matricula: '))

if promedio >= 9:
    matricula_sinIVA = (materias * 1000)
    descuento = matricula_sinIVA * 0.30
    finalCuota = matricula_sinIVA - descuento
    print('Su matricula total a pagar (becado) es de:  $', finalCuota)
else:
    print('Su matricula total a pagar es de:  $', matricula)


print('--------------------------EJERCICIO 5-----------------------------------')
sueldo = int(input('Ingrese su sueldo:  $'))
print('El programa SAR establece que se debe depositar el 5% de su salario en nuestras cuentas')
sar = sueldo * 0.05
print('Depositaremos de su sueldo la cantidad de:  $', sar, ' pesos')
pregunta = input('Desea depositar adicionalmente un porcentaje de su salario? Si/no: ')

if pregunta == 'si':
    extra = int(input('Cuánto desea depositar?: '))
    sueldo_final = sueldo - sar - extra
    print('A fin de mes su sueldo quedará en:  $', sueldo_final)
else:
    sueldo_no_extra = sueldo - sar
    print('Su sueldo será de:  $', sueldo_no_extra)

print('--------------------------EJERCICIO 6-----------------------------------')
print('100 hectareas es igual a 1.000.000 mts2')
superficie = int(input('Ingrese cantidad de hectareas del terreno (1h = 10.000mts): '))
pinos_hectarea = 8000
oyameles_hectarea = 10000
cedro_hectarea = 5555.55

if superficie > 100:
    sup_pinos = superficie * 0.70
    sup_oyamel = superficie * 0.20
    sup_cedro = superficie * 0.10
    sembrar_pino = pinos_hectarea * sup_pinos
    sembrar_oyamel = oyameles_hectarea * sup_oyamel
    sembrar_cedro = cedro_hectarea * sup_cedro
    print('Plantaremos la siguiente cantidad de PINOS:  ',sembrar_pino)
    print('Plantaremos la siguiente cantidad de OYAMELES:  ',sembrar_oyamel)
    print('Plantaremos la siguiente cantidad de CEDROS:  ',sembrar_cedro)
elif superficie <= 100:
    sup_pinos = superficie * 0.50
    sup_oyamel = superficie * 0.30
    sup_cedro = superficie * 0.20
    sembrar_pino = pinos_hectarea * sup_pinos
    sembrar_oyamel = oyameles_hectarea * sup_oyamel
    sembrar_cedro = cedro_hectarea * sup_cedro
    print('Plantaremos la siguiente cantidad de PINOS:  ',sembrar_pino)
    print('Plantaremos la siguiente cantidad de OYAMELES:  ',sembrar_oyamel)
    print('Plantaremos la siguiente cantidad de CEDROS:  ',sembrar_cedro)

print('--------------------------EJERCICIO 7-----------------------------------')
compra = int(input('Cuantás computadoras desea?: '))
computadoras = 1600
sub_total = compra * computadoras

if compra < 5:
    print('El sub total de su compra es:  $', sub_total)
    descuento = sub_total * 0.10
    print('Tiene un descuento del 10%: ', descuento)
    total = sub_total - descuento
    print('Total a pagar:  $', total)
elif compra >= 5 and compra < 10:
    print('El sub total de su compra es:  $', sub_total)
    descuento = sub_total * 0.20
    print('Tiene un descuento del 20%: ', descuento)
    total = sub_total - descuento
    print('Total a pagar:  $', total)
else:
    print('El sub total de su compra es:  $', sub_total)
    descuento = sub_total * 0.40
    print('Tiene un descuento del 40%: ', descuento)
    total = sub_total - descuento
    print('Total a pagar:  $', total)

print('--------------------------EJERCICIO 8-----------------------------------')
listo = input('Esta listo para jugar? si/no: ')

if listo == 'si':
    print('Primera Pregunta:')
    colon = input('Colón descubrió América?:  ')
    if colon == 'si':
        print('Muy bien! Segunda Pregunta: ')
        mexico = input('La independencia de México fue en el año 1810?:  ')
        if mexico == 'si':
            print('Excelente sigue así! Tercera Pregunta: ')
            doors = input('The Doors fue un grupo de rock Americano?:  ')
            if doors == 'no':
                print('EXCELEEENTE, ERES EL GANADOOOR!')
            else:
                print('Perdiste....Programa terminado ... ... ...')
        else:
            print('Perdiste....Programa terminado ... ... ...')
    else:
        print('Perdiste....Programa terminado ... ... ...')
else:
    print('Perdiste....Programa terminado ... ... ...')

print('--------------------------EJERCICIO 9-----------------------------------')
marca = input('Su producto es de marca YNOS o SONY?: ')
precio = int(input('Ingrese el Precio del producto:  $'))

if precio >= 2000:
    descuento = precio * 0.10
    print('Usted a obtenido un descuento del 10%...: ', descuento)
    precio_sinIVA = precio - descuento
    print('El Subtotal es:  $', precio_sinIVA)
    precio_final = precio_sinIVA * 1.21
    print('El monto total a pagar es:  $', precio_final, ' Con IVA incluido')
    if marca == 'YNOS':
        descuento = precio * 0.10
        precio_sinIVA = precio - descuento
        precio_final = precio_sinIVA * 1.21
        precio_YNOS = precio_final * 1.05
        print('Como su producto es de marca YNOS a accedido a un beneficio exclusivo, total a pagar:  $', precio_YNOS)
else:
    precio_final = precio * 1.21
    print('El monto total a pagar es:  $', precio_final, ' Con IVA incluido')



# print('--------------------------EJERCICIO 10-----------------------------------')
# print('--------------------------EJERCICIO 11-----------------------------------')
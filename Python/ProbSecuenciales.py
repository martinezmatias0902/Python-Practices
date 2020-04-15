print('--------------------------EJERCICIO 1-----------------------------------')
capital_depositado = int(input('Ingrese capital a depositar en el Banco: '))
interes_mensual = 0.02
def Bco(dinero, interes):
    total = dinero * interes
    print('Sus ganancias en un Mes serán de: ', total)
    print('Total a retirar: ', total + capital_depositado)
Bco(capital_depositado, interes_mensual)

print('--------------------------EJERCICIO 2-----------------------------------')
sueldo_base = int(input('Ingrese su Sueldo: '))
ventas_logradas = int(input('Ingrese ventas logradas: '))
comision = ventas_logradas * (sueldo_base * 0.10)
print('Su comisión es de: ', comision)
print('Su sueldo TOTAL es de: ', sueldo_base + comision)

print('--------------------------EJERCICIO 3-----------------------------------')
calificacion_uno = int(input('Ingrese nota primer parcial: '))
calificacion_dos = int(input('Ingrese nota segundo parcial: '))
calificacion_tres = int(input('Ingrese nota tercer parcial: '))
examen_final = int(input('Cual fue su nota examen final?: '))
trabajo_practico = int(input('Nota trabajo práctico: '))

def nota_final():
    calificaciones = (calificacion_uno + calificacion_dos + calificacion_tres) / 3
    tp = 15 * trabajo_practico / 100
    test = 30 * examen_final / 100
    notas = 55 * calificaciones / 100
    print('15% de TP: ', tp)
    print('30% de Final: ', test)
    print('55% calificaciones: ', notas)
    resultado = (tp + test + notas)
    print('Calificación final: ', resultado)

nota_final()


print('--------------------------EJERCICIO 4-----------------------------------')
hombres = int(input('Ingrese cantidad total de hombres: '))
mujeres = int(input('Ingrese cantidad total de mujeres: '))
total = hombres + mujeres
porcentajeH = (hombres * 100) / total
porcentajeM = (mujeres * 100) / total
print('El porcentaje de Hombres es:  %', porcentajeH, ' Y el porcentaje de Mujeres es:  %', porcentajeM)

print('--------------------------EJERCICIO 5-----------------------------------')
edad = int(input('Ingrese su edad: '))
pulsaciones = (220 - edad)/10
print(pulsaciones)

print('--------------------------EJERCICIO 6-----------------------------------')
socio_uno = int(input('Ingrese cantidad invertida socio uno: '))
socio_dos = int(input('Ingrese cantidad invertida socio dos: '))
socio_tres = int(input('Ingrese cantidad invertida socio tres: '))
total_inv = socio_uno + socio_dos + socio_tres

porcentaje_uno = (socio_uno * 100) / total_inv
porcentaje_dos = (socio_dos * 100) / total_inv
porcentaje_tres = (socio_tres * 100) / total_inv
print('Este es el porcentaje invertido por socio: ')
print('1) Socio uno:  %', float(porcentaje_uno))
print('2) Socio dos:  %', float(porcentaje_dos))
print('3) Socio tres:  %', float(porcentaje_tres))

print('--------------------------EJERCICIO 7-----------------------------------')

def analisis():
    nota = int(input('Ingrese la nota de su examen en Análisis: '))
    trabajo = int(input('Ingrese nota primer TP: '))
    trabajoDos = int(input('Ingrese nota segundo TP: '))
    trabajoTres = int(input('Ingrese nota tercer TP: '))
    test = (90 * nota) / 100
    print('El 90% de su examen final es:   %', test)
    tp = (trabajo + trabajoDos + trabajoTres) / 3
    tpfinal = (10 * tp) / 100
    print('El 10% del promedio de sus TPs es:  %', tpfinal)
    nota_final = test + tpfinal
    print('Su nota final en Análisis es: ', nota_final)
    
    return nota_final


def algebra():
    nota = int(input('Ingrese la nota de su examen en Álgebra: '))
    trabajo = int(input('Ingrese nota primer TP: '))
    trabajoDos = int(input('Ingrese nota segundo TP: '))
    test = (80 * nota) / 100
    print('El 80% de su examen final es:   %', test)
    tp = (trabajo + trabajoDos) / 2
    tpfinal = (20 * tp) / 100
    print('El 20% del promedio de sus TPs es:  %', tpfinal)
    nota_final = test + tpfinal
    print('Su nota final en Álgebra es: ', nota_final)
     
    return nota_final

def programacion():
    nota = int(input('Ingrese la nota de su examen en Programacion: '))
    trabajo = int(input('Ingrese nota primer TP: '))
    trabajoDos = int(input('Ingrese nota segundo TP: '))
    trabajoTres = int(input('Ingrese nota tercer TP: '))
    test = (85 * nota) / 100
    print('El 85% de su examen final es:   %', test)
    tp = (trabajo + trabajoDos + trabajoTres) / 3
    tpfinal = (15 * tp) / 100
    print('El 15% del promedio de sus TPs es:  %', tpfinal)
    nota_final = test + tpfinal
    print('Su nota final en Programacion es: ', nota_final)
     
    return nota_final


totally = analisis()
totalDos = algebra()
totalTres = programacion()

promedio = (totally + totalDos + totalTres) / 3

print('El promedio de sus tres materias es: ', promedio)
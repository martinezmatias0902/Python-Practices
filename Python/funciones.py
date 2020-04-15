#print()
#type()
#dir()

def matias(x):                         #esto es una definición de funcion "def"
    print('Hola ' + x)

matias('Matute')

print('-------------------1')

def suma(num):
    num = num + 1
    print(num)

suma(2)

print('-------------------2')

def alta_suma(num, num_dos):
    if num == 10:
        x = num * num_dos
        print(x)
    elif num_dos == 20:
        y = num / num_dos
        print(y)
    else:
        z = num + num_dos
        print(z)

alta_suma(10, 5)
alta_suma(100, 20)
alta_suma(654, 456)

print('-------------------3')
#---------------------------lambda-------------- Será cómo la arrow function? =>

add = lambda numeroUno, numeroDos: numeroUno + numeroDos

print(add(5, 105))

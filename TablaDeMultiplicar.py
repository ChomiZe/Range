#Desarrollar un programa que muestre en pantalla la tabla de multiplicar de un numero cualquiera que sea ingresado desde teclado
#Requerimientos
#Utilizar ciclo o bucle for
#la tabla debe tener multiplicaciones desde 0 hasta 10

num = int(input("Que tabla de multiplicar deseas ver? ingresa un numero: "))

print(f'La tabla del {num} es:')
for indice in range(1, 11):
    print(f'{num} x {indice} = {num * indice}')
# crea un porgrama que sea capaz de solicitarte un numero
# y se encargue de imprimir su tabla de multiplicar entrw el 1 y el 10.
# Debe visualizarse 

numero=int(input("Ingrese su número: "))

for x in range(1,11):
    resultado=numero*x
    print(numero,"x",x,"=",resultado)
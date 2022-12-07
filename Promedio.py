print("promedio de N números")    
limite = int(input("Digite el total de datos: "))
suma = 0
for i in range(1,limite+1):
    num = float(input(f"Digite el valor {i}: "))
    suma = suma + num

print("El promedio es: {0:.2f}".format(suma/limite))     

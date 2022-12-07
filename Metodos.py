def saludar():
    print("Hola mundo!")
def CalcularDoble(num):
    x = num*2
    print(x)
def triplicar(num):
    x = num*3
def menu():
    print("LLamada a la función saludar: ")
    saludar()
    num=int(input("ingrese un valor numerico para x: "))
    print("Llamada a la funcion CalcularDoble")
    print("El doble de ",num," es: ")
    CalcularDoble(num) 
    print("El valor original de x es: ",num)
    print("Llamada a la función triplicar")
    print("El nuevo valor de ",num, " es: ")
    triplicar(num)
menu()    
        


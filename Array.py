import random

A=[]
for i in range(0,10):
    x=random.randint(0,100)
    A.append(x)
print("Los numeros del arreglo son: ") 
print(A)
print("\n")
  
for i in reversed(A):
    print("Los numeros en orden inverso:",i," ", end="\n") 

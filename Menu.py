def menu():
    print("Menu de recomendaciones")
    print(" 1. Literatura")
    print(" 2. Cine")
    print(" 3. Música")
    print(" 4. Videojuegos")
    print(" 5. Salir")
def MenuDeLiteratura():    
    print("Lecturas recomendables")
    print("Esperándolo a Tito y otros cuentos de fúbol (Eduardo Sacheri)")
    print("El juego de Ender (Orson Scott Card)")
    print("El sueño de los héroes(Adolfo Bioy Casares)")

def MenuDeCine():    
    print("Películas recomendables ")
    print("Matrix (1999)")
    print("El último samuray (2003)")
    print("Cars(2006")
    
def MenuDeMusica():
    print("Discos recomendables ")
    print("Despedazado por mil partes (La Renga, 1996)")
    print("Búfalo (La Mississippi, 2008)")
    print("El sueño de los héroes(Adolfo Bioy Casares)")  
    
def MenuDeJuegos():    
    print("Videojuegos clásicos recomendables ")
    print("Día del tentáculo (LucasArts, 1993")
    print("Terminal Velocity (Terminal Reality/3D Realms, 1995)")
    print("Death Rally (Remedy/Apogee, 1996)")  
    
def MenuSalir():          
    print("gracias, vuelva pronto") 

opc = 0

while opc != 5:

    menu()
    opc = int(input("Ingrese la opción que desea: "))

    if opc == 1:
        MenuDeLiteratura()
        
    elif opc == 2:
        MenuDeCine() 

    elif opc == 3:
        MenuDeMusica()

    elif opc == 4:
        MenuDeJuegos()

    elif opc == 5:
        MenuSalir()
    else:
        print("Opción incorrecta")        




def Menu():
    print("Bienvenido a Historial BingBong")
    print("1.Agregar página al historial")
    print("2.Ver todo el historial")
    print("3.Buscar en el historial")
    print("4.Eliminar elemento más antiguo del historial")
    print("5.Salir del historial")
def Del(History):
    while 0 != 1:
        check = input(f"Está seguro de que desea eliminar el elemento {History[0]}?(S/N)")
        if check.upper() == "S":
            print(f"El elemento {History[0]} se eliminado con exito")
            print(" ")
            return History[1:]
        elif check.upper() == "N":
            print("Regresando al menú principal")
            input(" ")
            return History
        else:
            print("La opcción seleccionada no es valida")
def Find(History,Look):
    count = -1
    cont = 0
    for name in History:
        if name == Look:
            count = cont
        cont = cont + 1
    return count
def Show(History):
    cont = 1
    for name in history:
        print(f"Página: {cont}")
        print(name)
        print(" ")
        cont = cont + 1
def In(History):
    while 0 != 1:
        print("Ingreso de páginas al historial")
        print("(Presione X en cualquier momento para regresar al menu)")
        name = input("Ingrese el nombre de la página: ")
        if name == "X":
            print("Regresando al Menu")
            input(" ")
            print(" ")
            return History
        else:
            history.append(name)
            print("La página se a registrado correctamente.")
            input(" ")
            while 0 != 1:
                check = input("Desea agregar otra página? (S/N)")
                if check.upper() == "S":
                    break
                elif check.upper() == "N":
                    print("Regresando al menú principal")
                    exit1 = 1
                    input(" ")
                    return History
                else:
                    print("La opcción seleccionada no es valida")
allow = False
exit = 0
history = []
while allow == False:
    Menu()
    exit1 = 0
    opt = input("Ingrese la opción que desee: ")
    print(" ")
    match opt:
        case "1":
            history = In(history)
        case "2":
            if len(history) > 0:
                Show(history)
            else:
                print("Aún no hay ningún dato en el historial")
        case "3":
            if len(History) > 0:
                look = input("Ingrese la página que desea encontrar: ")
                find = Find(history,look)
                if find == -1:
                    print(f"La página {look} no existe dentro del historial")
                else:
                    print(f"Se a encontrado la página {look} en la posición {find} del historial")
            else:
                print("Aún no hay ningún dato en el historial ")
        case "4":
            if len(history) > 0:
                history = Del(history)
            else:
                print("Aún no hay ningún dato en el historial")
        case "5":
            while allow == False:
                check = input("Está seguro de que desea salir del programa? (S/N): ")
                if check.upper() == "S":
                    print("Gracias por utilizar el programa")
                    exit = 1
                    break
                elif check.upper() == "N":
                    print("Regresando al menú principal")
                    input(" ")
                    break
                else:
                    print("La opcción seleccionada no es valida")
        case _:
            print("La opción seleccionada no es valida")
    if exit == 1:
        break
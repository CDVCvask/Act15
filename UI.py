def Menu():
    print("Bienvenido a Historial BingBong")
    print("1.Agregar página al historial")
    print("2.Ver todo el historial")
    print("3.Buscar en el historial")
    print("4.Eliminar elemento más antiguo del historial")
    print("5.Salir del historial")
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
            while 0 != 1:
                print("Ingreso de páginas al historial")
                print("(Presione X en cualquier momento para regresar al menu)")
                name = input("Ingrese el nombre de la página: ")
                if name == "X":
                    print("Regresando al Menu")
                    input(" ")
                    print(" ")
                    break
                else:
                    history.append(name)
                    print("La página se a registrado correctamente.")
                    input(" ")
                    while 0!= 1:
                        check = input("Desea agregar otra página? (S/N)")
                        if check.upper() == "S":
                            break
                        elif check.upper() == "N":
                            print("Regresando al menú principal")
                            exit1 = 1
                            input(" ")
                            break
                        else:
                            print("La opcción seleccionada no es valida")
                if exit1 == 1:
                    break
        case "2":
            cont = 1
            if len(history) > 0:
                for name in history:
                    print(f"Página: {cont}")
                    print(name)
                    print(" ")
                    cont = cont + 1
            else:
                print("Aún no hay ningún dato en el historial")
        case "3":
            print("3")
        case "4":
            print("4")
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
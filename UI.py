def Menu():
    print("Bienvenido a Historial BingBong")
    print("1.Agregar página al historial")
    print("2.Ver todo el historial")
    print("3.Buscar en el historial")
    print("4.Eliminar elemento más antiguo del historial")
    print("5.Salir del historial")
allow = False
exit = 0
while allow == False:
    Menu()
    opt = input("Ingrese la opción que desee: ")
    print(" ")
    match opt:
        case "1":
            while 0 != 1:
                print("Ingreso de páginas al historial(Presione X para regresar al menu)")
        case "2":
            print("2")
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
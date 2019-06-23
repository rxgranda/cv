import funciones as fun
opcion=""
while opcion!="3":
    print("Menu")
    print("1 Myriam")
    print("2 Paola")
    print("3 salir")
    print("---------------")

    opcion=input("Ingrese una opcion: ")
    if opcion=="1":
        print("**********")
        fun.holaMyriam()
        print("**********")
    elif opcion=="2":
        print("**********")
        fun.holaPaola()
        print("**********")
    elif opcion=="3":
        print("Bye")
    else:
        print("Opcion Incorrecta")

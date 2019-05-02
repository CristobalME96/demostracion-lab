Users = []
Pass = []
option = 0
while option != 3:
    print("1) Registrarse\n2) Iniciar sesion\n3) Salir")
    option = int(input())
    if option == 1:
        Users.append(input("Elija un nombre de usuario: "))
        Pass.append(input("Elija una contraseña: "))
    if option == 2:
        validator = False
        user_login = input("Ingrese su usuario: ")
        for i in range(len(Users)):
            if Users[i] == user_login:
                pass_login = input("ingrese su contraseña: ")
                validator = True
                if Pass[i] == pass_login:
                    print("Bienvenido!")
                else:
                    print("Contraseña invalida")
            if i + 1 == len(Users) and validator == False:
                print("El usuario ingresado no existe, debe registrarse")
print("Adios")

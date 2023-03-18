while True:

    menu = """Bienvenio al registro de usuario, llene los campos que se sostieneque se sostiene y seleccione un numero del 1 al 3:
    [1]Digitar su Nombre
    [2]Digitar su Edad
    [3]Digitar su Correo
    [4]salir
    """

    print(menu)
    opcion = input('Entre a la opcion 1,2 o 3: ')
    if opcion == '1':
        while True:
            nombre = input('Digite su Nombre: ')
            if nombre.isalpha():
                print('Su nombre es: ',nombre)
                break
            else:
                print('Su nombre esta mal digitado')

            opcion = input('Entre a la opcion 1,2 o 3: ')


    elif opcion == '2':
        while True:
            edad = input('Digite su edad: ')
            if edad.isdigit():
                print('Su nombre es: ',edad)
                break
            else:
                print('Su edad esta mal digitada')


    elif opcion == '3':
        while True:
            correo = input('Digite su correo: ')
            if correo.find('@')==0 and correo.find('.')>=0:
                print('Su nombre es: ',correo)
                break
            else:
                print('Su correo no existe')

    elif opcion == '4':
        exit()

      


        

def principal():
    print("\nSISTEMA QUE REGISTRA USURIOS DE LA OFICINA\n")
    lista = [] #Lista vacia para objetos de tipo Usuario
    recibir_datos(lista) #Funcion para recibir datos
    buscar_usuario(lista) #Funcion para buscar usuario


def recibir_datos(lista):
    print("Ingreso de usuarios\n")
    num_usuarios = int(input("Ingrese el numero de usuarios a insertar: "))

    for x in range(num_usuarios):
        nombre = str(input("\nIngrese nombre de usuario: "))
        correo = str(input(f"Ingrese correo de {nombre}: "))
        lista.insert(x, usuario(nombre, correo))# Inserta un usuario en lista


def buscar_usuario(lista):
    print("\n\n--------BUSCAR USUARIO------")
    print("Tipos de Busqueda:\n"
          "1. Por nombre\n"
          "2. Por correo")

    while 1:
        opcion = int(input("Ingrese numero de opcion: "))
        if opcion == 1:
            nom = str(input("Ingrese nombre: "))
            usr = buscar(opcion, nom, lista) #Buscar por nombre
            break
        if opcion == 2:
            correo = str(input("Ingrese correo: "))
            usr = buscar(opcion, correo, lista) # Buscar por correo
            break
        else:
            print("Opcion Incorrecta, Intente de nuevo")

    if(type(usr) == usuario):
        print("\n---Datos Encontrados ---")
        print(f"Usuario= {usr.getNombre}  Contraseña= {usr.getCorreo}")
    else:
        print(usr) # Imprime mensaje si no encontró usuario


def buscar(opcion, dato, lista):

    encontrado = 0

    for x in range(len(lista)):
        if(opcion == 1):
            if(dato == lista[x].getNombre):
                encontrado = 1
                return lista[x] # Retorna usuario deseado
        else:
            if(dato == lista[x].getCorreo):
                encontrado = 1
                return lista[x] # Retorna usuario deseado

    if(encontrado == 0): #Si no se encuentra usuario deseado
        return "Lo sentimos, usuario no encontrado :("


class usuario():
    #Constructor y atributos privados
    def __init__(self, nombre, correo):
        self.__nombre = nombre 
        self.__correo = correo

    # Getters
    @property
    def getNombre(self):
        return self.__nombre

    @property
    def getCorreo(self):
        return self.__correo


principal()

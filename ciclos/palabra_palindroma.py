def palindroma(palabra):
    tam = len(palabra)-1  # Obtiene numero de indice de ultima palabra

    contador = 0
    for x in range(len(palabra)):  # Recorre de 0 hasta tamanio de palabra-1
        if palabra[x] == palabra[tam]:  # Compara primera letra con ultima
            contador += 1  # Suma +1 a contador si son iguales
        tam -= 1  # Disminuye indice
    palabra = palabra.upper()  # Convierte la palabra en mayusculas
    if contador == len(palabra):#Compara contador con el tamanio de palabra
        return f"\n{palabra}: Si es una palabra palindroma"
    else:
        return f"\n{palabra}: No es una palabra palindroma"


def palindroma2(palabra):
    if palabra == palabra[::-1]:
        return f"\n{palabra}: Sí es palindroma"
    else:
        return f"\n{palabra}: No es una palabra palindroma"


def principal():
    print("\n\n---Programa que recibe una palabra y comprueba si es palindroma o no---")
    mensaje = palindroma(input("Ingrese una palabra: "))
    print(mensaje)
    print("\n\n---Programa que comprueba si una palabra es palindroma (Codigo reducido)---")
    mensaje2 = palindroma2(input("Ingrese una palabra: "))
    print(mensaje2)


principal()

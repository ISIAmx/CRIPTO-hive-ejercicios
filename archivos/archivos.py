

def codificarTexto():
    lista = []
    f = open('origen.txt', "r")  # Abrir archivo en modo lectura
    text = f.read()  # obtiene contenido de archivo
    print(text)

    for x in range(len(text)):
        # Inserta codigo ASCII de caracter en lista
        lista.insert(x, ord(text[x]))
        # Suma 13 y obtiene modulo de cada codigo de lista
        lista[x] = (lista[x] + 13) % 26

    return lista  # retorna la lista generada como parametro


def escribirTexto(lista):
    f = open("destino.txt", "w")  # Abrir archivo en modo escritura
    print("\n--Caracteres Codificados")
    for x in range(len(lista)):

        # Suma 80 al codigo ASCII de c/e de lista y lo convierte en caracter
        caracter_nuevo = chr(lista[x]+80)
        f.write(caracter_nuevo)  # Escribe el nuevo caracter en archivo destino
        print(caracter_nuevo)


def principal():
    print("---CODIFICA TEXTO DE ARCHIVO ORIGEN Y LO ESCRIBE EN ARCHIVO DESTINO")
    textoCodificado = codificarTexto()
    escribirTexto(textoCodificado)


principal()

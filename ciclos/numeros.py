
"""Este programa solicita dos numeros enteros. Acepta el segundo siempre que sea mayor que el primero
.Al final imprime ambos numeros"""

print("\n\n--Este programa solicita dos numeros enteros. Acepta el segundo siempre que sea mayor que el primero. "
      "Al final imprime ambos numeros--")

num1 = int(input("\nIngrese el primer numero: "))
num2 = int(input(f"Ingrese un numero mayor a {num1}:"))

while num1 >= num2:
    print(f"\nEl {num2} no es mayor que {num1}")
    num2 = int(input(f"Ingrese un numero mayor a {num1}:"))

print(f"\nBien! Ingresaste el numero: {num1} y el numero:{num2}")


"""Solicita numeros enteros mas grandes que el anterior"""

print("\n--Este programa solicita numeros enteros mas grandes que el anterior--")
n1 = int(input(f"Ingrese primer numero: "))
while 1:
    n2 = int(input(f"Ingrese numero mayor a {n1}:"))
    while n2 <= n1:
        print(f"\nEl {n2} no es mayor que {n1}")
        n2 = int(input(f"Ingrese un numero mayor a {n1}:"))
    print(f"\nBien! El {n2} es mayor que {n1}")
    n1 = n2

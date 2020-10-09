# Hola Mundo en Python

print('Hola Mundo')

palabra = 'Hola Mundo'
print(palabra)

# Devuelve el tipo de dato la vairble --palabra--
print("\nDevuelve el tipo de dato la variable 'palabra'")
print(type(palabra))

# Suma de dos numeros
a = 5
b = 10

print(f"\nSuma de {a} + {b}")
print(a+b)


print('\nTabla de Multiplicar del 0 al 10')
x = 11
for i in range(x):
    print('\n')
    for j in range(x): 
        print(f"{i} * {j} = {i*j}")

numero = int(input("Escribe un número entero positivo: "))

if numero > 0:
    for i in range(1, numero + 1, 2):
        print(i, end=", ")
else:
    print("El número debe ser positivo.")


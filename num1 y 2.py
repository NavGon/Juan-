num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

if num2 == 0:
    print("No se puede dividir entre cero.")
else:
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")


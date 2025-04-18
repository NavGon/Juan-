peso = float(input("Escribe tu peso en kg: "))

estatura = float(input("Escribe tu estatura en metros: "))

imc = peso / (estatura ** 2)

imc = round(imc, 2)

print(f"Tu índice de masa corporal es {imc}")
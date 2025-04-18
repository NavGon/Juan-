cilindros = int(input("Cilindros vendidos en el ultimo paquete: "))
engranes = int(input("Engranes vendidos en el ultimo paquete: "))

peso_engranes = 112
peso_cilindros = 75

peso_total = (engranes * peso_engranes) + (cilindros * peso_cilindros)

print(f"El peso total del paquete es de {peso_total} gramos.")

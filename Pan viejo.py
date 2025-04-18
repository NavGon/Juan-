pan_viejo = int(input("Ingrese el pan no fresco vendido: "))

precio_normal = 3.49

descuento = 0.60

monto_descuento = precio_normal * descuento

precio_con_descuento = precio_normal - monto_descuento

costo_final_total = pan_viejo * precio_con_descuento

print("Precio habitual de un pan: $", precio_normal)
print("Descuento aplicado por no ser pan fresco: $", monto_descuento)
print("Coste final total: $", costo_final_total)

import utilidades


base_imponible = 1000.00
importe_con_descuento = utilidades.aplicar_descuento(base_imponible)
iva = utilidades.calcular_iva(importe_con_descuento)
total = importe_con_descuento + iva

print(f"Base imponible: {base_imponible:.2f} EUR")
print(f"Importe con descuento: {importe_con_descuento:.2f} EUR")
print(f"IVA: {iva:.2f} EUR")
print(f"Total: {total:.2f} EUR")

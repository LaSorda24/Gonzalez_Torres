importe_compra = 1250.00

if importe_compra > 1000:
    descuento = importe_compra * 0.10
else:
    descuento = 0

precio_final = importe_compra - descuento

print(f"Importe inicial: {importe_compra:.2f} EUR")
print(f"Descuento aplicado: {descuento:.2f} EUR")
print(f"Precio final: {precio_final:.2f} EUR")

volumen_compra = 1800.00

if volumen_compra < 500:
    tipo_cliente = "Cliente estandar"
elif volumen_compra <= 2000:
    tipo_cliente = "Cliente premium"
else:
    tipo_cliente = "Cliente VIP"

print(f"Volumen de compra: {volumen_compra:.2f} EUR")
print(f"Tipo de cliente: {tipo_cliente}")

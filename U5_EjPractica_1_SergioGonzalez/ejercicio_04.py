base_imponible = 1500.00
porcentaje_iva = 21

iva = base_imponible * porcentaje_iva / 100
total_factura = base_imponible + iva

print(f"IVA: {iva:.2f} EUR")
print(f"Total de la factura: {total_factura:.2f} EUR")

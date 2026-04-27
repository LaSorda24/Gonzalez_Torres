def calcular_total_factura(base_imponible, iva):
    return base_imponible + (base_imponible * iva / 100)


base = 1000.00
porcentaje_iva = 21
total = calcular_total_factura(base, porcentaje_iva)

print(f"Total de la factura: {total:.2f} EUR")

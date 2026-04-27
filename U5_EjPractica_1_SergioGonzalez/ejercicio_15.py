import utilidades


nombre_cliente = input("Introduce el nombre del cliente: ")
producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el numero de unidades: "))

subtotal = precio_unitario * unidades

if subtotal > 1000:
    total_con_descuento = utilidades.aplicar_descuento(subtotal)
else:
    total_con_descuento = subtotal

descuento = subtotal - total_con_descuento
iva = utilidades.calcular_iva(total_con_descuento)
total_final = total_con_descuento + iva

print("\nResumen de la venta")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Unidades: {unidades}")
print(f"Subtotal: {subtotal:.2f} EUR")
print(f"Descuento: {descuento:.2f} EUR")
print(f"IVA: {iva:.2f} EUR")
print(f"Total final: {total_final:.2f} EUR")

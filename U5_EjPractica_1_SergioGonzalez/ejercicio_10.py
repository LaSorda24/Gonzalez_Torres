productos = ["portatil", "monitor", "teclado", "raton", "impresora"]

producto_buscado = input("Introduce el nombre del producto: ").strip().lower()

if producto_buscado in productos:
    print(f"El producto '{producto_buscado}' existe en la lista.")
else:
    print(f"El producto '{producto_buscado}' no existe en la lista.")

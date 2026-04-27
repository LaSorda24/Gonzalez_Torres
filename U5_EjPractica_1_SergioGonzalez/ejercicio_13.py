try:
    importe = float(input("Introduce un importe: "))
    print(f"Importe introducido: {importe:.2f} EUR")
except ValueError:
    print("Error: el valor introducido no es numerico.")

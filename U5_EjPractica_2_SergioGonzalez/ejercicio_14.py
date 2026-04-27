import matplotlib.pyplot as plt


def main() -> None:
    productos: list[str] = ["Producto A", "Producto B", "Producto C", "Producto D"]
    ventas: list[int] = [52000, 68000, 45000, 73000]

    plt.figure(figsize=(8, 5))
    barras = plt.bar(productos, ventas, color=["#4C78A8", "#F58518", "#54A24B", "#E45756"])

    for barra, venta in zip(barras, ventas):
        posicion_x: float = barra.get_x() + barra.get_width() / 2
        posicion_y: int = venta
        plt.text(posicion_x, posicion_y + 1000, f"{venta} €", ha="center", va="bottom")

    plt.title("Ventas anuales por producto")
    plt.xlabel("Productos")
    plt.ylabel("Ventas (€)")
    plt.ylim(0, max(ventas) + 10000)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

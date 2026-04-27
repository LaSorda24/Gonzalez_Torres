import numpy as np


def main() -> None:
    productos: list[str] = ["Producto A", "Producto B", "Producto C"]
    ventas: np.ndarray = np.array([15000, 28000, 21000])
    indice_mas_vendido: int = int(np.argmax(ventas))

    print(f"Producto más vendido: {productos[indice_mas_vendido]}")


if __name__ == "__main__":
    main()

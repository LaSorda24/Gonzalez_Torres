import pandas as pd


def main() -> None:
    productos: pd.DataFrame = pd.DataFrame(
        {
            "nombre": [
                "Producto A",
                "Producto B",
                "Producto C",
                "Producto D",
                "Producto E",
                "Producto F",
            ],
            "precio": [15.0, float("nan"), 25.5, float("nan"), 18.0, float("nan")],
        }
    )

    total_inicial: int = len(productos)
    productos_limpios: pd.DataFrame = productos.dropna(subset=["precio"])
    registros_eliminados: int = total_inicial - len(productos_limpios)

    print(f"Registros eliminados: {registros_eliminados}")


if __name__ == "__main__":
    main()

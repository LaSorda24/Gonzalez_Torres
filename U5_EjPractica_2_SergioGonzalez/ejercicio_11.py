from pathlib import Path

import pandas as pd


def main() -> None:
    ruta_csv: Path = Path(__file__).with_name("productos_odoo.csv")
    productos: pd.DataFrame = pd.read_csv(ruta_csv)

    total_productos: int = len(productos)
    precio_medio: float = float(productos["precio"].mean())

    print(f"Productos: {total_productos}")
    print(f"Precio medio: {precio_medio:.2f} €")


if __name__ == "__main__":
    main()

import pandas as pd


def main() -> None:
    clientes: pd.DataFrame = pd.DataFrame(
        {
            "nombre": ["Empresa A", "Empresa B", "Empresa C"],
            "facturacion_anual": [25000, 40000, 60000],
        }
    )

    facturacion_total: float = float(clientes["facturacion_anual"].sum())
    facturacion_media: float = float(clientes["facturacion_anual"].mean())

    print(
        f"Facturación total: {facturacion_total:.0f} € "
        f"Media: {facturacion_media:.2f} €"
    )


if __name__ == "__main__":
    main()

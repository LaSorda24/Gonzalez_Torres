import pandas as pd


def main() -> None:
    clientes: pd.DataFrame = pd.DataFrame(
        {
            "nombre": ["Empresa A", "Empresa B", "Empresa C"],
            "pais": ["España", "Francia", "España"],
            "facturacion_anual": [25000, 40000, 60000],
        }
    )

    clientes_espana: pd.DataFrame = clientes[clientes["pais"] == "España"]
    nombres_clientes: str = " ".join(clientes_espana["nombre"].tolist())

    print(f"Clientes en España: {nombres_clientes}")


if __name__ == "__main__":
    main()

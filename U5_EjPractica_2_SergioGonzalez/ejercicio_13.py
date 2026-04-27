import matplotlib.pyplot as plt


def main() -> None:
    meses: list[str] = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    ventas: list[int] = [
        12000,
        13500,
        14200,
        15000,
        14800,
        15500,
        16000,
        15800,
        16200,
        17000,
        17500,
        19000,
    ]

    plt.figure(figsize=(10, 5))
    plt.plot(meses, ventas, marker="o", linewidth=2)
    plt.title("Evolución de ventas mensuales")
    plt.xlabel("Meses")
    plt.ylabel("Ventas (€)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

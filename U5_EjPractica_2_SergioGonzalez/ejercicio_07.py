import numpy as np


def main() -> None:
    ventas_mensuales: np.ndarray = np.array([9800, 12000, 14000, 15400, 19000, 21000])

    venta_media: float = float(np.mean(ventas_mensuales))
    venta_maxima: int = int(np.max(ventas_mensuales))
    venta_minima: int = int(np.min(ventas_mensuales))

    print(
        f"Venta media: {venta_media:.0f} € "
        f"Máxima: {venta_maxima} € "
        f"Mínima: {venta_minima} €"
    )


if __name__ == "__main__":
    main()

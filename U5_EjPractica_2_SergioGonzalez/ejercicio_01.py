from decimal import Decimal

import empresa_constantes as constantes


def formatear_importe(importe: Decimal) -> str:
    """Devuelve importes sin decimales cuando el resultado es entero."""
    if importe == importe.to_integral_value():
        return str(int(importe))

    return f"{importe:.2f}"


def calcular_total_factura(base: Decimal, tipo_iva: Decimal) -> tuple[Decimal, Decimal]:
    iva: Decimal = base * tipo_iva
    total: Decimal = base + iva
    return iva, total


def main() -> None:
    base: Decimal = Decimal("100")
    iva, total = calcular_total_factura(base, constantes.IVA_GENERAL)
    porcentaje_iva: int = int(constantes.IVA_GENERAL * 100)

    print(f"Base: {formatear_importe(base)} {constantes.MONEDA_DEFECTO}")
    print(
        f"IVA ({porcentaje_iva}%): "
        f"{formatear_importe(iva)} {constantes.MONEDA_DEFECTO}"
    )
    print(f"Total: {formatear_importe(total)} {constantes.MONEDA_DEFECTO}")


if __name__ == "__main__":
    main()

from decimal import Decimal
from typing import Final

IVA_EXENTO: Final[Decimal] = Decimal("0.00")
IVA_REDUCIDO: Final[Decimal] = Decimal("0.10")
IVA_GENERAL: Final[Decimal] = Decimal("0.21")

ESTADO_FACTURA_BORRADOR: Final[str] = "BORRADOR"
ESTADO_FACTURA_CONFIRMADA: Final[str] = "CONFIRMADA"
ESTADO_FACTURA_PAGADA: Final[str] = "PAGADA"

MONEDA_DEFECTO: Final[str] = "€"

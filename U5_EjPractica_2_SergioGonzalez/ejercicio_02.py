from enum import Enum


class EstadoPedido(Enum):
    BORRADOR = "BORRADOR"
    CONFIRMADO = "CONFIRMADO"
    ENVIADO = "ENVIADO"
    FACTURADO = "FACTURADO"


def cambiar_estado_pedido(nuevo_estado: EstadoPedido) -> EstadoPedido:
    return nuevo_estado


def main() -> None:
    estado_actual: EstadoPedido = cambiar_estado_pedido(EstadoPedido.CONFIRMADO)
    print(f"Estado actual del pedido: {estado_actual.value}")


if __name__ == "__main__":
    main()

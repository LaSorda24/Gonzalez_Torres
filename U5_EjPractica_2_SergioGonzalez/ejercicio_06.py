from dataclasses import dataclass


@dataclass
class Cliente:
    nombre: str
    email: str


@dataclass
class ProductoPedido:
    nombre: str
    precio_unitario: float
    unidades: int

    def subtotal(self) -> float:
        return self.precio_unitario * self.unidades


class Pedido:
    def __init__(self, cliente: Cliente, productos: list[ProductoPedido]) -> None:
        self.cliente = cliente
        self.productos = productos

    def total_pedido(self) -> float:
        return sum(producto.subtotal() for producto in self.productos)


def main() -> None:
    cliente: Cliente = Cliente("Empresa A", "compras@empresa-a.com")
    productos: list[ProductoPedido] = [
        ProductoPedido("Licencia ERP", 100.0, 2),
        ProductoPedido("Soporte tecnico", 40.0, 3),
    ]
    pedido: Pedido = Pedido(cliente, productos)

    print(f"Total del pedido: {pedido.total_pedido():.0f} €")


if __name__ == "__main__":
    main()

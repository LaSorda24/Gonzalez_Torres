
class Producto:
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def stock(self) -> int:
        return self.__stock

    def vender(self, unidades: int) -> None:
        if unidades <= 0:
            raise ValueError("Las unidades vendidas deben ser positivas.")

        if unidades > self.__stock:
            raise ValueError("No hay stock suficiente para realizar la venta.")

        self.__stock -= unidades

    def reponer(self, unidades: int) -> None:
        if unidades <= 0:
            raise ValueError("Las unidades repuestas deben ser positivas.")

        self.__stock += unidades

    def valor_stock(self) -> float:
        return self.__precio * self.__stock


def main() -> None:
    producto: Producto = Producto("Teclado empresarial", 10.0, 50)
    producto.vender(5)

    print(f"Stock restante: {producto.stock} Valor del stock: {producto.valor_stock():.0f} €")


if __name__ == "__main__":
    main()

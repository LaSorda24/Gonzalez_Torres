from dataclasses import dataclass


@dataclass
class Cliente:
    nombre: str
    email: str
    pais: str
    activo: bool = True

    def desactivar(self) -> None:
        self.activo = False


def main() -> None:
    cliente: Cliente = Cliente("Empresa X", "info@x.com", "España")
    cliente.desactivar()

    if not cliente.activo:
        print("Cliente desactivado correctamente")


if __name__ == "__main__":
    main()

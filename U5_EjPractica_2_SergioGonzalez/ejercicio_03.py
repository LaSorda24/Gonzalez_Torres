from dataclasses import dataclass


@dataclass
class Cliente:
    nombre: str
    email: str
    pais: str
    activo: bool

    def __str__(self) -> str:
        return (
            f"Cliente(nombre={self.nombre!r}, email={self.email!r}, "
            f"país={self.pais!r}, activo={self.activo!r})"
        )


def main() -> None:
    clientes: list[Cliente] = [
        Cliente("Empresa X", "info@x.com", "España", True),
        Cliente("Empresa Y", "contacto@y.com", "Portugal", True),
    ]

    for cliente in clientes:
        print(cliente)


if __name__ == "__main__":
    main()

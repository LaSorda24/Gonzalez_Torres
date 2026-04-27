import logging

try:
    from odoo import fields, models
except ImportError:
    class _Usuario:
        name = "admin"

    class _Entorno:
        user = _Usuario()

    class _Fields:
        @staticmethod
        def Boolean(**_opciones):
            return False

    class _Model:
        env = _Entorno()

        def __init__(self, **valores) -> None:
            self.name = valores.pop("name", "SO023")
            for campo, valor in valores.items():
                setattr(self, campo, valor)

        def __iter__(self):
            return iter([self])

    class _Models:
        Model = _Model

    fields = _Fields()
    models = _Models()


_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    reviewed = fields.Boolean(string="Revisado por administración", default=False)

    def action_mark_reviewed(self) -> bool:
        for pedido in self:
            pedido.reviewed = True
            _logger.info(
                "Pedido %s revisado por el usuario %s",
                pedido.name,
                pedido.env.user.name,
            )

        return True


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    pedido = SaleOrder(name="SO023")
    pedido.action_mark_reviewed()

    if pedido.reviewed:
        print(f"Pedido {pedido.name} marcado como revisado")


if __name__ == "__main__":
    main()

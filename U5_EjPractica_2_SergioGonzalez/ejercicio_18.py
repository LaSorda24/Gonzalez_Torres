import logging

try:
    from odoo import api, models
except ImportError:
    class _Api:
        @staticmethod
        def model(funcion):
            return funcion

    class _Model:
        def __init__(self, **valores) -> None:
            for campo, valor in valores.items():
                setattr(self, campo, valor)

        def create(self, valores: dict):
            return self.__class__(**valores)

    class _Models:
        Model = _Model

    api = _Api()
    models = _Models()


_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals: dict):
        cliente = super().create(vals)
        _logger.info("Nuevo cliente creado: %s", cliente.name)
        return cliente


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    modelo_cliente = ResPartner()
    modelo_cliente.create({"name": "Empresa Granada SL"})


if __name__ == "__main__":
    main()

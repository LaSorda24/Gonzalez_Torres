try:
    from odoo import api, fields, models
except ImportError:
    class _Api:
        @staticmethod
        def depends(*_campos: str):
            def decorador(funcion):
                return funcion

            return decorador

    class _Fields:
        @staticmethod
        def Float(**_opciones):
            return 0.0

    class _Model:
        def __init__(self, **valores) -> None:
            for campo, valor in valores.items():
                setattr(self, campo, valor)

        def __iter__(self):
            return iter([self])

    class _Models:
        Model = _Model

    api = _Api()
    fields = _Fields()
    models = _Models()


class SaleOrder(models.Model):
    _inherit = "sale.order"

    amount_total_with_tax = fields.Float(
        string="Total con IVA",
        compute="_compute_amount_total_with_tax",
        store=False,
    )

    @api.depends("amount_untaxed", "amount_tax")
    def _compute_amount_total_with_tax(self) -> None:
        for pedido in self:
            pedido.amount_total_with_tax = pedido.amount_untaxed + pedido.amount_tax


VISTA_FORMULARIO_PEDIDO: str = """
<odoo>
    <record id="view_order_form_inherit_amount_total_with_tax" model="ir.ui.view">
        <field name="name">sale.order.form.amount.total.with.tax</field>
        <field name="model">sale.order</field>
        <field name="inherit_id" ref="sale.view_order_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='amount_total']" position="after">
                <field name="amount_total_with_tax" readonly="1"/>
            </xpath>
        </field>
    </record>
</odoo>
"""


def main() -> None:
    pedido = SaleOrder(amount_untaxed=100.0, amount_tax=21.0)
    pedido._compute_amount_total_with_tax()
    print(f"Total con IVA: {pedido.amount_total_with_tax:.0f} €")


if __name__ == "__main__":
    main()

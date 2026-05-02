from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AutorecambiosReposicion(models.Model):
    _name = "autorecambios.reposicion"
    _description = "Solicitud de Reposicion"
    _order = "fecha_solicitud desc, id desc"

    name = fields.Char(
        string="Solicitud",
        required=True,
        copy=False,
        help="Codigo interno o nombre identificativo de la solicitud.",
    )
    referencia_recambio = fields.Char(
        string="Referencia del recambio",
        required=True,
        help="Referencia interna del recambio que necesita reposicion.",
    )
    solicitante = fields.Char(
        string="Solicitante",
        help="Empleado o responsable que solicita la reposicion.",
    )
    descripcion = fields.Text(
        string="Descripcion",
        help="Motivo o detalle de la necesidad de reposicion.",
    )
    fecha_solicitud = fields.Date(
        string="Fecha de solicitud",
        required=True,
        default=fields.Date.context_today,
    )
    cantidad = fields.Integer(
        string="Cantidad",
        required=True,
        default=1,
        help="Numero de unidades que se solicitan para reponer stock.",
    )
    precio_unitario = fields.Float(
        string="Precio unitario",
        required=True,
        digits=(16, 2),
        default=0.0,
        help="Coste estimado de cada unidad del recambio.",
    )
    tipo_prioridad = fields.Selection(
        selection=[
            ("baja", "Baja"),
            ("media", "Media"),
            ("alta", "Alta"),
        ],
        string="Prioridad",
        required=True,
        default="media",
    )
    importe_total = fields.Float(
        string="Importe total",
        compute="_compute_importe_total",
        store=True,
        digits=(16, 2),
        help="Importe total estimado de la reposicion.",
    )
    state = fields.Selection(
        selection=[
            ("draft", "Borrador"),
            ("confirmed", "Confirmado"),
            ("done", "Finalizado"),
        ],
        string="Estado",
        required=True,
        default="draft",
    )

    @api.depends("cantidad", "precio_unitario")
    def _compute_importe_total(self):
        """Calcula automaticamente el coste total estimado."""
        for record in self:
            record.importe_total = record.cantidad * record.precio_unitario

    @api.constrains("cantidad", "precio_unitario")
    def _check_valores_positivos(self):
        """Evita cantidades no validas y precios negativos."""
        for record in self:
            if record.cantidad <= 0:
                raise ValidationError(
                    "La cantidad solicitada debe ser mayor que cero."
                )
            if record.precio_unitario < 0:
                raise ValidationError(
                    "El precio unitario no puede ser negativo."
                )

    def action_confirm(self):
        """Pasa la solicitud de borrador a confirmada."""
        for record in self:
            if record.state == "draft":
                record.state = "confirmed"

    def action_done(self):
        """Marca la solicitud como finalizada."""
        for record in self:
            if record.state == "confirmed":
                record.state = "done"

    def action_reset_draft(self):
        """Permite volver a borrador para corregir la solicitud."""
        self.write({"state": "draft"})

from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    fecha_reserva = fields.Date(string='Fecha de Reserva')
    cantidad_personas = fields.Integer(string='Cantidad de Personas', default=1)

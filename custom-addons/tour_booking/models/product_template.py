from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    es_tour = fields.Boolean(string='Es Tour Turistico', default=False)

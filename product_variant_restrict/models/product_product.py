from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    bey_pass_counter_ids = fields.Many2many('pos.config',string="Restricted POS", help="This particular product will not be visible in the selected POS")
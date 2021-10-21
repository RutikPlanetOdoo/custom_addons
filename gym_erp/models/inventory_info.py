from odoo import api, models, fields

class InventoryInfo(models.Model):
    _inherit = 'stock.picking'
    _rec_name = 'pro_name'

    pro_name = fields.Char("Product Name")

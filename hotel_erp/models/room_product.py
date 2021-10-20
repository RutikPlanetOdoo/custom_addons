from odoo import api, fields, models

class RoomProduct(models.Model):
    _inherit = 'res.partner'

    room_product_ids = fields.One2many(comodel_name='sale.order.line', inverse_name='room_product_id', string='Room product')

class ResPartner(models.Model):
    _inherit = 'sale.order.line'

    room_product_id = fields.Many2one('res.partner')



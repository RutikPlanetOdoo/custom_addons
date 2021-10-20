from odoo import api,fields,models

class PartnerProduct(models.Model):
    _inherit = 'res.partner'

    room_product_ids = fields.One2many(comodel_name='product.info', inverse_name='room_product_id')

class ProductInfo(models.Model):
    _name = 'product.info'
    product_id = fields.Many2one('product.product')
    product_uom_qty = fields.Float('Quantity')
    price_unit = fields.Float('Unit Price')
    room_product_id = fields.Many2one('res.partner')
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.company)

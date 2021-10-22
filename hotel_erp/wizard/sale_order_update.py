from odoo import api, fields, models

class SaleOrderUpdate(models.TransientModel):
    _name = 'sale.customer'


    order_ids = fields.One2many(comodel_name='sale.info', inverse_name='product_id')

class SaleWizardInfo(models.TransientModel):
    _name = "sale.info"
    _description = "Sale Wizard"
    _rec_name = 'product_id1'

    product_id = fields.Many2one(comodel_name='sale.wizard', string="Product")
    product_id1 = fields.Many2one(comodel_name='product.product', string="Product")
    description = fields.Char("Description")
    category = fields.Char("Product Category")
    quantity = fields.Float("Quantity")
    unit_price = fields.Float("Unit Price")
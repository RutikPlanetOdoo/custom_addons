from odoo import api,models,fields

class ProductProduct(models.Model):
    _inherit = 'product.product'
    ci_product = fields.Selection([('person', 'Individual'),
                                   ('company', 'Company')], 'Company or Individual')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    can_rent = fields.Boolean('Can be rent')
    rent_price = fields.Float(
        'Rent Price', default=1.0,
        digits='Product Rent Price',
        help="Price at which the product is rented by customers.")

    # com_indi_product = fields.Selection([('individual','Individual'),
    #                                      ('company','Company')
    #                                      ],'Individual or Company')

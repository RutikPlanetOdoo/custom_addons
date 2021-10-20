from odoo import api, fields, models

class SaleOrderInfor(models.Model):
    _inherit = 'sale.order'

    order_day_info = fields.Char('Order Day')
    customer_name = fields.Char('Customer Name')
    coupon_code = fields.Char('Coupon Code')
    product_cat = fields.Char('Product Category')

    def copy(self, default={}):
        print('Copy running', default)
        default['partner_id'] = 51
        for rec in self.order_line:
            lines = [(5, 0, 0)]
            val = {
                'product_id': 58
            }
            lines.append((0, 0, val))
        self.order_line = lines
        return super(SaleOrderInfor, self).copy(default)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    short_code = fields.Char('Short Code')
    product_cat = fields.Char('Product Category', related='product_id.product_tmpl_id.categ_id.name')


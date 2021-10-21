from odoo import api, fields, models


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.wizard'
    _description = "Sale Wizard"

    expiration_date = fields.Date(string="Expiration")
    order_ids = fields.One2many(comodel_name='sale.wizardinfo', inverse_name='product_id')

    def update_detail(self):
        active_id = self.env.context.get('active_id')
        order_info_rec = self.env['sale.order']
        order_change_id = order_info_rec.search([('id', '=', active_id)])
        print("active_id: ", active_id)
        print('order_info_rec: ', order_info_rec)
        print('order_change_id: ', order_change_id)
        order_change_id.validity_date = self.expiration_date

        for rec in order_change_id:
            lines = [(5, 0, 0)]
            print("self.order_ids.product_id1", self.order_ids.product_id1)
            for line in self.order_ids:
                val = {
                    'product_id': line.product_id1.id,
                    'name': line.description,
                    'product_uom_qty': line.quantity,
                    'price_unit': line.unit_price,
                }
                lines.append((0, 0, val))
            print(lines)
            rec.order_line = lines
            print(rec.order_line)
        return 1


class SaleWizardInfo(models.TransientModel):
    _name = "sale.wizardinfo"
    _description = "Sale Wizard"
    _rec_name = 'product_id1'

    product_id = fields.Many2one(comodel_name='sale.wizard', string="Product")
    product_id1 = fields.Many2one(comodel_name='product.product', string="Product")
    description = fields.Char("Description")
    quantity = fields.Float("Quantity")
    unit_price = fields.Float("Unit Price")

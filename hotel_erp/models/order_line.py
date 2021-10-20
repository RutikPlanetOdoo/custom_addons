from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo import api,models,fields
import datetime

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    check_in = fields.Datetime('Check In Time')
    check_out = fields.Datetime('Check Out Time')
    num_hr = fields.Integer('Number of Hours stay', readonly=1)
    num_per = fields.Integer('Number of people')

    @api.onchange('check_in','check_out')
    def onchange_check_in(self):
        if self.check_in and self.check_out:
            in_date = self.check_in
            out_date = self.check_out
            if out_date > in_date:
                diff = out_date-in_date
                days, seconds = diff.days, diff.seconds

                hours = days * 24 + seconds // 3600
                self.num_hr = hours
                if hours > 0 and hours <=24:
                    self.product_uom_qty = 1
                else:
                    self.product_uom_qty = diff.days
            else:
                raise ValidationError('Invalid Date')


from odoo import api, fields, models

class  CompanyInfo(models.Model):
    _inherit = 'sale.order'

    company_check = fields.Boolean('Company check')

    @api.onchange('partner_id')
    def company_info(self):
        print('company')
        if self.partner_id.is_company == True:
            self.company_check = True
        else:
            self.company_check = False

    tax_discount = fields.Selection([('ten', '10%'),
                                     ('five', '5%'),],
                                    'Tax Discount',)
    tot_discount = fields.Float('Discount',readonly=True)

    @api.onchange('tax_discount')
    def discount(self):
        a = self.amount_untaxed * 10/100
        b = self.amount_untaxed * 5/100
        if self.tax_discount == "ten":
            self.amount_total = self.amount_untaxed - a + self.amount_tax
            self.tot_discount = a
        elif self.tax_discount == "five":
            self.amount_total = self.amount_untaxed - b + self.amount_tax
            self.tot_discount = b
        else:
            self.tot_discount = 0
        return 0
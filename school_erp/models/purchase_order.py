from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    ci_product = fields.Selection([('person', 'Individual'),
                                   ('company', 'Company')],
                                  'Company or Individual',related='partner_id.company_type')
from odoo import api, models, fields
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class AccountMove(models.Model):
    _inherit = 'account.move'

    check_comp = fields.Char(string='Company or Individual')

    @api.onchange('partner_id')
    def check_compa(self):
        if self.partner_id.is_company:
            self.check_comp = 'Company PO'
        elif not self.partner_id.is_company:
            self.check_comp = 'Individual PO'
        else:
            self.check_comp = ' '

    def unlink(self):
        if self.amount_total >= 10000:
            raise ValidationError('Cannot delete record containing total more than 10000')
        return super(AccountMove, self).unlink()

class AccountPayment(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        active_id = self.env['account.move'].search([('id', '=', self.env.context.get('active_id'))])
        if active_id.check_comp == 'Company PO' and self.amount <= 1000:
            raise ValidationError('Amount should be less than 1000')
        else:
            payments = self._create_payments()

            if self._context.get('dont_redirect_to_payments'):
                return True

            action = {
                'name': _('Payments'),
                'type': 'ir.actions.act_window',
                'res_model': 'account.payment',
                'context': {'create': False},
            }
            if len(payments) == 1:
                action.update({
                    'view_mode': 'form',
                    'res_id': payments.id,
                })
            else:
                action.update({
                    'view_mode': 'tree,form',
                    'domain': [('id', 'in', payments.ids)],
                })
            return action

from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo import api,fields,models

class SaleOrderView(models.Model):
    _inherit = 'sale.order'

    verification = fields.Boolean(string='Verification Done')
    room_number = fields.Many2one(comodel_name='room.info',string='Room Number')

    @api.onchange('partner_id')
    def UpdateOrder(self):
        # active_id = self.env.context.get('active_id')
        for rec in self:
            lines = []
            for line in self.partner_id.room_product_ids:
                val = {
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                }
                lines.append((0, 0, val))
                print(lines)
            rec.order_line = lines
            return 0

    global room_list
    room_list = []
    @api.onchange('room_number')
    def onchange_room(self):
        for record in self.room_number:
            if record.room_num in room_list:
                raise ValidationError('The selected Room is already booked')
            else:
                room_list.append(record.room_num)
            print(room_list)

    def action_confirm(self):
        res = super(SaleOrderView, self).action_confirm()
        action = {
            'name': "Create Invoices",
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': False,
            'res_model': 'sale.advance.payment.inv',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }
        return action


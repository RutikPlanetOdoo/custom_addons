from odoo import api, fields, models


class InheritFile(models.Model):
    _inherit = 'cultural.fest'
    culture_theme = fields.Char('Theme of Fest')

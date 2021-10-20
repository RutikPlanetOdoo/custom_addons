from odoo import api, fields, models


class DoctorsInfo(models.Model):
    _name = 'doctors.info'
    _rec_name = 'doc_name'
    doc_name = fields.Char("Doctor's name")


from odoo import api, fields, models

class  Scholarship(models.Model):
    _name = 'scholarship.info'
    _rec_name = 'scholarship_type'

    student_id = fields.Many2one('student.info','Student Name')
    standard_id = fields.Many2one('standard.info','Standard Name')
    scholarship_type = fields.Char('Type of Scholarship')

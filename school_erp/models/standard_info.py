from odoo import api, fields, models


class StandardInfo(models.Model):
    _name = 'standard.info'
    _rec_name = 'teacher_id'

    # teacher_name = fields.Char("Teacher name")
    standard_id = fields.Selection([('std_1', 'Standard 1'),
                                    ('std_2', 'Standard 2'),
                                    ('std_3', 'Standard 3'),
                                    ('std_4', 'Standard 4'),
                                    ('std_5', 'Standard 5'),
                                    ('std_6', 'Standard 6'),
                                    ('std_7', 'Standard 7'),
                                    ('std_8', 'Standard 8'),
                                    ('std_9', 'Standard 9'),
                                    ('std_10', 'Standard 10'),],
                                   'Standard', related='teacher_id.standard_id')
    teacher_id = fields.Many2one('teacher.info', 'Teacher Name')
    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('div_d', 'D'), ],
                                'Division', required=True, related='teacher_id.division')


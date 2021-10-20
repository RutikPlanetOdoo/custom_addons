from odoo import api, fields, models


class TeacherInfo(models.Model):
    _name = 'teacher.info'
    name = fields.Char('Teacher Name')
    Surname = fields.Char('Surname')
    teachers_age = fields.Integer('Age')
    standard_id = fields.Selection([('std_1', 'Standard 1'),
                                    ('std_2', 'Standard 2'),
                                    ('std_3', 'Standard 3'),
                                    ('std_4', 'Standard 4'),
                                    ('std_5', 'Standard 5'),
                                    ('std_6', 'Standard 6'),
                                    ('std_7', 'Standard 7'),
                                    ('std_8', 'Standard 8'),
                                    ('std_9', 'Standard 9'),
                                    ('std_10', 'Standard 10')],
                                   'Standard', required=True)


    city = fields.Char('City', default ='Mumbai', readonly =True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')],
                              'Gender', required=True)
    is_pwd = fields.Boolean('is available fulltime')

    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('div_d', 'D'),],
                                'Division', required=True)
    subject = fields.Many2one(comodel_name='subject.info')
    teacher_id = fields.Many2one('teacher.info', 'Teacher')

class SubjectInfo(models.Model):
    _name = 'subject.info'
    _rec_name = 'subject_name'

    subject_name = fields.Char("Subject Name")





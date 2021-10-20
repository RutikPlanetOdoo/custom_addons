from odoo import api, fields, models

class StudentInfo(models.Model):
    _name = 'student.info'

    name = fields.Char('Name')
    last_name = fields.Char('Last Name')
    student_age = fields.Integer('Age')
    city = fields.Char('City', default='Mumbai', readonly=True)
    gender_male = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                   'Gender')
    is_pwd = fields.Boolean('Is Physically Handicapped?')
    teacher_id = fields.Many2one('teacher.info')

    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('std_d', 'D'),],
                                'Division', related='teacher_id.division')
    teacher_name = fields.Char(related='teacher_id.name')

    student1_id = fields.Many2one(comodel_name='library.info')

    issue_date = fields.Datetime('Issue Date')
    ret_date = fields.Datetime('Return Date')
    education_quota = fields.Selection([('five', '5%'),
                                        ('ten', '10%'),
                                        ('two-five', '25%'),
                                        ('twelve', '12%'),
                                        ('fifty', '50%'),
                                        ],'Education Quota')
    stu_budget = fields.Integer('Budget',compute='_compute_budget',readonly=0, store=1)
    event_ids = fields.One2many(comodel_name='event.info',inverse_name='stu_name')

    fest_ids = fields.Many2many(comodel_name='cultural.fest', relation='student_info_cultural_fest_rel',
                                column1='stud_id', column2='fest_id', string='Groups')

    scholarship_ids = fields.Many2many(comodel_name='scholarship.info', relation='student_info_scholarship_info_rel',
                                       column1='stud_id2e', column2='scholarship_id', string='scholarship')

    teachers_ids = fields.One2many(comodel_name='teachers.subjects.line', inverse_name='teacher1_id')

    chemistry = fields.Integer('Chemistry')
    physics = fields.Integer('Physics')
    maths = fields.Integer('Maths')
    english = fields.Integer('English')
    hsc_total = fields.Integer('HSC Total', compute='_compute_total', store=True)
    hsc_percentage = fields.Float('HSC Percentage', readonly=True)
    status = fields.Char(default=None,readonly=True)
    documents = fields.Binary(string='Documents')

    student_tt = fields.Html(string='Student Time Table')

    @api.depends('chemistry','physics','maths','english')
    def _compute_total(self):
            total = self.chemistry + self.physics + self.maths + self.english
            self.hsc_total = total

    @api.onchange('hsc_total')
    def onchange_total(self):
        percentage = (self.hsc_total*100)/ 400
        self.hsc_percentage = percentage

    @api.onchange('hsc_percentage')
    def onchange_per(self):
        if self.hsc_percentage < 40:
            self.status = 'Fail'
        elif self.hsc_percentage > 40:
            self.status = 'Pass'

    @api.depends('event_ids')
    def _compute_budget(self):
        for budget in self.mapped('event_ids'):
            if not budget.check_record:
                up_fee = self.stu_budget - budget.event_fee
                self.stu_budget = up_fee
                budget.check_record = True

    def change_age(self):
        self.student_age = 25
        return 1

    @api.onchange('gender_male')
    def onchange_name(self):
        print("aaaaaaaa")
        if self.gender_male == 'female':
            self.education_quota = 'ten'
        else:
            self.education_quota = 'five'

    @api.onchange('is_pwd')
    def onchange_name(self):
        print("pwd")
        if self.is_pwd == True:
            self.education_quota = 'two-five'
        else:
            self.education_quota = 'five'



class TeachersSubjects(models.Model):
    _name = 'teachers.subjects.line'

    teacher1_id = fields.Many2one(comodel_name='student.info')

    subject_id = fields.Many2one(comodel_name='subject.info', string="Subjects")

    teacher_name_id = fields.Many2one(comodel_name='teacher.info')

from odoo import api, fields, models
from datetime import datetime

class LibraryInfo(models.Model):
    _name = 'library.info'
    _rec_name = 'book_name'
    book_name = fields.Char("Book name", required = True)
    author_name = fields.Char('Author name')
    book_id = fields.Integer('Book ID')
    book_type = fields.Char('Book type')
    teacher_id = fields.Many2one('teacher.info','Teacher')
    # date_time = fields.Datetime('Date time')
    date_time = fields.Date('Date')
    library_ids = fields.One2many(comodel_name='student.info', inverse_name='student1_id')

    # @api.onchange('teacher_id')
    # def onchange_subject(self):
    #     print("aaaaaaaa")
    #     if self.teacher_id.subject.subject_name == 'Geography':
    #         self.book_id = 10


    def write(self, vals):
        print('Vals',vals)
        if vals:
            vals.update({'book_type': 'Fun'})
        return super(LibraryInfo, self).write(vals)

    @api.model
    def create(self, vals):
        print('CREATE CALL', vals)
        print('Create working')
        vals['date_time'] = datetime.today()
        return super(LibraryInfo, self).create(vals)



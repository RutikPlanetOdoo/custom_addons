from odoo import api, fields, models

class  CulturalFest(models.Model):
    _name = 'cultural.fest'
    _rec_name = 'fest_name'

    fest_name = fields.Char('Festival Name')
    standard_id = fields.Many2one('standard.info','Standard Name')
    number_of_participants = fields.Integer('Number of Participants')
    festival_information = fields.Text('Fest Information')

    event_info = fields.One2many('event.info','culture_many','Event info')

    @api.model
    def default_get(self, fields):
        res = super(CulturalFest, self).default_get(fields)
        res['fest_name'] = 'Udaan'
        res['number_of_participants'] = 10
        return res

    # def write(self, values):
    #     lines = []
    #     for rec in values.get('event_info'):
    #         print("Main record: ", rec)
    #         print("event_info record: ", rec[1])
    #         for record in rec:
    #             if type(rec[1]) is int:
    #                 fest_line_obj = self.env['event.info'].browse(rec[1])
    #                 print("fest_line_obj: ", fest_line_obj)
    #                 if not fest_line_obj.check_record:
    #                     if type(record) is dict:
    #                         print("record: ", record)
    #                         if record.get('event_fee'):
    #                             val = {
    #                                 'check_record': True,
    #                                 'event_fee': record.get('fees'),
    #                             }
    #                             lines.append((1, rec[1], val))
    #         if lines:
    #             values.update({"event_info": lines})
    #     print("values: ", values)
    #     return super(CulturalFest, self).write(values)

class EventInfo(models.Model):
    _name = 'event.info'
    _rec_name = 'event_name'

    culture_many = fields.Many2one('cultural.fest')
    event_name = fields.Char('Competition')
    event_fee = fields.Integer('Fees')
    stu_name = fields.Many2one('student.info', 'Student Name')
    check_record = fields.Boolean('Fee Check', store=True)
    check_addition = fields.Boolean('Addition check')

    def unlink(self):
        print("Unlink is running")
        for record in self:
            print(record)
            for rec in record.stu_name:
                print(rec.stu_budget)
                budget_remained = rec.stu_budget + record.event_fee
                rec.stu_budget = budget_remained
        return super(EventInfo, self).unlink()

    @api.onchange('event_fee')
    def onchange_fees_id(self):
        if self.event_fee:
            self.stu_name.stu_budget -= self.event_fee
            self.check_record = True
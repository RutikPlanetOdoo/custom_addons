from odoo import api, models, fields
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import date
import re

class GymInfo(models.Model):
    _inherit ='res.partner'

    cus_name = fields.Char('Customer Name')
    join_date = fields.Date('Joining Date')
    new_gym_ids = fields.One2many(comodel_name='gym.notebook', inverse_name='note_many')
    total_price = fields.Integer('Total Price', compute='_compute_total', store=True)
    cus_dob = fields.Date('Date Of Birth')
    cus_age = fields.Char('Age')

    @api.onchange('cus_dob')
    def compute_age(self):
        today = date.today()
        age = today.year - self.cus_dob.year - ((today.month, today.day) < (self.cus_dob.month, self.cus_dob.day))
        self.cus_age = age

    @api.onchange('email')
    def check_mail(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex,self.email):
            pass
        else:
            raise ValidationError('Not a valid email')

    @api.depends('new_gym_ids', 'total_price')
    def _compute_total(self):
        total = 0
        for record in self.new_gym_ids:
            print(self.new_gym_ids)
            total += record.price_supp_mass
        self.total_price = total

class GymSchedule(models.Model):
    _name = 'gym.schedule'
    _rec_name = 'exe_name'
    exe_name = fields.Char('Name of the exercise')
    reps = fields.Integer('Repetition')
    sets = fields.Integer('Sets')

    gym_note = fields.One2many(comodel_name='gym.notebook', inverse_name='note_many') #no use

class GymNotebook(models.Model):

    _name = 'gym.notebook'

    schdl_date = fields.Date('Sheduling Date')
    wrkout_plan = fields.Many2one('gym.schedule')
    in_date = fields.Date('In Date')
    out_date = fields.Date('Out Date')
    note_many = fields.Many2one('res.partner')
    gym_massage = fields.Boolean('Massage')
    supplement = fields.Boolean('Supplement')
    price_supp_mass = fields.Integer('Price', compute='_compute_price',store=True)
    # total_price = fields.Integer('Total Price', compute='_price_total',store=True)


    @api.depends('gym_massage','supplement')
    def _compute_price(self):
        mass = 500
        supp = 100
        if self.gym_massage == True & self.supplement == True:
            self.price_supp_mass = mass + supp
        elif self.gym_massage:
            self.price_supp_mass = mass
        elif self.supplement:
            self.price_supp_mass = supp
        else:
            self.price_supp_mass = 0

    @api.depends('price_supp_mass')
    def _price_total(self):
        for i in self:
            mass = 500
            supp = 100
            if self.gym_massage == True & self.supplement == True:
                self.price_supp_mass = mass + supp
            elif self.gym_massage:
                self.price_supp_mass = mass
            elif self.supplement:
                self.price_supp_mass = supp
            else:
                self.price_supp_mass = 0


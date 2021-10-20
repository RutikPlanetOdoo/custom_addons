from odoo import api,fields,models

class RoomInfo(models.Model):
    _name = 'room.info'
    _rec_name = 'room_num'

    room_num = fields.Selection([('101', '101'),
                                 ('102', '102'),
                                 ('103', '103'),
                                 ('104', '104'),
                                 ('105', '105'),
                                 ('106', '106'),
                                 ('107', '107'),
                                 ('108', '108'),
                                 ('109', '109'),
                                 ('110', '110')],
                                'Room Number')

    floor_num = fields.Selection([('1', '1st Floor'),
                                  ('2', '2nd Floor'),
                                  ('3', '3st Floor'),
                                  ('4', '4st Floor'),
                                  ('5', '5st Floor')],
                                'Floors')
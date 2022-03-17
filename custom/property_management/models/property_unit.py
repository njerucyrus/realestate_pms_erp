from odoo import api, fields, models, _


class PropertyUnit(models.Model):
    _name = 'pms.property_unit'
    _rec_name = 'house_number'
    _description = 'Property Unit'
    property_id = fields.Many2one(comodel_name='pms.property', string='Property')
    house_number = fields.Char(string='House Number', required=True, tracking=True)
    floor = fields.Selection(string='Floor',
                             selection=[
                                 ('0', 'Ground Floor'),
                                 ('1', '1st Floor'),
                                 ('2', '2nd Floor'),
                                 ('3', '3rd Floor'),
                                 ('4', '4th Floor'),
                                 ('5', '5th Floor'),
                                 ('6', '6th Floor'),
                                 ('7', '7th Floor'),
                                 ('9', '9th Floor'),
                                 ('10', '10th Floor'),
                                 ('11', '11th Floor'),
                                 ('12', '12th Floor'),
                             ],
                             required=True, tracking=True)
    unit_type = fields.Selection(string='Type', selection=[
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('bedsitter', 'Bedsitter'),
        ('1bedroom', '1 Bedroom'),
        ('2bedroom', '2 Bedroom'),
        ('3bedroom', '3 Bedroom'),
    ], required=True, tracking=True)
    rent_fee = fields.Float(string='Rent Fee', required=True, tracking=True)
    status = fields.Selection(selection=[
        ('vacant', 'Vacant'),
        ('occupied', 'Occupied'),
    ], string='Status', default='vacant', tracking=True)



from odoo import api, fields, models, _


class LandLord(models.Model):
    _name = 'pms.landlord'
    _description = 'Landlord'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Full Name", required=True, tracking=True)
    landlord_type = fields.Selection(string="Type", selection=[
        ('individual', 'Individual'),
        ('company', 'Company')
    ], required=True, default='company', tracking=True)
    phone_number = fields.Char(string='Phone Number', required=True, tracking=True)
    email_id = fields.Char(string='Email Address', required=True, tracking=True)
    country = fields.Selection(selection=[
        ('kenya', 'Kenya'),
        ('uganda', 'Uganda'),
        ('tanzania', 'Tanzania'),
        ('rwanda', 'Rwanda'),
    ], default='kenya', string='Country')

    state = fields.Char(string='State')
    city = fields.Char(string='City')
    address = fields.Char(string='Address')

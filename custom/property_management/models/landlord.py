from odoo import api, fields, models, _


class LandLord(models.Model):
    _name = 'pms.landlord'
    _description = 'Landlord'
    name = fields.Char(string="Full Name", required=True, tracking=True)
    landlord_type = fields.Selection(string="Type", selection=[
        ('individual', 'Individual'),
        ('company', 'Company')
    ], required=True, tracking=True)
    phone_number = fields.Char(string='Phone Number', required=True, tracking=True)
    email_id = fields.Char(string='Email Address', required=True, tracking=True)
    city = fields.Char(string='City', required=True, tracking=True)
    state = fields.Char(string='State', required=True, tracking=True)
    country = fields.Char(string='Country', required=True, tracking=True)

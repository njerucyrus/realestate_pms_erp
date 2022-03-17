from odoo import api, fields, models, _


class Tenant(models.Model):
    _name = 'pms.tenant'
    _description = 'Tenant'

    name = fields.Char(string='Full Name', required=True, tracking=True)
    phone_number = fields.Char(string='Phone Number', required=True, tracking=True)
    email = fields.Char(string='Email Address', required=True, tracking=True)
    marital_status = fields.Selection(string='Marital Status', selection=[
        ('single', 'Single'),
        ('married', 'Married'),
        ('other', 'Other'),
    ])
    gender = fields.Selection(string='Gender', selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('not_say', 'Prefer not to say'),
    ])


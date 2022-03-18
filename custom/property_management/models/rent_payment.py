from odoo import api, fields, models, _


class RentPayment(models.Model):
    _name = 'pms.rent_payment'
    _description = 'Rent Payment Records'
    date = fields.Date(string='Date')
    tenancy_detail_id = fields.Many2one(comodel_name='pms.rent_detail', string='Tenancy Details')
    transaction_id = fields.Char(string='Transaction ID')
    receipt_no = fields.Char(string='Receipt No')
    phone_number = fields.Char(string='Phone Number')
    amount = fields.Char(string='Amount')
    payment_method = fields.Selection(selection=[
        ('cash', 'Cash'),
        ('bank_deposit', 'Bank Deposit'),
        ('mpesa', 'Mpesa')
    ])

    paid_by = fields.Char(string='Paid By')
    status = fields.Selection(selection=[
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ], default='pending', string='Status')

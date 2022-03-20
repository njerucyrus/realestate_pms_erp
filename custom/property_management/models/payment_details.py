from odoo import api, fields, models, _


class PaymentDetail(models.Model):
    _name = 'pms.payment_detail'
    _description = "Model for storing payment details for a property"

    property_id = fields.Many2one(comodel_name='pms.property', string='Property')
    payment_channel = fields.Selection(selection=[
        ('bank', 'Bank'),
        ('mobile_money', 'Mobile Money'),
    ])
    bank_account = fields.Many2one(comodel_name='pms.bank_account', string='Bank Account')


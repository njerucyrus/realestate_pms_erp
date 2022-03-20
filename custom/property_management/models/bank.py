from odoo import api, fields, models, _


class BankAccount(models.Model):
    _name = 'pms.bank_account'
    _description = 'Bank Accounts'
    country = fields.Selection(selection=[
        ('kenya', 'Kenya'),
        ('uganda', 'Uganda'),
        ('tanzania', 'Tanzania'),
        ('rwanda', 'Rwanda'),
    ], default='kenya', string='Country', required=True)
    bank_name = fields.Char(string="Bank Name", required=True)
    branch = fields.Char(string="Branch")
    account_no = fields.Char(string="Account Number", required=True)

    def name_get(self):
        res = []
        for rec in self:
            rec_name = f"{rec.bank_name}({rec.account_no})"
            res.append(rec_name)
        return res


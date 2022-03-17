from odoo import api, fields, models, _


class TenancyDetail(models.Model):
    _name = 'pms.tenancy_detail'
    _description = 'Tenancy Details'

    property_id = fields.Many2one(comodel_name='property', string='Property')
    property_unit_id = fields.Many2one(comodel_name='pms.property_unit', String="House Number")
    tenant_id = fields.Many2one(comodel_name='pms.tenant', string='Tenant')
    tenancy_start = fields.Date(string="Tenancy Start")
    tenancy_end = fields.Date(string="Tenancy End")
    deposit = fields.Float(string='Deposit')
    payment_day = fields.Integer(string='Payment Day')
    attachment_id = fields.Many2one(comodel_name='ir.attachment', string="Agreement Document", required=True)

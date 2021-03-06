from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TenancyDetail(models.Model):
    _name = 'pms.tenancy_detail'
    _rec_name = 'tenant_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tenancy Details'

    property_id = fields.Many2one(comodel_name='pms.property', string='Property')
    property_unit_id = fields.Many2one(comodel_name='pms.property_unit', String="House Number")
    tenant_id = fields.Many2one(comodel_name='pms.tenant', string='Tenant')
    tenancy_start = fields.Date(string="Tenancy Start")
    tenancy_end = fields.Date(string="Tenancy End")
    deposit = fields.Float(string='Deposit')
    payment_day = fields.Integer(string='Payment Day')
    attachment_id = fields.Binary(string="Agreement Document", required=True)
    filename = fields.Char('Filename')

    @api.model
    def create(self, vals):
        res = super(TenancyDetail, self).create(vals)
        unit_record = self.env['pms.property_unit'].search([('id', '=', vals.get('property_unit_id'))])
        unit_record.write({'status': 'occupied'})
        return res

    def unlink(self):
        for rec in self:
            unit_record = self.env['pms.property_unit'].search([('id', '=', rec.property_unit_id.id)])
            unit_record.write({'status': 'vacant'})
        return super(TenancyDetail, self).unlink()

    @api.constrains('tenancy_start', 'tenancy_end')
    def date_constrains(self):
        for rec in self:
            if rec.tenancy_end < rec.tenancy_start:
                raise ValidationError(_('Sorry, Tenancy End Date Must be greater Than Tenancy Start Date.'))

    @api.onchange('property_id')
    def onchange_property_id(self):
        for rec in self:
            return {'domain': {'property_unit_id': [('property_id', '=', rec.property_id.id)]}}





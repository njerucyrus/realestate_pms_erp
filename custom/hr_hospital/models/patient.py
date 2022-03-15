# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string="Reference", readonly=True,copy=False, default=lambda self: _('New'))
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),

    ], required=True, default='other', tracking=True )

    note = fields.Text(string='Notes', )
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancel', 'Canceled'),
                              ], default="draft", string='Status', tracking=True)

    responsible_id = fields.Many2one(comodel_name='res.partner', string='Responsible', tracking=True)


    def action_confirm(self):
        self.state = 'confirm'

    def action_cancel(self):
        self.state = "cancel"

    def action_done(self):
        self.state = "done"

    def action_mark_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, vals):

        if vals.get('reference', _('New') == _('New')):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

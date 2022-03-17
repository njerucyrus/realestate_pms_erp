# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Property(models.Model):
    _name = 'pms.property'
    _description = 'Rental Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Property Name", required=True, tracking=True)
    property_type = fields.Selection(string="Type", selection=[
        ('apartment', 'Apartment'),
        ('flat', 'Flat'),

    ], default='apartment')

    image = fields.Binary(string="Property Image")
    country = fields.Selection(selection=[
        ('kenya', 'Kenya'),
        ('uganda', 'Uganda'),
        ('tanzania', 'Tanzania'),
        ('rwanda', 'Rwanda'),
    ], default='kenya', string='Country')

    state = fields.Char(string='State')
    city = fields.Char(string='City')
    address = fields.Char(string='Address/Physical Location')
    # Amenities
    nearby_bus_stop = fields.Boolean(string="Bus Stop", tracking=True, default=False)
    nearby_hospital = fields.Boolean(string="Hospital", tracking=True, default=False)
    scenic_view = fields.Boolean(string="Scenic View", tracking=True, default=False)
    balcony = fields.Boolean(string="Balcony", tracking=True, default=False)
    cctv = fields.Boolean(string="CCTV", tracking=True, default=False)
    garden = fields.Boolean(string="Garden", tracking=True, default=False)
    swimming_pool = fields.Boolean(string="Swimming Pool", tracking=True, default=False)
    lift = fields.Boolean(string="Lift/Elevator", tracking=True, default=False)
    gym = fields.Boolean(string="Gym", tracking=True, default=False)
    electric_fence = fields.Boolean(string="Electric Fence", tracking=True, default=False)
    parking = fields.Boolean(string="Electric Fence", tracking=True, default=False)
    backup_generator = fields.Boolean(string="Backup Generator", tracking=True, default=False)
    fiber_internet = fields.Boolean(string="Fibre Internet", tracking=True, default=False)
    walkin_closet = fields.Boolean(string="Walk In Closet", tracking=True, default=False)
    service_charge = fields.Boolean(string="Service Charge", tracking=True, default=False)
    ensuite = fields.Boolean(string="Ensuite", tracking=True, default=False)
    alarm = fields.Boolean(string="Alarm", tracking=True, default=False)
    property_unit_lines = fields.One2many('pms.property_unit', 'property_id', string='Unit Lines')
    # units = fields.Char(string='Units', compute='_compute_property_lines')
    # vacant = fields.Char(string='Vacant Units', compute='_compute_vacant')
    # occupied = fields.Char(string='Occupied Units', compute='_compute_occupied')

    # def _compute_property_lines(self):
    #     lines = len(self.property_unit_lines)
    #     self.units = f"{lines}"
    #
    # def _compute_vacant(self):
    #     vacant_units = 0
    #     for line in self.property_unit_lines:
    #         if line.status == 'vacant':
    #             vacant_units += 1
    #
    #     self.vacant = f'{vacant_units}'
    #
    # def _compute_occupied(self):
    #     occupied_units = 0
    #     for line in self.property_unit_lines:
    #         if line.status == 'occupied':
    #             occupied_units += 1
    #
    #     self.occupied = f'{occupied_units}'

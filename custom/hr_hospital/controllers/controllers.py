# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/hrHospital(http.Controller):
#     @http.route('/custom/hr_hospital/custom/hr_hospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/hr_hospital/custom/hr_hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/hr_hospital.listing', {
#             'root': '/custom/hr_hospital/custom/hr_hospital',
#             'objects': http.request.env['custom/hr_hospital.custom/hr_hospital'].search([]),
#         })

#     @http.route('/custom/hr_hospital/custom/hr_hospital/objects/<model("custom/hr_hospital.custom/hr_hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/hr_hospital.object', {
#             'object': obj
#         })

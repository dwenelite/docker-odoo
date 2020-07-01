# -*- coding: utf-8 -*-
from odoo import http

# class Odoo-addons(http.Controller):
#     @http.route('/odoo-addons/odoo-addons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-addons/odoo-addons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-addons.listing', {
#             'root': '/odoo-addons/odoo-addons',
#             'objects': http.request.env['odoo-addons.odoo-addons'].search([]),
#         })

#     @http.route('/odoo-addons/odoo-addons/objects/<model("odoo-addons.odoo-addons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-addons.object', {
#             'object': obj
#         })
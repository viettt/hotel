# -*- coding: utf-8 -*-
from odoo import http

# class HotelModifier(http.Controller):
#     @http.route('/hotel_modifier/hotel_modifier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_modifier/hotel_modifier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_modifier.listing', {
#             'root': '/hotel_modifier/hotel_modifier',
#             'objects': http.request.env['hotel_modifier.hotel_modifier'].search([]),
#         })

#     @http.route('/hotel_modifier/hotel_modifier/objects/<model("hotel_modifier.hotel_modifier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_modifier.object', {
#             'object': obj
#         })
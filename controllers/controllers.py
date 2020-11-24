# -*- coding: utf-8 -*-
from odoo import http

# class Trips(http.Controller):
#     @http.route('/trips/trips/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trips/trips/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('trips.listing', {
#             'root': '/trips/trips',
#             'objects': http.request.env['trips.trips'].search([]),
#         })

#     @http.route('/trips/trips/objects/<model("trips.trips"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trips.object', {
#             'object': obj
#         })
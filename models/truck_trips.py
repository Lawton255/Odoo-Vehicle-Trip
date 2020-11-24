from odoo import models, fields, api

class TruckTrips(models.Model):
    _name = 'truck.trips'
    _iniherit = 'fleet.vehicle'

    customer    = fields.Many2one('res.partner' , string='Customer name')
    trip_no     = fields.Integer(string="Trip number", required=True, unique=True, default=0)
    truck       =  fields.Many2one('fleet.vehicle', string='Truck', required=True)
    trip_type   = fields.Selection([('go', 'Go'), ('return', 'Return')], required=True)
    container   = fields.Selection([('20', '20'), ('40', '40')], required=True)
    departure_date  = fields.Date(string='Departure date')
    alive_date  = fields.Date(string='Alive date')
    start_region      = fields.Char(string='Departure Region')
    start_country     = fields.Many2one('res.country', string='Departure Country', required=True)
    end_region      = fields.Char(string='Destination Region')
    end_country     = fields.Many2one('res.country', string='Destination Country', required=True)

    


from odoo import models, fields, api

class TruckTrips(models.Model):
    _name = 'truck.trip'
    _iniherit = 'fleet.vehicle'

    customer    = fields.Many2one('res.partner' , string='Customer name')
    trip_no     = fields.Integer(string="Trip number", required=True, unique=True, default=0)
    truck       =  fields.Many2one('fleet.vehicle', string='Truck', required=True)
    trip_type   = fields.Selection([('go', 'Go'), ('return', 'Return')], required=True)
    container_no = fields.Integer(string="Container number")
    container_type  = fields.Selection([('0', '0'), ('20', '20'), ('40', '40')], default='0', required=True, string="Container Type")
    cargo_type  =    fields.Selection([('lose cargo', 'Lose Cargo'),('sulpher', 'Sulpher') ], string="Cargo type")
    departure_date  = fields.Date(string='Departure date')
    arrived_date  = fields.Date(string='Arrived date')
    amount = fields.Integer(String="Price")
    loaded_date  = fields.Date(string='Loaded date')
    unloaded_date  = fields.Date(string='Unloaded date')
    start_region    = fields.Char(string='Departure Region', default="Dar Es Salaam")
    start_country   = fields.Many2one('res.country', string='Departure Country', required=True)
    end_region      = fields.Char(string='Destination Region')
    end_country     = fields.Many2one('res.country', string='Destination Country', required=True)

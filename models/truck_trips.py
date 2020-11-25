from odoo import models, fields, api

class TruckTrips(models.Model):
    _name = 'truck.trip'
    _iniherit = 'fleet.vehicle'

    customer    = fields.Many2one('res.partner' , string='Customer name', required=True)
    trip_no     = fields.Integer(string="Trip number", required=True, unique=True, default=0)
    truck       =  fields.Many2one('fleet.vehicle', string='Truck', required=True)
    trip_type   = fields.Selection([('go', 'Go'), ('return', 'Return')], required=True)
    container_no = fields.Integer(string="Container number" , required=True)
    container_type  = fields.Selection([('0', '0'), ('20', '20'), ('40', '40')], default='0', required=True, string="Container Type")
    cargo_type  =    fields.Selection([('lose cargo', 'Lose Cargo'),('steel cargo', 'Steel Cargo') ], string="Cargo type", required=True)
    cargo_amount = fields.Float(string="Price in USD", required=True)
    cargo_unit   = fields.Float(string="Unit per Ton", default='1.00')
    total_amount = fields.Float(string="Total in USD")
    departure_date  = fields.Date(string='Departure date')
    arrived_date  = fields.Date(string='Arrived date')
    loaded_date  = fields.Date(string='Loaded date')
    unloaded_date  = fields.Date(string='Unloaded date')
    start_region    = fields.Char(string='Departure Region', default="Dar Es Salaam")
    start_country   = fields.Many2one('res.country', string='Departure Country', required=True)
    end_region      = fields.Char(string='Destination Region')
    end_country     = fields.Many2one('res.country', string='Destination Country', required=True)

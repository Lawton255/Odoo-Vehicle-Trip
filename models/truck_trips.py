from odoo import models, fields, api

class TruckTrips(models.Model):
    _name = 'truck.trip'
    _iniherit = 'fleet.vehicle'

    @api.depends('cargo_quantity', 'cargo_amount')
    def _compute_total_amount(self):
        for record in self:
            if record['cargo_amount'] !=0:
                record['total_amount'] = record.cargo_amount * record.cargo_quantity

    @api.depends('cargo_commission', 'unit_qty', 'bond_price')
    def _compute_total_commission(self):
        for commission in self:
            commission['total_commission'] = ((commission.cargo_commission * commission.unit_qty) + commission.bond_price)

    
    @api.depends('total_amount', 'total_commission')
    def _compute_total_return(self):
        for rec in self:
            rec['total_return'] = rec.total_amount - rec.total_commission
            

    customer    = fields.Many2one('res.partner' , string='Customer name', required=True)
    trip_no     = fields.Integer(string="Trip number", required=True, unique=True, default=0)
    truck       =  fields.Many2one('fleet.vehicle', string='Truck', required=True)
    trip_type   = fields.Selection([('go', 'Go'), ('return', 'Return')], required=True)
    container_no = fields.Integer(string="Container number" , required=True)
    container_type  = fields.Selection([('0', '0'), ('20', '20'), ('40', '40')], default='0', required=True, string="Container Type")
    departure_date  = fields.Date(string='Departure date')
    arrived_date  = fields.Date(string='Arrived date')
    loaded_date  = fields.Date(string='Loaded date')
    unloaded_date  = fields.Date(string='Unloaded date')
    start_region    = fields.Char(string='Departure Region', default="Dar Es Salaam")
    start_country   = fields.Many2one('res.country', string='Departure Country', required=True)
    end_region      = fields.Char(string='Destination Region')
    end_country     = fields.Many2one('res.country', string='Destination Country', required=True)

    cargo_type  =    fields.Selection([('lose cargo', 'Lose Cargo'),('steel cargo', 'Steel Cargo') ], string="Cargo type", required=True)
    cargo_amount = fields.Float(string="Price in USD", required=True)
    cargo_quantity   = fields.Float(string="Quantity in Tonnes", default='1.00')
    total_amount = fields.Float(string="Cargo Return in USD", compute="_compute_total_amount")

    cargo_commission = fields.Float(string='Commission Price in USD')
    unit_qty         = fields.Float(string='Quantity in Tonnes', default='1.0')
    bond_price       = fields.Float(string='Bond Price in USD')
    total_commission = fields.Float(string='Total Commission' , compute="_compute_total_commission")

    total_return = fields.Float(string='Total Return without expenses $', compute='_compute_total_return')

    

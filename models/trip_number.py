from odoo import models, fields

class TripNumber(models.Model):
    _name = 'trip.number'
    _rec_name = 'trip_no'

    trip_no = fields.Char(string="Trip number", unique=True)
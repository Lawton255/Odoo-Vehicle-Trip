from odoo import models, fields

class TripNumber(models.Model):
    _name = 'trip.number'
    _rec_name = 'trip_no'

    #_sql_constraints = [
    #('trip_no', 'unique (trip_no)', _('Trip number must be unique !')),
    #]

    trip_no = fields.Char(string="Trip number")
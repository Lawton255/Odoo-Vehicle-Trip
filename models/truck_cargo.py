from odoo import models, fields

class Cargo(models.Model):
    _name = 'trip.cargo'

    name = fields.Char(string='Cargo Type')
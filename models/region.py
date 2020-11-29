from odoo import models, fields

class Region(models.Model):
    _name = 'region.region'

    name = fields.Char(string='Region')
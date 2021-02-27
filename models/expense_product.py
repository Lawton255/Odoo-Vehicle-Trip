from odoo import models, fields

class ProductExpenses(models.Model):
    _name = 'product.expenses'

    name = fields.Char()
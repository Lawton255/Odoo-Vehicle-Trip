from odoo import models, fields

class ExpenseSupplier(models.Model):
    _name = 'supplier.expense'

    name = fields.Char(string="Supplier name")
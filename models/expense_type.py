from odoo import models,fields

class ExpenseType(models.Model):
    _name = 'type.expense'
    

    name = fields.Char(string="Expense Type")
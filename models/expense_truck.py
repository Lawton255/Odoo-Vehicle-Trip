from odoo import models, fields, api

class AllExpenses(models.Model):
    _name = 'truck.expenses'
    _rec_name = 'trip_no'
    _order  =   'trip_no asc'


    @api.depends('expense_amount', 'expense_qty')
    def _compute_total_expense(self):
        for record in self:
                record['expense_total'] = record.expense_amount * record.expense_qty

    @api.model
    def default_get(self, default_fields):
        res = super(AllExpenses, self).default_get(default_fields)
        res.update({
            'date': fields.Date.context_today(self)})
        return res

    
    trip_no = fields.Many2one('truck.trip', 'Trip no', required=True , auto_join=True, index=True, ondelete='cascade')
    responsible = fields.Many2one('res.partner', 'Responsible', required=True , auto_join=True, index=True, ondelete='cascade')
    date                = fields.Date(string="Date")
    expense_id  = fields.One2many('truck.expenses', 'id', string='Expense Line')
    expense_type = fields.Many2one('type.expense',required=True, auto_join=True, index=True, ondelete='cascade')
    expense_product = fields.Many2one('product.expenses', 'Expense name', required=True , auto_join=True, index=True, ondelete='cascade')
    expense_amount  = fields.Float(string="Price", required=True)
    expense_qty        = fields.Float(string="Quantity" , default='1.0')
    expense_total   = fields.Float(string="Total(Tsh)", compute="_compute_total_expense", required=True)
    date        = fields.Date(string="Date")
    #expense_responsible = fields.Many2one('res.partner', 'Responsible Person', auto_join=True, index=True, ondelete='cascade')

    #Payments of expenses
    paid_by     = fields.Many2one('res.partner', string="Paid by" , required=True, auto_join=True, index=True, ondelete='cascade')
    paid        = fields.Boolean(string="Paid", default=True , required=True, auto_join=True, index=True, ondelete='cascade')
    payment_method = fields.Selection([('cash', 'Cash'), ('cheque', 'Cheque'), ('mobile_money', 'Mobile Money'),], required=True)
    #payment_reference = fields.Char(string='Payment reference', required=True)
    supplier = fields.Many2one('supplier.expense', auto_join=True, index=True, ondelete='cascade')
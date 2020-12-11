from odoo import models, fields, api

class TruckTrips(models.Model):
    _name = 'truck.trip'
    _rec_name = 'trip_no'
    _iniherit = ['fleet.vehicle' ,
                 'region.region',
                 'trip.cargo',
                 'trip.number']
    _order    = 'trip_no desc'

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

    @api.depends('total_return', 'rate')
    def _compute_rate(self):
        for myrate in self:
            myrate['total_return_rate'] = myrate.total_return * myrate.rate
            

    #Truck trips
    trip_no     = fields.Many2one('trip.number', required=True, unique=True, auto_join=True, index=True, ondelete='cascade')
    customer    = fields.Many2one('res.partner' , string='Customer name', required=True, auto_join=True, index=True, ondelete='cascade')
    truck       =  fields.Many2one('fleet.vehicle', string='Truck', required=True, auto_join=True, index=True, ondelete='cascade')
    trip_type   = fields.Selection([('go', 'Go'), ('return', 'Return')], required=True)
    container_no = fields.Integer(string="Container number" , required=True)
    container_type  = fields.Selection([('0', '0'), ('20', '20'), ('40', '40')], default='0', required=True, string="Container Type")
    departure_date  = fields.Date(string='Departure date')
    arrived_date  = fields.Date(string='Arrived date')
    loaded_date  = fields.Date(string='Loaded date')
    unloaded_date  = fields.Date(string='Unloaded date')
    start_region    = fields.Many2one('region.region', 'Departure Region', required=True, auto_join=True, index=True, ondelete='cascade')
    start_country   = fields.Many2one('res.country', string='Departure Country', required=True, auto_join=True, index=True, ondelete='cascade')
    end_region      = fields.Many2one('region.region', 'Destination Region', required=True, auto_join=True, index=True, ondelete='cascade')
    end_country     = fields.Many2one('res.country', string='Destination Country', required=True, auto_join=True, index=True, ondelete='cascade')

    #Cargo details
    cargo_type  =    fields.Many2one('trip.cargo', required=True, auto_join=True, index=True, ondelete='cascade')
    cargo_amount = fields.Float(string="Price in USD", required=True)
    cargo_quantity   = fields.Float(string="Quantity in Tonnes", default='1.00')
    total_amount = fields.Float(string="Cargo Return (USD)", compute="_compute_total_amount")

    #Commission
    cargo_commission = fields.Float(string='Commission Price (USD)')
    unit_qty         = fields.Float(string='Quantity in Tonnes', default='1.0')
    bond_price       = fields.Float(string='Bond Price (USD)')
    total_commission = fields.Float(string='Total Commission (USD)' , compute="_compute_total_commission")

    total_return = fields.Float(string='Total Return without expenses (USD)', compute='_compute_total_return')

    rate = fields.Float(string="Rate(Tsh)", required=True)
    total_return_rate = fields.Float(string="Total Return without expenses (Tsh)", compute="_compute_rate")
    child_id = fields.One2many(comodel_name="expense.truck", inverse_name="parent_id", string="General Expense",required=False, auto_join=True, index=True, ondelete='cascade')

    #Truck Expenses
class TruckExpenses(models.Model):
    _name = 'expense.truck'
    #_rec_name = 'trip_no'
    _order  =   'date asc'


    @api.depends('expense_amount', 'expense_qty')
    def _compute_total_expense(self):
        for record in self:
                record['expense_total'] = record.expense_amount * record.expense_qty

    @api.model
    def default_get(self, default_fields):
        res = super(TruckExpenses, self).default_get(default_fields)
        res.update({
            'date': fields.Date.context_today(self)})
        return res

    
    #trip_no = fields.Many2one('truck.trip', 'Trip no', required=True , auto_join=True, index=True, ondelete='cascade')
    responsible = fields.Many2one('res.partner', 'Responsible', required=True , auto_join=True, index=True, ondelete='cascade')
    date                = fields.Date(string="Date")
    #expense_id  = fields.One2many('expense.truck', 'id', string='Expense Line')
    expense_type = fields.Many2one('expense.type',required=True, auto_join=True, index=True, ondelete='cascade')
    expense_product = fields.Many2one('expenses.product', 'Expense name', required=True , auto_join=True, index=True, ondelete='cascade')
    expense_amount  = fields.Float(string="Price", required=True)
    expense_qty        = fields.Float(string="Quantity" , default='1.0')
    expense_total   = fields.Float(string="Total(Tsh)", compute="_compute_total_expense", required=True)
    #expense_responsible = fields.Many2one('res.partner', 'Responsible Person', auto_join=True, index=True, ondelete='cascade')
    

    #Payments of expenses
    paid_by     = fields.Many2one('res.partner', string="Paid by" , required=True, auto_join=True, index=True, ondelete='cascade')
    paid        = fields.Boolean(string="Paid", default=True , required=True, auto_join=True, index=True, ondelete='cascade')
    payment_method = fields.Selection([('cash', 'Cash'), ('cheque', 'Cheque'), ('mobile_money', 'Mobile Money'),], required=True)
    #payment_reference = fields.Char(string='Payment reference', required=True)
    supplier = fields.Many2one('expense.supplier', required=True, auto_join=True, index=True, ondelete='cascade')
    parent_id = fields.Many2one(comodel_name="truck.trip", string="Parent ID", required=False, auto_join=True, index=True, ondelete='cascade')

class ProductExpenses(models.Model):
    _name = 'expenses.product'

    name = fields.Char()

class ExpenseType(models.Model):
    _name = 'expense.type'
    

    name = fields.Char(string="Expense Type")

class ExpenseSupplier(models.Model):
    _name = 'expense.supplier'

    name = fields.Char(string="Supplier name")
# -*- coding: utf-8 -*-
{
    'name': "Odoo-Vehicle-Trip",

    'summary': "Trips of each truck including go and return",

    'description': """
        Long description of module's purpose
    """,

    'author': "Emmauel Lawton",
    'website': "#",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '12.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
       # 'views/templates.xml',
       'views/trip_view.xml',
       'views/truck_view_expenses.xml',
       'views/invoice_template.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
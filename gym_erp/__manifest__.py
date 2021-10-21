# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'GYM ERP',
    'version': '1.0',
    'author': 'Rutik Pabharekar',
    'category': 'Fitness',
    'summary': 'Gym tutorials ',
    'description': "We are learning what is odoo and development in odoo",
    'website': 'https://www.odoo.com',
    'depends': [
        'base', 'stock', 'sale', 'purchase', 'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/gym_info_views.xml',
        'views/inventory_info_views.xml',
        'wizard/update_phone_wizard_view.xml',
        'wizard/sale_order_wizard_view.xml',
        'views/sale_order_button_view.xml',
        'views/purchase_error_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}


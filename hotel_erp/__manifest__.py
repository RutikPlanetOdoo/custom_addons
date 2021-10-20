# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hotel ERP',
    'version': '1.0',
    'author': 'Rutik Pabharekar',
    'category': 'Test',
    'summary': 'Tutorials of school ERP',
    'description': "Hotel Management System",
    'website': 'https://www.odoo.com',
    'depends': [
        'base','sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/room_info_views.xml',
        # 'views/room_product_views.xml',
        'views/sale_order_views.xml',
        'views/room_prod_views.xml',
        'views/order_line_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

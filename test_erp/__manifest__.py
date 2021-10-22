# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Test ERP',
    'version': '1.0',
    'author': 'Rutik Pabharekar',
    'category': 'Testing',
    'summary': 'Testing ERP for odoo 15',
    'description': "Test",
    'website': 'https://www.odoo.com',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School ERP',
    'version': '1.0',
    'author': 'Rutik Pabharekar',
    'category': 'Tutorials',
    'summary': 'Tutorials of school ERP',
    'description': "We are learning what is odoo and development in odoo",
    'website': 'https://www.odoo.com',
    'depends': [
        'base', 'sale', 'account', 'purchase', 'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_info_views.xml',
        'views/standard_info_views.xml',
        'views/teacher_info_views.xml',
        'views/library_info_views.xml',
        'views/cultural_info_views.xml',
        'views/scholarship_info_views.xml',
        'views/subject_info_views.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'views/weather_info_views.xml',
        'wizard/update_age_wizard_view.xml',
        'views/account_move_views.xml',
        'views/company_other_views.xml',
        'report/report.xml',
        'report/student_card.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

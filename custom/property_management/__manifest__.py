# -*- coding: utf-8 -*-
{
    'name': "Property Management",

    'summary': "Property Management",

    'description': """
        Long description of module's purpose
    """,

    'author': "Hudutech Ventures",
    'website': "http://www.hudutech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/property_view.xml',
        'views/agents_view.xml',
        'views/landlords_view.xml',
        'views/tenants_view.xml',
        'views/tenancy_details_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        ],
    "sequence": -101,
    "installable": True,
    "application": True,
    "auto_install": False,
}

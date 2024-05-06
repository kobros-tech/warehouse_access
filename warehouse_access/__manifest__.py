# -*- coding: utf-8 -*-

{
    'name': "Warehouse Access Management",
    'version': '17.0.1.0.0',
    'summary': """Warehouse Access Management""",
    'description': """Warehouse Access Management""",
    'author': 'Mohamed Alkobrosli',
    'company': 'kobros-tech',
    'maintainer': 'Mohamed Alkobrosli',
    'website': 'https://www.kobros-tech.com',
    'depends': [
        'stock',
        'sale',
        'sale_stock',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'security/stock_security.xml',
        'views/res_users_views.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False
}

# Copyright (c) 2020-Present Autodidacta TI. (<https://autodidactati.com>)

{
    'name': 'Hide Qty',
    "version": "14.0",
    'author': 'Ivan Arriola - Autodidacta TI, Exemax, Codize',
    'category': 'Extra Tools',
    'license': 'OPL-1',
    'website': 'https://autodidactati.com',
    'summary': 'Oculta cantidades de stock en ubicaciones que los usuarios no son responsables',
    'description': '''Oculta cantidades de stock en ubicaciones que los usuarios no son responsables''',
    'depends': ['stock', 'sale'],
    'data': [
        'views/stock_location.xml',
        'views/stock_quant.xml'
    ],
    'installable': True,
    'auto_install': False
}

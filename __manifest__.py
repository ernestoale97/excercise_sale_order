{
    'name': "Sales Order Expiration Date Feature",
    'summary': "Extension of the Sales Management (sale_management) module for managing an expiration date on sales",
    'description': "Extension of the Sales Management (sale_management) module for managing an expiration date on sales",
    'author': "Ernesto Alejandro Quintero Suarez",
    'website': "https://www.epcsoftwares.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': True,
}

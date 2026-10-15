{
    'name': 'HR Payroll Colombia - Rules',
    'version': '18.0.1.0.0',
    'summary': 'Scaffold seed for HR Payroll CO Odoo modules',
    'description': """
HR Payroll CO
===========================

This is a reusable module scaffold/seed to bootstrap new Odoo modules
following basic conventions. Use this as a starting point.
    """,
    'author': 'Jam <j4mlfy@gmail.com>',
    'website': 'http://jam2tech.co',
    'license': 'LGPL-3',
    'category': 'Payroll',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/seed_template_data.xml',
        'views/seed_template_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'icon': '/hr_payroll_co_seed/static/description/icon.png',
}

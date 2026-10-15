{
    'name': 'HR Payroll CO - Module Seed',
    'version': '18.0.1.0.0',
    'summary': 'Scaffold seed for HR Payroll CO Odoo modules',
    'description': """
HR Payroll CO - Module Seed
===========================

This is a reusable module scaffold/seed to bootstrap new Odoo modules
following basic conventions. Use this as a starting point.
    """,
    'author': 'HR Payroll CO',
    'website': '',
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

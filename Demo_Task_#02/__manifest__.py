{
    'name': 'Analytic Distribution on Invoices and PDF Report',
    'version': '1.0.0',
    'description': """
    Replicate analytic distribution in invoices and show on PDF reports.
    """,
    'author': 'Ahmed Jakwani',
    'depends': ['base', 'sale'],
    'data': [
        'report/sale_report_inherit.xml',
        'report/invoice_report_inherit.xml',
    ],
    'application': True,
    'installable': True,

}
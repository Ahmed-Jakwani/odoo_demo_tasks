{
    'name': 'Custom Invoice Template',
    'version': '1.0.0',
    'description': """
    Custom Invoice Template Report
    """,
    'author': 'Ahmed Jakwani',
    'depends': ['base'],
    'data': [
        'data/custom_invoice_paperformat.xml',
        
        'report/custom_invoice_report_template.xml',
        'report/custom_invoice_report_action.xml'
    ],
    'application': True,
    'installable': True,
}
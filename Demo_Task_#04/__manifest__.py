{
    'name': 'Stock Approval Workflow',
    'version': '1.0.0',
    'description': """
    This module adds an approval process when the "Done" quantity exceeds the "Demand" quantity in transfer receipts, 
    controlling button visibility and allowing specific users to approve or reject the transfer.
    """,
    'author': 'Ahmed Jakwani',
    'depends': ['stock'],
    'data': [
        'security/groups_for_receipt_approval.xml',
        'views/stock_picking.xml',
    ],
    'application': True,
    'installable': True,
}
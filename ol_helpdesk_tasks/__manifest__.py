# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Create Helpdesk Ticket Tasks',
    'author':'Maaz Ali',
    # 'version': '1.0',
    "license": "OPL-1",
    "version": "16.0",
    'category': '',
    'sequence':100,
    'summary': 'Create Helpdesk Ticket Tasks',
    'description': """""",
    'depends': ['base','sh_all_in_one_helpdesk'],
    'data': [
        'views/helpdesk_ticket.xml',
        ],
    'demo': [],
    'installable': True,
    'assets': {},
    'application':True,
    # 'license': 'LGPL-3',
}

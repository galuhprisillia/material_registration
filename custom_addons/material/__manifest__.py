# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Material Module',
    'version': '14.0.0',
    'category': 'Application',
    'summary': 'List of material',
    'description': 'List of material',
    'live_test_url': '',
    'sequence': '1',
    'website': 'https://github.com/galuhprisillia',
    'author': 'galuhprisillia',
    'maintainer': 'galuhprisillia',
    'license': 'LGPL-3',
    'support': 'galuhprisillia@gmail.com',
    'depends': [
        'base'
    ],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'view/material_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}

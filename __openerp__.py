# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Forecast Pro Data Loader',
    'version': '1.0.0',
    'author': 'acentoNET',
    'summary': 'Forecast, data',
    'description' : """
Forecast Pro Data Loader
========================
    """,
    'website': 'http://www.acentonet.com',
    'category': 'Purchase',
    'depends': ["product", "purchase"],
    'init_xml' : [],
    'demo_xml' : [],
    'data': [
        'forecastpro_data_loader.xml',
        'views/forecastpro_data_sales_view.xml',
        'views/forecastpro_data_inventory_view.xml',
        'wizard/forecastpro_data_sales_wizard.xml',
        'wizard/forecastpro_data_inventory_wizard.xml',
        'wizard/forecastpro_generate_data_file_wizard.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

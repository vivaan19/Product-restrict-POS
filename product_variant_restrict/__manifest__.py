# -*- coding: utf-8 -*-
#############################################################################
#
#    Beyondata Solution Pvt. Ltd.
#
#    Copyright (C) Beyondata Solution Pvt. Ltd.(<http://beyondatagroup.com/>)
#    Author: Beyondata Solution Pvt. Ltd.(<http://beyondatagroup.com/>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Product Variant Restrict',
    'version': '1.0',
    'summary': 'For Product Restrict',
    'description': 'For product variant restrict in POS Screen',
    'category': 'Point of Sale',
    'author': 'BeyonData Solution Pvt. Ltd.',
    'license': 'LGPL-3',
    'price': '19.10',
    'currency': 'USD',

    'depends': ['base', 'point_of_sale'],
    
    'data': [
        'views/product_product.xml',
    ],
    
    'assets': {
        'point_of_sale._assets_pos': [
            'product_variant_restrict/static/src/overrides/models/pos_store.js',
        ],
    
    },

    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
}

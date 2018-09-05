# -*- coding: utf-8 -*-
{
    'name': "Modulo de Refacciones",
    'summary': """
    """,
    'description': """
        Módulo de refacciones especiales
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    # le quite --> ,'data/refaccion_demo.xml'
    'data': ['views/refaccion_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
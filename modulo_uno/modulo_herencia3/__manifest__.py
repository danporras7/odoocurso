# -*- coding: utf-8 -*-
{
    'name': "Modelo Herencia 3",

    'summary': """
    """,

    'description': """
        Modulo creado para ocultar pestana
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base','stock','product'
    ],

    # always loaded
    'data': [
    'views/ocultapestana.xml'
    ],
    'installable':True,
}

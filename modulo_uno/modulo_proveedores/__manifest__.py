# -*- coding: utf-8 -*-
{
    'name': "Modulo de Personas",
    'summary': """
    """,
    'description': """
        Modulo creado como practica
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
    # le quite --> ,'data/personas_demo.xml'
    'data': ['views/persona_view.xml',
             'views/calendario_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}


#              'reports/reporte_cal.xml',
#              'reports/calendario_qweb.xml',

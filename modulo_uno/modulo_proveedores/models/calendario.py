# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class Calendario (models.Model):
    _name = 'personas.calendario'

    name = fields.Char(
        string="Descripcion Evento"
    )
    color = fields.Char(
        string="Color",
        help="Elige el color",
        size=7,
        store = True
    )
    date_start = fields.Datetime(
        string='Fecha inicio',
        default=fields.Datetime.now,
        store=True
    )

    date_stop = fields.Datetime(
        string='Fecha termino',
        default=fields.Datetime.now,
        store = True
    )

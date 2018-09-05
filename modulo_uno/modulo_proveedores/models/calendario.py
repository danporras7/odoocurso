# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta

class Calendario (models.Model):
    _name = 'personas.calendario'

    name = fields.Char(
        string="Descripcion Evento"
    )
    color = fields.Integer(
        string="Color",
    )
    date_start = fields.Datetime(
        string='Fecha inicio',
        default=datetime.now()
    )
    date_stop = fields.Date(
        string='Fecha termino',
        default = datetime.now()
    )

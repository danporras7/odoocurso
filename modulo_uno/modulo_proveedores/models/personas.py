# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Personas (models.Model):
    _name = 'personas.informacion_data'

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )

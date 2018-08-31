# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Grados_estudio (models.Model):
    _name = 'grados_estudio.informacion_data'

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )

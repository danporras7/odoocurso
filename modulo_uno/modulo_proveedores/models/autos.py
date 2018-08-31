# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Autos (models.Model):
    _name = 'autos.informacion_data'

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )

# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Nombre_cuentas_email (models.Model):
    _name = 'nombre_cuentas_email.informacion_data'

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )

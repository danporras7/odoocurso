# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class NombresCuentasEmail (models.Model):
    _name = 'personas.nombre_cuentas_email'

    name = fields.Char(
        string="Dominio",
        required=True,
    )
    dominio_publico = fields.Boolean(
        string="¿El dominio es público?",
    )

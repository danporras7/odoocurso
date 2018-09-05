# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Unidades (models.Model):
    _name = 'unidades.catalogo'

    name = fields.Char(
        string="Unidad",
    )

    nombre = fields.Char(
        string="Nombre de la Unidad",
    )
    #persona_id=fields.Many2one('refaccion.main_data',string="Unidad",)

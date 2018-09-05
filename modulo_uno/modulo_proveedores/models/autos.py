# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Autos (models.Model):
    _name = 'personas.autos'

    name = fields.Char(
        string="Matricula",
    )
    color = fields.Char(
        string="Color",
    )
    anio = fields.Char(
        string="Año",
    )

    persona_id=fields.Many2one('persona.main_data',string="Persona",)

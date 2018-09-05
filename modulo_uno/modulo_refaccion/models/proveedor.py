# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Proveedor (models.Model):
    _name = 'proveedor.catalogo'

    name = fields.Char(
        string="Nombre",
    )

    direccion = fields.Char(
        string="Dirección",
    )
    email = fields.Char(
        string="Correo",
    )

    proveedor_ids = fields.Many2many('refaccion.main_data', string="Refacciones de este proveedor")

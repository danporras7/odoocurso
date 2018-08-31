# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Module_demo (models.Model):
    _name = 'module_demo.informacion_data'

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )

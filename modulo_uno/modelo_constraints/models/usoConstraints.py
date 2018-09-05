from odoo import fields, models, api

class apiConstrainOdoo(models.Model):
    _inherit = 'product.template'

    _sql_constraint = [('default_code_uniq', 'unique(default_code)', ('¡la referencia es unica!'))]

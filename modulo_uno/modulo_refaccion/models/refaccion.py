# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Refaccion(models.Model): #paquete.clase
    _name = 'refaccion.main_data' #por convencion nombre significativo.loque se va a guardar, name siempre se ha de poner

    name = fields.Char(
                       string="Descripción de la Refacción", #es una etiqueta
                       required=True,
                       help="Indique la refacción",
                       index=True,
                       )

    descripcion = fields.Char( string="Caracterizticas de la refacción", )

    foto = fields.Binary(string="Foto", help="Agregue la foto de la refacción")

    fecha = fields.Datetime(string="Fecha de registro",)

    proveedor = fields.Char(string="Proveedor",)

    unidad = fields.Char(string="Unidad de venta",)

    proveedor_ids = fields.Many2many('proveedor.catalogo', string="Proveedores que lo venden")

    unidad_ids = fields.Many2one('unidades.catalogo', string="Unidades de venta")

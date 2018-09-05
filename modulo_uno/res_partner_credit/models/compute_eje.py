import random
from odoo import models, fields, api

# importing the requests library
import requests

class compute_eje(models.Model):
    _inherit = 'res.partner'

    nss = fields.Char(string='Num. Seguridad Social')
    porcentaje = fields.Float(compute='_muestra_porcentaje')
    instructor_id = fields.Many2one('res.company', string="Instructor")

    price = fields.Float(string = "Precio",store=True)
    unit_price = fields.Float(string = "Precio unitario")
    amount = fields.Float(string = "Monto")

    geolocaliza = fields.Char(string = "Maps pos",store=True)

    #instructor_id = fields.Many2one('res.company', 'company_id', string="Instructor")

    #barcode = fields.Char(compute='_actualizaId')
    #barcode = fields.Char(compute='_compute_name')
    #name = fields.Char(compute='_obtiene_valor')
    #codigo = fields.Char(related='barcode',store=True)

    #@api.one, depends, onchange, model
    # self es una palabra reservada, referencia del registro editando

    @api.multi
    def _actualizaId(self):
    	for record in self:
    		identificador = str(record.id)
    		record.barcode = identificador

    @api.multi
    def _compute_name(self):
        for record in self:
            identificador = str(random.randint(1, 1e6))
            record.barcode = identificador

    @api.depends('credit_limit')
    def _muestra_porcentaje(self):
        for record in self:
            if not record.credit_limit:
                record.credit_limit = 0.0
            if record.credit_limit>100000.0:
                record.credit_limit = 100000.0
            record.porcentaje = record.credit_limit/100000.0 * 100

    # onchange handler
    @api.onchange('amount', 'unit_price') # 'amount', 'unit_price', 'price'
    def _onchange_price(self):
        # set auto-changing field
        self.price = self.amount * self.unit_price
        # Can optionally return a warning and domains
        return {
            'warning': {
                'title': "Algo malo paso",
                'message': "En verdad, mejor vende algo %s" % str(self.price),
            }
        }

    @api.onchange('price')
    def _onchange_monto(self):

        # api-endpoint
        URL = "http://maps.googleapis.com/maps/api/geocode/json"

        # location given here
        location = "zocalo oaxaca mexico"

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'address': location}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format
        data = r.json()

        # extracting latitude, longitude and formatted address
        # of the first matching location
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        formatted_address = data['results'][0]['formatted_address']

        # printing the output
        #print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
        #      % (latitude, longitude, formatted_address))

        self.geolocaliza = "Latitude:%s, Longitude:%s Formatted Address:%s" % (latitude, longitude, formatted_address)

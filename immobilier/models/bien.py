from odoo import models, fields

class BienImmobilier(models.Model):
    _name = "immobilier.bien"
    _description = "Bien immobilier"

    name = fields.Char(string="Nom du bien", required=True)
    prix = fields.Float(string="Prix")
    surface = fields.Float(string="Surface (m²)")
    disponible = fields.Boolean(string="Disponible", default=True)
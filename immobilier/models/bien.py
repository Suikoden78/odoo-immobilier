from odoo import models, fields

class BienImmobilier(models.Model):
    _name = "immobilier.bien"
    _description = "Bien immobilier"

    x_bien_titre_du_bien = fields.Char(string="Titre du bien", required=True)
    x_bien_reference = fields.Char(string="Référence")
    x_bien_statut = fields.Char(string="Statut")
    x_bien_prix_du_bien = fields.Float(string="Prix")
    x_bien_surface_habitable = fields.Float(string="Surface habitable (m²)")
    x_bien_surface_du_terrain = fields.Float(string="Surface du terrain (m²)")
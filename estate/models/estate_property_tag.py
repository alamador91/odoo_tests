from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = 're.estate.property.tag'
    _description = 'Property Tag'
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

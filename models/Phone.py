from odoo import models, fields


class Phone(models.Model):
    _name = "phone.model"
    description = "Phone"

    name = fields.Char()
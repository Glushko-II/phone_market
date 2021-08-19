from odoo import models, fields


class PhoneManufacturer(models.Model):
    _name = "phone.manufacturer"
    _description = "Phone Manufacturer"

    name = fields.Char()


class PhoneModel(models.Model):
    _name = "phone.model"
    _description = "Phone Model"

    name = fields.Char()


class Phone(models.Model):
    _name = "phone"
    _description = "Phone"

    name = fields.Char()
    manufacturer_ids = fields.Many2many('phone.manufacturer', string='Phone manufacturers')
    model_ids = fields.Many2many('phone.model', string='Phone models')

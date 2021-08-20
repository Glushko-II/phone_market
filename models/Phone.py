from odoo import models, fields, api


class PhoneManufacturer(models.Model):
    _name = "phone.manufacturer"
    _description = "Phone Manufacturer"

    name = fields.Char()
#    phone_id = fields.Many2one('phone')


class PhoneModel(models.Model):
    _name = "phone.model"
    _description = "Phone Model"

    name = fields.Char()
#    phone_id = fields.Many2one('phone')


class Phone(models.Model):
    _name = "phone"
    _description = "Phone"

    manufacturer_ids = fields.Many2one('phone.manufacturer', string='Manufacturer')
    model_ids = fields.Many2one('phone.model', string='Model')

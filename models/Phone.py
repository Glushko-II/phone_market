from odoo import models, fields, api


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

    manufacturer_ids = fields.Many2one('phone.manufacturer', string='Manufacturer')
    model_ids = fields.Many2one('phone.model', string='Model')


class Orders(models.Model):
    _name = "orders"
    _description = "Orders"

    manufacturer_ids = fields.Many2one('phone.manufacturer', string='Manufacturer')
    model_ids = fields.Many2one('phone.model', string='Model')
    order_date = fields.Date(default=fields.Date.today, tracking=True)
    

    @api.onchange('manufacturer_ids')
    def set_domain_for_model_id(self):
        class_obj = self.env['phone'].search([('manufacturer_ids', '=', self.manufacturer_ids.id)])
        model_list = []
        for data in class_obj:
            model_list.append(data.model_ids.id)

        res = {}
        res['domain'] = {'model_ids': [('id', 'in', model_list)]}
        return res

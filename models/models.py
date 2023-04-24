# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class shohan-erp(models.Model):
#     _name = 'shohan-erp.shohan-erp'
#     _description = 'shohan-erp.shohan-erp'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

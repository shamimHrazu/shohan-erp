# -*- coding: utf-8 -*-
# from odoo import http


# class Shohan-erp(http.Controller):
#     @http.route('/shohan-erp/shohan-erp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shohan-erp/shohan-erp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('shohan-erp.listing', {
#             'root': '/shohan-erp/shohan-erp',
#             'objects': http.request.env['shohan-erp.shohan-erp'].search([]),
#         })

#     @http.route('/shohan-erp/shohan-erp/objects/<model("shohan-erp.shohan-erp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shohan-erp.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class ExcerciseSaleOrder(http.Controller):
#     @http.route('/excercise_sale_order/excercise_sale_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/excercise_sale_order/excercise_sale_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('excercise_sale_order.listing', {
#             'root': '/excercise_sale_order/excercise_sale_order',
#             'objects': http.request.env['excercise_sale_order.excercise_sale_order'].search([]),
#         })

#     @http.route('/excercise_sale_order/excercise_sale_order/objects/<model("excercise_sale_order.excercise_sale_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('excercise_sale_order.object', {
#             'object': obj
#         })


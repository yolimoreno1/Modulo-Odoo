# -*- coding: utf-8 -*-
# from odoo import http


# class Formacionymr(http.Controller):
#     @http.route('/formacionymr/formacionymr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formacionymr/formacionymr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formacionymr.listing', {
#             'root': '/formacionymr/formacionymr',
#             'objects': http.request.env['formacionymr.formacionymr'].search([]),
#         })

#     @http.route('/formacionymr/formacionymr/objects/<model("formacionymr.formacionymr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formacionymr.object', {
#             'object': obj
#         })

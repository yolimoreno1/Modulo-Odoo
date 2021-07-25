# -*- coding: utf-8 -*-

from odoo import models, fields


class Employee(models.Model):
    _inherit = 'hr.employee'

    is_student = fields.Boolean(string='Is student', default=False)
    id_acciones = fields.Many2many('formacionymr.acciones', string='Training Actions')
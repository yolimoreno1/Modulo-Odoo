# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean('Teacher', default=False)
    id_especialidades = fields.Many2many('formacionymr.especialidades')
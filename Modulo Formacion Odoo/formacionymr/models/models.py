# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cursos(models.Model):
    _name = 'formacionymr.cursos'
    _description = 'formacionymr.cursos'

    name = fields.Char('Nombre', required=True)
    description = fields.Text()
    grade = fields.Selection([('first', 'Proximamente'), ('second', 'En curso'),
                              ('third', 'Finalizado')], string='Estado', required=True)
    time = fields.Integer('Horas del curso', default=1)
    hours = fields.Integer('Horas por sesion', default=1)
    sessions = fields.Integer('Sesiones', compute='_sessions_time')
    id = fields.Char('ID', required=True)
    date_begin = fields.Date('F.Inicio', required=True)
    date_end = fields.Date('F.Fin', required=True)
    hour_begin = fields.Float('Inicio de la clase')
    hour_end = fields.Float('Fin de la clase')
    day = fields.Many2many('formacionymr.weekday', string='Dias de la semana', required=True)
    id_especialidades = fields.Many2one('formacionymr.especialidades', string='Especialidad')
    id_acciones = fields.One2many('formacionymr.acciones', inverse_name='id_cursos')
    name_partner = fields.Char(related='id_especialidades.name_partner')

    @api.depends('time', 'hours')
    def _sessions_time(self):
        if self.time > 0 and self.hours > 0:
            self.sessions = self.time / self.hours


class weekday(models.Model):
    _name = 'formacionymr.weekday'
    _description = 'formacionymr.weekday'

    name = fields.Selection([('Lunes', 'Lunes'),
                             ('Martes', 'Martes'), ('Miercoles', 'Miercoles'),
                             ('Jueves', 'Jueves'), ('Viernes', 'Viernes')], string='Dia de la semana', required=True)
    color = fields.Integer()
    description = fields.Text()


class acciones(models.Model):
    _name = 'formacionymr.acciones'
    _description = 'formacionymr.acciones'
    _order = 'id_cursos'

    name = fields.Char(related='id_cursos.name', requires=True)
    status = fields.Selection(related='id_cursos.grade', string='Estado')
    date_begin = fields.Date(related='id_cursos.date_begin', string='Inicio del curso')
    date_end = fields.Date(related='id_cursos.date_end', string='Fin del curso')
    id_cursos = fields.Many2one('formacionymr.cursos', string='Curso', ondelete='cascade')
    id_employee = fields.Many2many('hr.employee', string='Empleados', ondelete='cascade')
    id_partner = fields.Many2one('res.partner', string='Formador')
    name_partner = fields.Char(related='id_cursos.name_partner')


class especialidades(models.Model):
    _name = 'formacionymr.especialidades'
    _description = 'formacionymr.especialidades'

    name = fields.Char('Especialidad', required=True)
    is_teacher = fields.Boolean(related='id_partner.is_teacher')
    id_partner = fields.Many2many('res.partner', 'id_especialidades', string='Formador', required=True)
    name_partner = fields.Char(related='id_partner.name')
    description = fields.Text('Descripcion')

from odoo import models


class Employee(models.Model):
    _name = 'hr.employee'
    _inherit = ['hr.employee', 'email.proxy.mixin']

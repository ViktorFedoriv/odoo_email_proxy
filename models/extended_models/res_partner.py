from odoo import models


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner', 'email.proxy.mixin']

from odoo import fields, models


class SeedTemplate(models.Model):
    _name = 'hr.payroll.co.seed.template'
    _description = 'Seed Template'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Description')

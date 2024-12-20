from odoo import models, fields, api

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    is_instructure = fields.Boolean(string="Is Instructure")

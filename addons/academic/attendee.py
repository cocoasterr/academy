from odoo import models, fields, api

class Attendee(models.Model):# package bawaan odoo
    _name = "academic.attendee" #identity nama class odoo secara general
    _description = "Attendee model for academic purposes"  # Deskripsi model
    
    name = fields.Char(string="Name", required = True)
    session_id = fields.Many2one(comodel_name="academic.session",
                                     string="Session ID", required = True)
        
    partner_id = fields.Many2one(comodel_name="res.partner",
                                     string="Partner ID", required = True)
    
    @api.onchange('partner_id')
    def _on_change_partner_id(self):
        self.name = self.partner_id.name
        
        
    # to avoid mutliple atendee with _sql_constraints
    _sql_constraints = [
        ("partner_session_unique","UNIQUE(session_id, partner_id)","Multiple partner detected!")
    ]
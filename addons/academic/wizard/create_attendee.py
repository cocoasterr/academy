from odoo import models, fields, api

# transient model itu tidak di create di database
class CreateAttendeeWizard(models.TransientModel):
    _name = "academic.create.attendee.wizard"
    _description = "Create Attendee Wizard"
    
    session_id = fields.Many2one(comodel_name="academic.session",
                                 string="Session ID", 
                                #  required = True)
                                )
    
    partner_ids = fields.Many2many(comodel_name="res.partner",
                                   string="Partner ID", required = True)
    
    session_ids = fields.Many2many(comodel_name="academic.session",
                                   string="sessions", required = True)
    
    def action_add_attendee(self):
        self.ensure_one()
        
        # one to many
        # self.session_id.attendee_ids = [
        #         (0, 0, {
        #             "partner_id": partner.id,
        #             "name": f"{partner.name} - {self.session_id.name}"
        #         }) 
        #         for partner in self.partner_ids
        #     ]
        
        # many to many
        for ses in self.session_ids:
            ses.attendee_ids = [
                (0, 0, {
                    "partner_id": partner.id,
                    "name": f"{partner.name} - {self.session_id.name}"
                }) 
                for partner in self.partner_ids
            ]
        
        return {
            "type": "ir.actions.act_window_close",
        }

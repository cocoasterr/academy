from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):# package bawaan odoo
    _name = "academic.session" #identity nama class odoo secara general
    _description = "Session model for academic purposes"  # Deskripsi model
    
    name = fields.Char(string="Name", required = True)
    course_id = fields.Many2one(comodel_name="academic.course",
                                string="Course", required = True) 
    instructure_id = fields.Many2one(comodel_name="res.partner",
                                     string="Instructure ID", required = True)
    start_date = fields.Date(string="Date", default=fields.Date.context_today)
    duration = fields.Integer(string="Duration")
    seats = fields.Integer(string="Seats")
    active = fields.Boolean(string="Active", default=True)
    
    attendee_ids = fields.One2many(
        comodel_name="academic.attendee",
        string="Attendees",
        inverse_name="session_id",
        ondelete="cascade",
        )
    
    image_session = fields.Binary(string="Image Session")
    
    # compute field example, jadi _calc_taken_seats itu func dari class Session
    percentage_taken_seats = fields.Float(string="Percentage Taken Seats", 
                               compute="_calc_taken_seats",
                            #    store=True, kalau mau disimpan in memory
                               )
    
    state = fields.Selection(
        string="state",
        selection=[("draft", "Draft"), ("open","Open"), ("done", "Done")],
        required=True,
        readonly=True,
        default="draft",
        )
    
    def action_draft(self):
        self.state = "draft"
    
    def action_open(self):
        self.state = "open"

    def action_done(self):
        self.state = "done"
    
    # lalu buat class nya
    def _calc_taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.percentage_taken_seats = 100.0 * (len(rec.attendee_ids) / rec.seats)
            else:
                rec.percentage_taken_seats = 0.0
                
    # Event on change
    # Jika field seats dan attendee_ids berubah (bertambah/berkurang), maka function ini akan terpanggil
    @api.onchange('seats','attendee_ids')
    def _on_change_taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.percentage_taken_seats = 100.0 * (len(rec.attendee_ids) / rec.seats)
            else:
                rec.percentage_taken_seats = 0.0
                
    # untuk memvalidasi sebelum simpan database
    # kalau sudah menjadi instructure tidak boleh menjadi peserta
    @api.constrains('instructure_id', 'attendee_ids')
    def _check_instructure(self):
        for session in self:
            # apakah instructure_id ada disalah satu attendee id    
            # jika ada validation error
            partner_ids = []
            for attendee in session.attendee_ids:
                partner_ids.append(attendee.partner_id.id)
            if session.instructure_id.id in partner_ids:
                # if not valid
                raise ValidationError("Instructure cannot be Attendee!")
            
    # contoh: action > duplicate
    def copy (self, default=None):
        self.ensure_one()
        d = dict(default or {},name = f"copy of {self.name}")
        return super(Session, self).copy(default = d)
    
    def open_wizard(self):
        view = self.env.ref('academic.create_attendee_wizard_form')

        wizard = self.env['academic.create.attendee.wizard'].create({
            'session_id': self.id
        })  

        return {
            'name': 'Add Attendee',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'academic.create.attendee.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': wizard.id,
            'context': self.env.context,
        }
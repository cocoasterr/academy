from odoo import models, fields, api

class Course(models.Model):
    _name = "academic.course" #identity nama class odoo secara general
    _description = "Course model for academic purposes"  # Deskripsi model
    
    name = fields.Char(string="Name", required=True) #nama field
    description = fields.Text(string="Description", required = True) #description field
    resposible_id = fields.Many2one(
        comodel_name="res.users",  #to many model
        string="Responsible", # lable
        required = True) #field responsable
    
    
    session_ids = fields.One2many(
        comodel_name="academic.session",
        string="Sessions",
        inverse_name="course_id",
        ondelete="cascade",
        )
    
    # membuat unique
    _sql_constraints = [
        ('check_name_unique', 'unique(name)', 'Course Name already exists!, please change Course Name.'),
        ('check_name_desc_unique', 'CHECK(name <> description)', 'Name and Description cannot be the same.'),
    ]
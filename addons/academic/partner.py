from odoo import models, fields, api

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    is_instructure = fields.Boolean(string="Is Instructure")

    # category_ids = fields.Many2many(
    #     'res.partner.category',  # The model we're relating to
    #     'res_partner_category_rel',  # The relation table (this will be created automatically)
    #     'partner_id',  # The field in the relation table referring to the partner
    #     'category_id',  # The field in the relation table referring to the category
    #     string='Categories'
    # )
    
    # @api.model
    # def default_get(self, fields_list):
    #     """Override default_get to handle default_category_id from context."""
    #     res = super(Partner, self).default_get(fields_list)
    #     default_category_name = self.env.context.get('default_category_id')
    #     if default_category_name:
    #         category = self.env['res.partner.category'].search([('name', 'ilike', default_category_name)], limit=1)
    #         if category:
    #             res['category_ids'] = [(6, 0, [category.id])]
    #     return res
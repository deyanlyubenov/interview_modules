from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    state = fields.Selection([
        ('new', 'New'),
        ('to_validate', 'To be validated'),
        ('validated', 'Validated')
    ], string='State', default='new', required=True, tracking=True)

    @api.model
    def _set_existing_contacts_validated(self):
        contacts = self.search([('state', '!=', 'validated')])
        contacts.write({'state': 'validated'})

    def action_request_validation(self):
        for partner in self:
            partner.state = 'to_validate'

    def action_validate(self):
        for partner in self:
            partner.state = 'validated'

    def action_reject(self):
        for partner in self:
            partner.state = 'new'

    def action_no_validation_needed(self):
        for partner in self:
            partner.state = 'validated'

    @api.model
    def create(self, vals):
        partner = super(ResPartner, self).create(vals)
        if self.env.context.get('installing_module'):
            partner.state = 'validated'
        return partner

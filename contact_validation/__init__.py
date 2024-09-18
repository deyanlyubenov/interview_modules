from odoo import api, SUPERUSER_ID
from . import models

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.partner']._set_existing_contacts_validated()

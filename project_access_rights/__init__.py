from . import models
from odoo import api, SUPERUSER_ID

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    rule = env.ref('project.project_public_members_rule', raise_if_not_found=False)
    if rule:
        rule.sudo().write({'active': True})  # Unarchive the rule on module uninstall

    rule = env.ref('project.project_project_manager_rule', raise_if_not_found=False)
    if rule:
        rule.sudo().write({'active': True})  # Unarchive the rule on module uninstall

    rule = env.ref('project.task_visibility_rule', raise_if_not_found=False)
    if rule:
        rule.sudo().write({'active': True})  # Unarchive the rule on module uninstall

    rule = env.ref('project.project_manager_all_project_tasks_rule', raise_if_not_found=False)
    if rule:
        rule.sudo().write({'active': True})

    rule = env.ref('project.ir_rule_private_task', raise_if_not_found=False)
    if rule:
        rule.sudo().write({'active': True})

from odoo import fields, models
from odoo.osv import expression
from odoo.tools.safe_eval import safe_eval

class IrRule(models.Model):
    _inherit = 'ir.rule'

    force_global = fields.Boolean(string='Force Global', default=False, help='If checked, this rule will be applied even if the global rule is disabled.')

    def _compute_domain(self, model_name, mode="read"):
        rules = self._get_rules(model_name, mode=mode)
        if not rules:
            return

        # browse user and rules as SUPERUSER_ID to avoid access errors!
        eval_context = self._eval_context()
        user_groups = self.env.user.groups_id
        global_domains = []                     # list of domains
        group_domains = []                      # list of domains
        for rule in rules.sudo():
            # evaluate the domain for the current user
            dom = safe_eval(rule.domain_force, eval_context) if rule.domain_force else []
            dom = expression.normalize_domain(dom)
            if rule.force_global and rule.groups & user_groups:
                global_domains.append(dom)
            else:
                if not rule.groups:
                    global_domains.append(dom)
                elif rule.groups & user_groups:
                    group_domains.append(dom)

        # combine global domains and group domains
        if not group_domains:
            return expression.AND(global_domains)
        return expression.AND(global_domains + [expression.OR(group_domains)])
# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ReturnedCheckReport(models.Model):
    _name = 'account.returned.check.report'
    _description = 'Returned Check Report'

    reason_id = fields.Many2one(comodel_name='reason.rejected.check', string='Reason',
                                domain="[('type', '=', 'returned')]")
    date_since = fields.Date(string='Since')
    date_to = fields.Date(string='To')
    replaced = fields.Selection([('yes', 'Yes'), ('no', 'No'), ('all', 'All')], string='Replaced', default='all')
    check_qty = fields.Integer(string='Found Checks', compute='_compute_returned_check_qty')

    @api.onchange('date_since', 'date_to', 'reason_id', 'replaced')
    def _compute_returned_check_qty(self):
        for rec in self:
            returned_checks = rec._compute_returned_check_ids()
            rec.check_qty = len(returned_checks) if returned_checks else 0

    def _compute_returned_check_ids(self):
        domain = [('state', '=', 'returned')]

        if self.date_since:
            domain.append(('return_date', '>=', self.date_since))
        if self.date_to:
            domain.append(('return_date', '<=', self.date_to))
        if self.reason_id:
            domain.append(('reason_id', '=', self.reason_id.id))
        if self.replaced != 'all':
            replaced = True if self.replaced == 'yes' else False
            domain.append(('replaced', '=', replaced))

        returned_checks = self.env['account.issued.check'].search(domain)
        return returned_checks

    def print_report(self):
        returned_checks = self._compute_returned_check_ids()
        if returned_checks:
            data = {'ids': returned_checks.ids,
                    'model': 'account.issued.check',
                    'form': self.read()[0],
                    }
            return {
                'data': data,
                'type': 'ir.actions.report',
                'report_name': 'report_xlsx.report_returned_check',
                'report_type': 'xlsx',
                'report_file': 'returned_checks',
                'name': 'Report returned checks',
            }
        raise UserError("Empty report.")


class RejectedThirdCheckReport(models.Model):
    _name = 'rejected.third.check.report'
    _description = 'Rejected Check Report'

    reason_id = fields.Many2one(comodel_name='reason.rejected.check', string='Reason',
                                domain="[('type', '=', 'rejected')]")
    date_since = fields.Date(string='Since')
    date_to = fields.Date(string='To')
    check_qty = fields.Integer(string='Found Checks', compute='_compute_rejected_check_qty')
    owner_type = fields.Selection([('own', 'Own'), ('third', 'Third'), ('all', 'All')], string='Owner', default='all')

    @api.onchange('date_since', 'date_to', 'reason_id', 'owner_type')
    def _compute_rejected_check_qty(self):
        for rec in self:
            rejected_checks = rec._compute_rejected_check_ids()
            rec.check_qty = len(rejected_checks) if rejected_checks else 0

    def _compute_rejected_check_ids(self):
        domain = [('state', '=', 'rejected')]

        if self.date_since:
            domain.append(('reject_date', '>=', self.date_since))
        if self.date_to:
            domain.append(('reject_date', '<=', self.date_to))
        if self.reason_id:
            domain.append(('reason_id', '=', self.reason_id.id))
        if self.owner_type != 'all':
            domain.append(('check_issuing_type', '=', self.owner_type))

        rejected_checks = self.env['account.third.check'].search(domain)
        return rejected_checks

    def print_report(self):
        rejected_checks = self._compute_rejected_check_ids()
        if rejected_checks:
            data = {'ids': rejected_checks.ids,
                    'model': 'account.third.check',
                    'form': self.read()[0],
                    }
            return {
                'data': data,
                'type': 'ir.actions.report',
                'report_name': 'report_xlsx.report_rejected_third_check',
                'report_type': 'xlsx',
                'report_file': 'rejected_third_checks',
                'name': 'Report rejected checks',
            }
        raise UserError("Empty report.")

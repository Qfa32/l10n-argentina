##############################################################################
#   Copyright (c) 2018 Eynes/E-MIPS (www.eynes.com.ar)
#   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PerceptionPerception(models.Model):
    _name = "perception.perception"
    _inherit = "perception.perception"

    from_register_ARBA = fields.Boolean('From ARBA Register')
    from_register_AGIP = fields.Boolean('From AGIP Register')
    from_register_AGIP_RP = fields.Boolean('From AGIP Register')
    from_register_SANTA_FE = fields.Boolean('From SANTA FE Register')
    from_register_JUJUY = fields.Boolean('From JUJUY Register')
    from_register_TUCUMAN = fields.Boolean('From TUCUMAN Register')

    @api.model
    def _get_perception_from_arba(self):
        ret = self.search([('from_register_ARBA', '=', True)])
        if len(ret) > 1:
            raise ValidationError(
                _('Perceptions Improperly Configured\n') +
                _('You can not have more than one perception to update ' +
                  'from ARBA. Please review configuration'))
        elif len(ret) == 0:
            return False
        else:
            return ret

    @api.model
    def _get_perception_from_agip(self):
        ret = self.search([('from_register_AGIP', '=', True)])
        if len(ret) > 1:
            raise ValidationError(
                _('Perceptions Improperly Configured\n') +
                _('You can not have more than one perception to update ' +
                  'from AGIP. Please review configuration'))
        elif len(ret) == 0:
            return False
        else:
            return ret
    @api.model
    def _get_perception_from_agip_rp(self):
        ret = self.search([('from_register_AGIP_RP', '=', True)])
        if len(ret) > 1:
            raise ValidationError(
                _('Perceptions Improperly Configured\n') +
                _('You can not have more than one perception to update ' +
                  'from AGIP. Please review configuration'))
        elif len(ret) == 0:
            return False
        else:
            return ret

    @api.model
    def _get_perception_from_santa_fe(self):
        ret = self.search([('from_register_SANTA_FE', '=', True)])
        if len(ret) > 1:
            raise ValidationError(
                _('Perceptions Improperly Configured\n') +
                _('You can not have more than one perception to update ' +
                  'from SANTA_FE. Please review configuration'))
        elif len(ret) == 0:
            return False
        else:
            return ret

    @api.model
    def _get_perception_from_jujuy(self):
        ret = self.search([('from_register_JUJUY', '=', True)])
        if len(ret) > 1:
            raise ValidationError(
                _('Perceptions Improperly Configured\n') +
                _('You can not have more than one perception to update ' +
                  'from SANTA_FE. Please review configuration'))
        elif len(ret) == 0:
            return False
        else:
            return ret

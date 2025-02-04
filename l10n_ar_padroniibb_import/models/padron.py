##############################################################################
#   Copyright (c) 2018 Eynes/E-MIPS (www.eynes.com.ar)
#   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
##############################################################################

from odoo import models, fields
from odoo.exceptions import ValidationError

class TemplatePadron(models.Model):
    _name = 'padron.template'

    def unlink(self):
        for record in self:
            query_retention = """
                DELETE FROM res_partner_retention
                WHERE partner_id IN (SELECT id FROM res_partner WHERE vat = %s)
                AND from_padron = True
            """

            query_perception = """
                DELETE FROM res_partner_perception
                WHERE partner_id IN (SELECT id FROM res_partner WHERE vat = %s)
                AND from_padron = True
            """

            try:
                self.env.cr.execute(query_retention, (record.vat,))
                self.env.cr.execute(query_perception, (record.vat,))
                self.env.cr.commit()
            except Exception as e:
                raise ValidationError(e)

        return super(TemplatePadron, self).unlink()


class AgipRetentionGroup(models.Model):
    _name = 'agip.retention.group'
    _description = 'Group number of Retention'

    name = fields.Char('Group Number', size=2, index=1)
    aliquot = fields.Float("Aliquot", digits=(3, 2))

class AgipRetentionGroupRP(models.Model):
    _name = 'agip.perception.group.rp'
    _inherit = 'agip.retention.group'
    _description = 'Group number of Perception'

class AgipPerceptionGroup(models.Model):
    _name = 'agip.perception.group'
    _description = 'Group number of Perception'

    name = fields.Char('Group Number', size=2, index=1)
    aliquot = fields.Float("Aliquot", digits=(3, 2))

class AgipPerceptionGroupRP(models.Model):
    _name = 'agip.perception.group.rp'
    _inherit = 'agip.perception.group'
    _description = 'Group number of Perception'

class AgipRetentions(TemplatePadron):
    """
    This model represent the agip csv file that defines percentage
    of retentions and perceptions
    """
    _name = 'padron.agip_percentages'
    _description = 'Definition of percentages of taxes by customer'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    percentage_perception = fields.Float('Percentage of perception')
    percentage_retention = fields.Float('Percentage of retention')
    multilateral = fields.Boolean('Is multilateral?')
    name_partner = fields.Text('Company name')
    group_retention_id = fields.Many2one(
        'agip.retention.group', 'Retention Group')
    group_perception_id = fields.Many2one(
        'agip.perception.group', 'Perception Group')

class AgipRetentionsRP(models.Model):
    """
    This model represent the agip csv file that defines percentage
    of retentions and perceptions
    """
    _name = 'padron.agip_percentages.rp'
    _inherit = 'padron.agip_percentages'
    _description = 'Definition of percentages of taxes by customer'

    group_retention_id = fields.Many2one(
        'agip.retention.group.rp', 'Retention Group')
    group_perception_id = fields.Many2one(
        'agip.perception.group.rp', 'Perception Group')


class ArbaPerceptions(TemplatePadron):
    """
    This model represent de ARBA csv file that
    defines percentage of perceptions
    """
    _name = 'padron.arba_perception'
    _description = 'Definition of arba percentages of perception'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    percentage_perception = fields.Float('Percentage of perception')
    multilateral = fields.Boolean('Is multilateral?')


class ArbaRetentions(TemplatePadron):
    """
    This model represent de ARBA csv file that
    defines percentage of retention
    """
    _name = 'padron.arba_retention'
    _description = 'Definition of arba percentages of retention'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    percentage_retention = fields.Float('Percentage of retention')
    multilateral = fields.Boolean('Is multilateral?')

class SantaFePerceptions(TemplatePadron):
    """
    This model represent the santa fe csv file that defines percentage
    of retentions and perceptions
    """
    _name = 'padron.santa_fe_percentages'
    _description = 'Definition of percentages of taxes by customer'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    percentage_perception = fields.Float('Percentage of perception')
    percentage_retention = fields.Float('Percentage of retention')
    multilateral = fields.Boolean('Is multilateral?')
    name_partner = fields.Text('Company name')


class JujuyRetentions(TemplatePadron):
    """
    This model represent the agip csv file that defines percentage
    of retentions and perceptions
    """
    _name = 'padron.jujuy_percentages'
    _description = 'Definition of percentages of taxes by customer'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    percentage_perception = fields.Float('Percentage of perception')
    percentage_retention = fields.Float('Percentage of retention')
    multilateral = fields.Boolean('Is multilateral?')
    name_partner = fields.Text('Company name')

class TucumanPercentages(TemplatePadron):

    _name = 'padron.tucuman_acreditan'
    _description = 'Definition of percentages of taxes by customer'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    u1 = fields.Char('Grupo')
    percentage_perception = fields.Float('Percentage of perception')
    multilateral = fields.Boolean('Is multilateral?')
    coeficiente = fields.Float("Coeficiente")

class TucumanCoefiecient(TemplatePadron):

    _name = 'padron.tucuman_coeficiente'
    _description = 'Definition of percentages of taxes by customer'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    u1 = fields.Char('Grupo')
    percentage_perception = fields.Float('Percentage of perception')
    multilateral = fields.Boolean('Is multilateral?')
    coeficiente = fields.Float("Coeficiente")

class CordobaPerceptions(TemplatePadron):
    """
    This model represent de ARBA csv file that
    defines percentage of perceptions
    """
    _name = 'padron.cordoba_perception'
    _description = 'Definition of arba percentages of perception'

    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    vat = fields.Char('Afip code', size=15, index=1)
    percentage_perception = fields.Float('Percentage of perception')
    percentage_retention = fields.Float('Percentage of retention')
    multilateral = fields.Boolean('Is multilateral?')
    name_partner = fields.Text('Company name')

class FormosaPadron(TemplatePadron):
    _name = 'padron.formosa'
    _description = 'Definition of percentages of taxes by customer'

    vat = fields.Char('CUIT', size=11)
    denomination = fields.Text('Denomination')
    period = fields.Char('Period')
    category = fields.Char('Category', size=20)
    category_description = fields.Char('Category description', size=18)
    ac_ret_28_97 = fields.Float('Alicuota retention rg 28 97', size=6)
    ac_per_23_14 = fields.Float('Alicuota perception rg 23 14', size=6)
    date_ret_28_97 = fields.Date('Date retention rg 28 97')
    date_per_23_14 = fields.Date('Date perception rg 23 14')
    ac_per_33_99 = fields.Float('Alicuota perception rg 33 99', size=6)
    ac_per_27_00 = fields.Float('Alicuota perception rg 27 00', size=6)
    date_per_33_99 = fields.Date('Date perception rg 33 99')
    date_per_27_00 = fields.Date('Date perception rg 27 00')
    regime = fields.Text('Regime')
    exent = fields.Boolean('Exent')

class res_country_state(models.Model):
    _name = "res.country.state"
    _inherit = "res.country.state"

    jurisdiction_code = fields.Char(string="Jurisdiction Code", size=15)

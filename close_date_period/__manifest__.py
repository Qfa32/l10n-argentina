###############################################################################
#
#    Copyright (c) 2019 Eynes/E-MIPS (www.eynes.com.ar)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "Close Date Period",
    "category": "L10N AR",
    "version": "12.0.1.0.0",
    "author": "Eynes/E-MIPS",
    "license": "AGPL-3",
    "description": "Allow locking a period to prevent accounting changes.",
    "depends": [
        "base_period",
    ],
    "data": [
        "wizard/date_period_wizard_view.xml",
        "wizard/account_journal_wizard_view.xml",
        #"views/date_period_view.xml",
        "views/account_journal_view.xml",
    ],
    "installable": True,
    "application": True,
}

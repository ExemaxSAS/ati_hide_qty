# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('company_id')
    def change_location_company(self):
        wh = self.env['stock.warehouse'].search([('user_id', '=', self.user_id.id)])

        if wh:
            self.warehouse_id = wh.id
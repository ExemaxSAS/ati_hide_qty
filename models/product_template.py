# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.current_user = self.env.user.id
    
    @api.depends()
    def get_invisible_qty(self):
        for rec in self:
            if rec.current_user == 1 or rec.current_user == 2 or rec.current_user == 23:
                rec.invisi_qty = 0
            else:
                rec.invisi_qty = 1

    def _qty_for_user(self):
        for rec in self:
            rec.qty_for_user = 0
            squant = rec.env['stock.quant'].search([('product_tmpl_id.id','=',rec.id)])
            if len(squant) > 0:
                for u in squant:
                    if u.location_id.user_id.id == rec.env.user.id:
                        rec.qty_for_user += u.available_quantity


    qty_for_user = fields.Float(string="Mi Stock", compute='_qty_for_user')
    
    current_user = fields.Integer(string="Id Current User", compute=_get_current_user)
    invisi_qty = fields.Integer(string="Invisible", compute=get_invisible_qty, default=0)
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.current_user = self.env.user.id
    
    @api.depends()
    def get_invisible_qty(self):
        for rec in self:
            if rec.user_id == rec.current_user or rec.current_user == 1 or rec.current_user == 2:
                rec.invisi_qty = 0
            else:
                rec.invisi_qty = 1

    user_id = fields.Integer(
        string="Id User",
        related="location_id.user_id.id"
    )
    current_user = fields.Integer(string="Id Current User", compute=_get_current_user)
    invisi_qty = fields.Integer(string="Invisible", compute=get_invisible_qty, default=0)
    
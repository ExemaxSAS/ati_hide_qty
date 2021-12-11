# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockLocation(models.Model):
    _inherit = "stock.location"

    def _stock_warehouse(self):
        for location in self:
            location.stock_warehouse = self.env['stock.warehouse'].search([('active', '=', True), '|', ('lot_stock_id', '=', location.id), ('view_location_id', '=', location.id)])

    stock_warehouse = fields.Many2one('stock.warehouse', string="Almacen", compute='_stock_warehouse')
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsable",
        related="stock_warehouse.user_id"
    )

class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    user_id = fields.Many2one('res.users', 'Responsable')
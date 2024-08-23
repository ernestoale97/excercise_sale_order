from odoo import fields, models, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    expiration_date = fields.Date(String="Expiration Date", required=False)
    auto_cancel = fields.Boolean(String="Auto Cancel Expired Orders", default=False)

    @api.model
    def auto_cancel_expired_orders(self):
        today = fields.Date.context_today(self)
        expired_orders = self.search([("expiration_date", "<", today), ("state", "!=", "sale")])
        if self.auto_cancel:
            expired_orders.write({"state": "cancel"})

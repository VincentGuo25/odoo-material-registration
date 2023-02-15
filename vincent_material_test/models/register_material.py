# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError


class RegisterMaterial(models.Model):
    _name = "register.material"
    
    name = fields.Char('Material Name', required=True)
    code = fields.Char('Material Code', required=True)
    material_type = fields.Selection(string="Material Type", selection=[('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')], default='fabric', required=True)
    buy_price = fields.Float('Material Buy Price', required=True)
    related_supplier_id = fields.Many2one('res.partner','Related Supplier', required=True)


    @api.constrains('buy_price')
    def _check_values(self):
        if self.buy_price < 100:
            raise UserError(_('Material Buy Price cannot be lower than 100'))

# -*- coding: utf-8 -*-
from odoo.tests import Form
from odoo.tests.common import TransactionCase


class TestMaterialRegistration(TransactionCase):

    def setUp(self):
        super(TestMaterialRegistration, self).setUp()
        self.register_material_model = self.env['register.material']
        self.res_partner_model = self.env['res.partner']


    def test_material_buy_price(self):
        partner_id = self.res_partner_model.create(dict(name="George"))

        material_form = Form(self.env['register.material'].with_context(tracking_disable=True))
        material_form.name = 'Material-001'
        material_form.code = 'M-001'
        material_form.material_type = 'jeans'
        material_form.buy_price = 200
        material_form.related_supplier_id = partner_id

        register_material = material_form.save()

        status = ''
        if material_form.buy_price < 100:
        	status = 'lower'
        else:
        	status = 'not_lower'

        self.assertEqual('not_lower', status, "The buy price must not lower than 100")
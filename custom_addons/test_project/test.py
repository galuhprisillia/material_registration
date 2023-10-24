from odoo.tests.common import TransactionCase


class TestMaterialRegistration(TransactionCase):
    def setUp(self):
        super(TestMaterialRegistration, self).setUp()
        self.Material = self.env['material.materials']
        self.Supplier = self.env['res.partner']

    def test_create_material(self):
        # Create a new supplier
        supplier_data = {'name': 'Supplier XYZ'}
        supplier = self.Supplier.create(supplier_data)

        # Create a new material
        material_data = {
            'material_code': 'M123',
            'material_name': 'Material A',
            'material_type': 'fabric',
            'material_buy_price': 150.0,
            'supplier_id': supplier.id,
        }
        material = self.Material.create(material_data)

        # Check if material is created
        self.assertTrue(material)
        self.assertEqual(material.material_code, 'M123')

    def test_update_material(self):
        # Create a new supplier
        supplier_data = {'name': 'Supplier XYZ'}
        supplier = self.Supplier.create(supplier_data)

        # Create a new material
        material_data = {
            'material_code': 'M123',
            'material_name': 'Material A',
            'material_type': 'fabric',
            'material_buy_price': 150.0,
            'supplier_id': supplier.id,
        }
        material = self.Material.create(material_data)

        # Update material data
        material.write({'material_buy_price': 200.0})
        self.assertEqual(material.material_buy_price, 200.0)

    def test_delete_material(self):
        # Create a new supplier
        supplier_data = {'name': 'Supplier XYZ'}
        supplier = self.Supplier.create(supplier_data)

        # Create a new material
        material_data = {
            'material_code': 'M123',
            'material_name': 'Material A',
            'material_type': 'fabric',
            'material_buy_price': 150.0,
            'supplier_id': supplier.id,
        }
        material = self.Material.create(material_data)

        # Delete the material
        material.unlink()

        # Check if the material is deleted
        self.assertFalse(material.exists())

    def test_invalid_material_price(self):
        # Try to create a material with an invalid price
        supplier_data = {'name': 'Supplier XYZ'}
        supplier = self.Supplier.create(supplier_data)

        material_data = {
            'material_code': 'M123',
            'material_name': 'Material A',
            'material_type': 'fabric',
            'material_buy_price': 50.0,  # Invalid price
            'supplier_id': supplier.id,
        }

        with self.assertRaises(Exception):
            self.Material.create(material_data)


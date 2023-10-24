from odoo import fields, models, api, _
from odoo.exceptions import Warning, ValidationError


class materials(models.Model):
    _name = 'materials'
    _description = 'list all materials'
    _rec_name = 'material_name'

    material_code = fields.Char(name="Material Code", required=True)
    material_name = fields.Char(name="Material Name", required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], name="Material Type", required=True)
    material_buy_price = fields.Float(name="Material Buy Price", required=True)
    supplier_id = fields.Many2one(comodel_name="res.partner", string="Supplier", required=True)

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        for me in self:
            if me.material_buy_price < 100:
                raise ValidationError(_('Material Buy Price cannot less than 100'))

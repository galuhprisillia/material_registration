from odoo import http
from odoo.http import request
import json


class MaterialController(http.Controller):

    @http.route('/materials', auth='public', methods=['GET'])
    def get_materials(self, **kw):
        params = request.params.get("material_type")
        domain = []
        if params:
            domain = [('material_type', '=', params)]
        materials = request.env['materials'].search(domain)
        material_data = []
        for material in materials:
            material_data.append({
                'material_code': material.material_code,
                'material_name': material.material_name,
                'material_type': material.material_type,
                'material_buy_price': material.material_buy_price,
                'related_supplier': material.supplier_id.name,
            })
        return json.dumps(material_data)

    @http.route('/materials/<int:material_id>', auth='public', methods=['PUT'])
    def update_material(self, material_id, **kw):
        material = request.env['materials'].browse(material_id)
        if material:
            # Update material data based on request
            material.write({
                'material_code': kw.get('material_code'),
                'material_name': kw.get('material_name'),
                'material_type': kw.get('material_type'),
                'material_buy_price': float(kw.get('material_buy_price')),
                'supplier_id': int(kw.get('supplier_id')),
            })
            return json.dumps({'message': 'Material updated successfully'})
        return json.dumps({'message': 'Material not found'})

    @http.route('/materials/<int:material_id>', auth='public', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['materials'].browse(material_id)
        if material:
            material.unlink()
            return json.dumps({'message': 'Material deleted successfully'})
        return json.dumps({'message': 'Material not found'})

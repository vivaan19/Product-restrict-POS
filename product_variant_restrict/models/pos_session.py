from odoo import api, fields, models, tools, _
from odoo.osv.expression import AND, OR

class PosSession(models.Model):
	_inherit = 'pos.session'
	
	def _loader_params_product_product(self):
		
		result = super()._loader_params_product_product()
		
		result['search_params']['fields'].append('bey_pass_counter_ids')
		
		return result
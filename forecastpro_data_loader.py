from openerp.osv import fields, osv, orm
from tempfile import NamedTemporaryFile
from openpyxl import load_workbook
import base64
from openerp.tools.translate import _

class forecastpro_data_sales(osv.osv):
    _name = "forecastpro.data.sales"
    _description = "Forecast Pro sales history per branch"
    _columns = {
        'branch': fields.many2one('res.partner', 'Branch', required=True, select=True),
        'product_id': fields.many2one('product.product', 'Product', required=True, select=True),
        'description': fields.char('Product description'),
        'year': fields.integer('Year'),
        'month': fields.integer('Month'),
        'units': fields.integer('Units sold')
    }

class forecastpro_data_inventory(osv.osv):
    _name = "forecastpro.data.inventory"
    _description = "Forecast Pro sales history per branch"
    _columns = {
        'branch': fields.many2one('res.partner', 'Branch', required=True, select=True),
        'product_id': fields.many2one('product.product', 'Product', required=True, select=True),
        'inventory_type': fields.selection([('onhand', 'Inventory on hand'), ('onorder', 'Inventory on order')], 'Inventory type'),
        'year': fields.integer('Year'),
        'month': fields.integer('Month'),
        'units': fields.integer('Units sold')
    }

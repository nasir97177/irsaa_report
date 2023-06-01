# Copyright (c) 2023, irsaa_report and contributors
# For license information, please see license.txt

# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model import no_value_fields
from frappe.model.document import Document
from frappe.utils import cint, flt


class BOQ(Document):

	@frappe.whitelist()
	def get_items(self):
		self.set("items", [])
		# frappe.msgprint('abc')

		for item in frappe.get_all("Item", {"item_group": self.item_group_item},  ["item_name", "item_code", "stock_uom"]):
				item = {
					"item_code": item.item_code,
					"item_name": item.item_name,
					"uom": item.stock_uom,
					"item_group": item.item_group
				}
			
				self.append("items", item)
    
# 	@frappe.whitelist()
# 	def get_items_groups(self):
# 		self.set("items", [])

# 		for item in frappe.get_all("Item", {"item_group": self.item_group},  ["item_name", "item_code", "stock_uom"]):
# 				item = {
# 					"item_code": item.item_code,
# 					"item_name": item.item_name,
# 					"uom": item.stock_uom,
# 					"item_group": self.item_group
# 				}
			
# 				self.append("items", item)


# @frappe.whitelist()
# def get_items(item_group):
# 	return frappe.get_all("Item", {"item_group": item_group},  ["item_name", "item_code", "stock_uom"])
# @frappe.whitelist()
#  def item_group_item
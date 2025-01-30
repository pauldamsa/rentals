# Copyright (c) 2025, paul damsa and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	def before_save(self):
		self.set_title()

	def set_title(self):
		self.title = self.make + ' ' + self.model + ' ' + str(self.year)
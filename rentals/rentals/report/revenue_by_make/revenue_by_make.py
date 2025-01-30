# Copyright (c) 2025, paul damsa and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data() 
	chart = {
		"data": {
			"labels": [x.make for x in data],
			"datasets": [
				{
					"name": "Total Revenue",
					"values": [x.total_amount for x in data],
				},
			],
		},
		"type":"bar"
	}
	return columns, data, "message summary", chart


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Make"),
			"fieldname": "make",
			"fieldtype": "Data",
		},
		{
			"label": _("Total Revenue"),
			"fieldname": "total_amount ",
			"fieldtype": "Currency",
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	list_ride_booking = frappe.get_all(
		"Ride Booking", 
		fields=["total_amount","vehicle.make"], 
		filters={"docstatus":("<", 2)})
	return list_ride_booking

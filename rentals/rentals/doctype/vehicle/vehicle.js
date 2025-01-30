// Copyright (c) 2025, paul damsa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {

	},
    get_summary(frm){
        frm.get_field("summary").$wrapper.append("<h1>Summary of the vehicle</h1>");
    }
});

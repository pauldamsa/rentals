// Copyright (c) 2025, paul damsa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        if (frm.doc.status === 'New') {
            frm.add_custom_button('Accept', () => {
                frm.set_value('status', 'Accepted')
                frm.save()
            }, "Actions")
        // if (frm.doc.status === 'Rejected') {
        frm.add_custom_button('Reject', () => {
            frm.set_value('status', 'rejected')
            frm.save()
            // })
        }, "Actions")
    }
    },
    status(frm){
        frappe.msgprint('Status changed to ' + frm.doc.status)
    }
});

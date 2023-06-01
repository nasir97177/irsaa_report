// Copyright (c) 2023, irsaa_report and contributors
// For license information, please see license.txt



// cur_frm.fields_dict['item_group'].get_query = function(doc, cdt, cdn) {
// 	return{
// 		filters:{ 'docstatus': 0}
// 	}
// }


// cur_frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
// 	if(!doc.delivery_note) {
// 		frappe.throw(__("Please select a Item Group"));
// 	} else {
// 		return {
			
// 			filters:{ 'item': doc.item}
// 		}
// 	}
// }

// cur_frm.cscript.onload_post_render = function(doc, cdt, cdn) {
// 	if(doc.delivery_note && doc.__islocal) {
// 		cur_frm.cscript.get_items(doc, cdt, cdn);
// 	}
// }

cur_frm.cscript.get_items = function(doc, cdt, cdn) {
	return this.frm.call({
		doc: this.frm.doc,
		method: "get_items",
		callback: function(r) {
			if(!r.exc) cur_frm.refresh();
		}
	});
}
// frappe.prompt([
//     {
//         label: 'Item Group',
//         fieldname: 'item_group',
//         fieldtype: 'Link'
//     },
    
// ], (values) => {
//     console.log(values.first_name, values.last_name);
// })

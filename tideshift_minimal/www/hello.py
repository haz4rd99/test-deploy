import frappe

def get_context(context):
	"""Build context for tideshift test page"""
	context.title = "Tideshift Minimal Test"
	context.message = "If you can see this page, minimal Tideshift deployment works!"
	context.current_time = frappe.utils.now()
	return context

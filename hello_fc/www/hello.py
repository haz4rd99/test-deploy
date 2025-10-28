import frappe

def get_context(context):
	"""Build context for hello page"""
	context.title = "Hello from Frappe Cloud"
	context.message = "If you can see this page, the smoke test passed!"
	context.current_time = frappe.utils.now()
	return context

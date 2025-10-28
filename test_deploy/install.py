# Copyright (c) 2025, Test Deploy and contributors
# For license information, please see license.txt

import frappe

def after_install():
    """Called after app installation"""
    frappe.msgprint("Test Deploy app installed successfully!")
